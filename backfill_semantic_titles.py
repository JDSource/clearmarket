"""
backfill_semantic_titles.py — one-time pass to add semantic_title + telemetry to the wire
items that predate the 2026-06-04 title split (they carry only the old flat `headline`).

Why: the daily cron writes new dated wires but never rewrites past days' files, so the existing
~54 wires would otherwise render via the render-time fallback (a question-form title derived from
event_question). This backfill gives them the same clean dual-surface fields fresh wires get:
  - semantic_title — one batched Claude call, same SEMANTIC_TITLE rule as the generators.
  - telemetry      — composed deterministically in Python (never the LLM), per detection_path.

Idempotent: a wire that already has semantic_title is skipped. Run from repo root:
    python3 backfill_semantic_titles.py            # write
    python3 backfill_semantic_titles.py --dry-run  # preview, no writes
"""
import sys, json, re
from pathlib import Path

import yaml

from gen_news_cycle import claude_json, yz, no_dash, pct, compact_usd, venue_label

ROOT = Path(__file__).parent
SIG_DIR = ROOT / "web/src/content/signals"
DRY = "--dry-run" in sys.argv
# --force re-titles every wire even if it already has a semantic_title (for re-running after a rule change)
FORCE = "--force" in sys.argv

SEMANTIC_TITLE_RULE = (
    "A semantic_title is the durable, indexed title for a prediction-market wire item, written like a "
    "wire-service desk editor (Bloomberg/Reuters register). It reports the MARKET'S CURRENT PRICING STANCE "
    "on the claim. It must NOT predict the real-world outcome ('Karen Bass to win' is BANNED) and must NOT "
    "pose a question ('Will Bass win?' is BANNED). Report how the market is pricing/positioning.\n"
    "SHARED RULES: MAX 62 CHARACTERS — hard limit, count the characters; the long stance tail is the usual "
    "cause of overflow, so keep it to 2-3 words ('a long shot', 'near-certain', 'a coin flip'). NO "
    "probability, NO raw volume, NO venue names, NO math symbols (≥, ≤, ~, %). "
    "Claim-defining figures that DEFINE the market (a strike, level, or date IN the source question) ARE "
    "allowed — spell them out ('4 percent', '$150K', 'by June 30'); only the probability and volume are "
    "forbidden. NUMBER FORMAT: compact notation only — dollar PRICE LEVELS from the claim as $65K or $150K, non-dollar counts/index levels as 30K / 80K (the 24h trading VOLUME is telemetry — NEVER put a volume dollar figure in the title); NEVER spell out 'thousand' or 'million'. Snapshot only — never imply a permanent/final real-world consequence. Do NOT invent a date "
    "or horizon absent from the source question; if it is unclear or templated, omit it rather than guess.\n"
    "BATCH VARIATION (you write all of these in one pass — prevent template bingo): alternate Subject-first "
    "('Bass commands...') and Market-first ('Consensus hardens...') constructions; do NOT reuse the same "
    "opening verb or noun across items; never stack three identical grammar orders in a row.\n"
    "PER-TYPE REGISTER (apply by each item's detection_path; palettes are inspiration, NOT a lookup table):\n"
    "  news_cycle — consensus shifts + narrative alignment. Palette: commands, hardens, solidifies, "
    "fractures, wavers, breaks away, anchors, nears full pricing. e.g. 'Bass commands the LA mayoral race in "
    "prediction pricing'; 'CPI above 4 percent nears full pricing'.\n"
    "  benchmark_drift — macro friction vs the FRED/BLS baseline. Palette: outruns, paces ahead, gaps, lags, "
    "overshoots, tracks tight, detaches. e.g. 'Rate expectations detach from historical target trend'.\n"
    "  cross_venue_divergence — arbitrage spread + fragmentation (venues GENERICALLY, never named). Palette: "
    "splits sharply, decouples, mirrors, spreads, converges, tracks a premium. e.g. 'Anthropic IPO pricing "
    "splits sharply across venues'.\n"
    "  volume_spike — liquidity conviction + capital deployment. Palette: traders pile into, write off, "
    "defend, target, heavy flows test, fade. e.g. 'Traders write off a near-term MicroStrategy Bitcoin sale'; "
    "'A $150K Bitcoin by June sits deep in tail-risk territory'."
)


def split_frontmatter(text):
    """Return (fm_dict, fm_raw_lines, body) for a wire .md. fm_raw_lines preserves exact text."""
    if not text.startswith("---"):
        return None, None, None
    parts = text.split("\n---\n", 1) if "\n---\n" in text else None
    # frontmatter is between the first '---' line and the next '---' line
    lines = text.split("\n")
    assert lines[0].strip() == "---"
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    fm_raw = lines[1:end]
    body = "\n".join(lines[end + 1:])
    fm = yaml.safe_load("\n".join(fm_raw))
    return fm, fm_raw, body


def compose_telemetry(fm):
    dp = fm.get("detection_path")
    pm = fm.get("primary_market") or {}
    price = pm.get("current_price")
    if dp == "cross_venue_divergence":
        rel = (fm.get("related_markets") or [{}])[0]
        a = f"{venue_label(pm.get('platform'))} {pct(price)}"
        b = f"{venue_label(rel.get('platform'))} {pct(rel.get('current_price'))}" if rel.get("platform") else ""
        return f"{a} vs {b}" if b else a
    if dp == "volume_spike":
        vol = compact_usd(pm.get("volume_24h_usd"))
        return f"{pct(price)} · {vol} 24h" if vol else pct(price)
    if dp == "benchmark_drift":
        # benchmark anchor is preserved in sources[0].label as "<label>: <current value>"
        label_full = ((fm.get("sources") or [{}])[0]).get("label", "")
        if ": " in label_full:
            lab, cur = label_full.rsplit(": ", 1)
            return f"{pct(price)} · {lab} {cur}"
        return pct(price)
    # news_cycle (+ default)
    if "ladder" in (fm.get("headline", "").lower()):
        return f"{venue_label(pm.get('platform'))} ladder".strip()
    return f"{venue_label(pm.get('platform'))} {pct(price)}".strip()


def main():
    files = sorted(SIG_DIR.glob("*.md"))
    todo = []
    for fp in files:
        text = fp.read_text()
        fm, fm_raw, body = split_frontmatter(text)
        if fm is None:
            print(f"  skip (no frontmatter): {fp.name}")
            continue
        if fm.get("semantic_title") and not FORCE:
            continue
        todo.append((fp, text, fm, fm_raw, body))

    print(f"{len(todo)}/{len(files)} wires need semantic_title", flush=True)
    if not todo:
        return

    # ---- one batched Claude call for all semantic_titles ----
    # current_market_read carries the actual price/volume so the stance WORD is calibrated to the
    # number (so 31% never reads "likely") — the model sees it but must NOT print it in the title.
    catalog = [{
        "slug": fm.get("signal_slug"),
        "detection_path": fm.get("detection_path"),
        "event_question": fm.get("event_question"),
        "market_question": (fm.get("primary_market") or {}).get("question_raw"),
        "current_market_read": compose_telemetry(fm),
        "old_headline": fm.get("headline"),
    } for (_, _, fm, _, _) in todo]

    system = (
        "You convert prediction-market wire items into clean semantic titles. " + SEMANTIC_TITLE_RULE +
        " Return STRICT JSON only: {\"titles\":[{\"slug\":\"<slug>\",\"semantic_title\":\"<title>\"}]} "
        "with one entry per input slug."
    )
    user = (
        "Produce a semantic_title for each wire. Use event_question / market_question for the claim. "
        "current_market_read gives the ACTUAL current price/volume: your stance word MUST be consistent "
        "with it (a market at 31% is a long shot / skeptically priced, NOT 'likely'; ~50% is a coin flip; "
        ">90% is near-certain) — but do NOT print the number in the title. old_headline shows the "
        "price-laden version to AVOID copying.\n\n"
        + json.dumps(catalog, indent=2)
    )
    result = claude_json(system, user, max_tokens=min(120 * len(todo) + 800, 16000))
    titles = {t["slug"]: t["semantic_title"] for t in result.get("titles", []) if t.get("slug")}
    print(f"  Claude returned {len(titles)} titles", flush=True)

    written = 0
    for (fp, text, fm, fm_raw, body) in todo:
        slug = fm.get("signal_slug")
        st = no_dash((titles.get(slug) or "").strip())
        # deterministic safety net: the rule bans the % sign in the title; convert any slip to "percent"
        st = re.sub(r'(\d(?:\.\d+)?)\s*%', r'\1 percent', st)
        telem = compose_telemetry(fm)
        if not st:
            print(f"  WARN no title for {slug}; leaving fallback", flush=True)
            continue
        # insert semantic_title + telemetry right after the headline: line, preserving everything else.
        # Drop any existing semantic_title:/telemetry: lines first so --force re-writes don't double-key.
        new_fm = []
        for line in fm_raw:
            if line.startswith("semantic_title:") or line.startswith("telemetry:"):
                continue
            new_fm.append(line)
            if line.startswith("headline:"):
                new_fm.append(f"semantic_title: {yz(st)}")
                new_fm.append(f"telemetry: {yz(telem)}")
        out = "---\n" + "\n".join(new_fm) + "\n---\n" + body
        if DRY:
            print(f"\n--- {slug} ---\n  semantic_title: {st}\n  telemetry: {telem}")
        else:
            fp.write_text(out)
        written += 1

    print(f"\n{'(dry-run) would write' if DRY else 'wrote'} {written} wires", flush=True)


if __name__ == "__main__":
    main()
