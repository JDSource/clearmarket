"""
Build-time ladder intercept (tactical pre-launch fix for the CM DATA layer).

The enrichment mislabels multinomial strike-ladder events (Fed rate, CPI, counts) with a wrong
event-level question + an arbitrary 'primary' strike, so the event page / API show garbage
("Fed funds above 4.5% at 99%" when the rate is ~3.5%). The per-market strike data
(threshold/direction/last_price) is correct, so we repair the event records DETERMINISTICALLY,
in place, before the Astro build + D1 seed. No schema migration, no re-enrichment.

For every event that reconstructs as a clean monotonic ladder (ladder_read):
  - event_type = "LADDER"
  - ladder_distribution = {direction, implied_band, strikes:[{threshold,prob}]}
  - question -> clean metric label (Haiku batch; deterministic fallback if no key)
  - primary_market_id -> the sharp-tail anchor strike (a real market with a real price)
Binary/unclean events get event_type="BINARY" and are left untouched.

Run before `cd api && npm run export` (D1 seed) and before `cd web && npm run build`.
Usage: python3 patch_ladders.py [--no-llm]
"""
import json, os, re, sys
from collections import Counter, defaultdict
from pathlib import Path

from gen_news_cycle import ladder_read

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
LABEL_CACHE = ROOT / "data/ladder-labels.json"   # event_id -> clean label; committed + human-editable
NO_LLM = "--no-llm" in sys.argv


def deterministic_label(sample, underlying):
    """Fallback label: prefer the enriched underlying_reference subject; else strip the strike phrase."""
    s = re.sub(r"\b(above|below|more than|less than|greater than|at least|reach|hit)\b.*?\$?\d[\d.,]*\s*%?", "", sample, flags=re.I)
    s = re.sub(r"^(will|how (high|many|much|low)|the number of)\b", "", s.strip(), flags=re.I)
    s = re.sub(r"\b(be|get|go|there)\b", " ", s)
    s = re.sub(r"[?]+$", "", s)
    s = re.sub(r"\s{2,}", " ", s).strip(" ,.")
    return (s[:1].upper() + s[1:]) if s and len(s) > 8 else (underlying[:60].rstrip(". ") if underlying else "Market-implied level")


def llm_labels(rows):
    """One Haiku call per chunk -> clean metric labels. rows: [(sample, underlying, band, slug, resolve)]."""
    from anthropic import Anthropic
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        return None
    client = Anthropic(api_key=key)
    out = []
    for i in range(0, len(rows), 50):
        chunk = rows[i:i + 50]
        listing = "\n".join(
            f'{j}. sample="{s[:65]}" | source="{u[:40]}" | implied_band={b} | slug={sl} | resolves={rv}'
            for j, (s, u, b, sl, rv) in enumerate(chunk)
        )
        sys_p = ("Write a concise, neutral metric label for each prediction-market LADDER event: the "
                 "thing measured + the SPECIFIC period. Derive the period from the slug and resolve date "
                 "(e.g. slug 'kxfed-26jun' -> 'June 2026 meeting'; resolves 2026-05-31 -> 'May 31, 2026'). "
                 "Two events that differ only by period MUST get different labels, so always include the "
                 "specific month/meeting/date, never just the year. Describe the underlying METRIC ONLY, "
                 "NEVER a specific price/strike/threshold/level (the event is a whole distribution, not one "
                 "strike): write 'Bitcoin price, May 30, 2026' NOT 'Bitcoin price above $66,000'; 'Trump "
                 "approval rating, Dec 31, 2026' NOT 'approval rating below 33%'. NO '[X]' placeholders, no "
                 "'Will', no question mark. Examples: 'Federal funds rate upper bound, June 2026 meeting'; 'Core CPI "
                 "month-over-month, May 2026'; 'ICE removals, FY2026'. Return a STRICT JSON array of strings "
                 'in the same order, nothing else.')
        resp = client.messages.create(
            model="claude-haiku-4-5-20251001", max_tokens=2000, system=sys_p,
            messages=[{"role": "user", "content": listing}],
        )
        txt = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
        txt = re.sub(r"^```(?:json)?\s*|\s*```$", "", txt.strip())
        out.extend(json.loads(txt))
    return out


def main():
    b = json.loads(BUNDLE.read_text())
    mbye = defaultdict(list)
    for m in b["markets"]:
        mbye[m.get("event_id")].append(m)

    ladders = []  # (event, ladder_read, sample, underlying)
    for e in b["events"]:
        ms = mbye.get(e["event_id"], [])
        lr = ladder_read(ms) if len(ms) > 4 else None
        if lr:
            sample = lr["sample_question"]
            underlying = next((m.get("underlying_reference") or "" for m in ms), "")
            ladders.append((e, lr, sample, underlying))
            e["event_type"] = "LADDER"
        else:
            e["event_type"] = "BINARY"

    # labels — CACHED by event_id for run-to-run stability. LLM output is non-deterministic, but a
    # reference-data title must not silently reword on every build, so a label is generated once and
    # pinned. Only NEW ladder events hit Haiku; the cache is committed + human-editable (hand-fix a
    # specific label in data/ladder-labels.json and it sticks forever).
    cache = json.loads(LABEL_CACHE.read_text()) if LABEL_CACHE.exists() else {}
    need = [(e, lr, s, u) for (e, lr, s, u) in ladders if e["event_id"] not in cache]
    n_new = 0
    if not NO_LLM and need:
        try:
            rows = [(s, u, lr["implied_band"], e["slug"],
                     (lr["anchor_market"].get("resolve_at") or lr["anchor_market"].get("close_at") or "")[:10])
                    for (e, lr, s, u) in need]
            for (e, _, _, _), lab in zip(need, llm_labels(rows) or []):
                if lab:
                    cache[e["event_id"]] = lab
                    n_new += 1
            LABEL_CACHE.write_text(json.dumps(cache, indent=2, sort_keys=True))
        except Exception as ex:
            print(f"  Haiku label pass failed ({ex}); using cache + deterministic fallback")
    for e, lr, sample, underlying in ladders:
        lo, hi = lr["implied_band"]
        e["ladder_distribution"] = {
            "direction": lr["direction"],
            "implied_band": [lo, hi],
            "strikes": [{"threshold": t, "prob": p} for t, p in lr["strikes"]],
        }
        e["primary_market_id"] = lr["anchor_market"]["market_id"]
        e["question"] = cache.get(e["event_id"]) or deterministic_label(sample, underlying)

    dups = {l: n for l, n in Counter(e["question"] for e, _, _, _ in ladders).items() if n > 1}
    if dups:
        print(f"  WARNING: {len(dups)} duplicate ladder labels — hand-disambiguate in {LABEL_CACHE.name}:")
        for l, n in sorted(dups.items()):
            print(f"    [{n}x] {l}")

    BUNDLE.write_text(json.dumps(b, default=str))
    print(f"patched {len(ladders)} LADDER events / {len(b['events'])} total "
          f"(labels: {len(cache)} cached, {n_new} new this run)")


if __name__ == "__main__":
    main()
