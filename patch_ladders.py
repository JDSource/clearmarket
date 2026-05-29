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
from collections import defaultdict
from pathlib import Path

from gen_news_cycle import ladder_read

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
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
    """One Haiku call per chunk -> clean metric labels. rows: [(sample, underlying, band)]."""
    from anthropic import Anthropic
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        return None
    client = Anthropic(api_key=key)
    out = []
    for i in range(0, len(rows), 50):
        chunk = rows[i:i + 50]
        listing = "\n".join(
            f'{j}. sample="{s[:70]}" | source="{u[:50]}" | implied_band={b}'
            for j, (s, u, b) in enumerate(chunk)
        )
        sys_p = ("Write a concise, neutral metric label for each prediction-market LADDER event: the "
                 "thing measured + the period. NO '[X]' placeholders, no 'Will', no question mark. "
                 "Examples: 'Federal funds rate upper bound, June 2026 meeting'; 'Core CPI month-over-month, "
                 "May 2026'; 'ICE removals, FY2026'; 'US corporate bankruptcies, 2026'. Return a STRICT JSON "
                 'array of strings in the same order, nothing else.')
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

    # labels
    labels = None
    if not NO_LLM and ladders:
        try:
            labels = llm_labels([(s, u, lr["implied_band"]) for _, lr, s, u in ladders])
        except Exception as ex:
            print(f"  Haiku label pass failed ({ex}); using deterministic fallback")
    for idx, (e, lr, sample, underlying) in enumerate(ladders):
        lo, hi = lr["implied_band"]
        e["ladder_distribution"] = {
            "direction": lr["direction"],
            "implied_band": [lo, hi],
            "strikes": [{"threshold": t, "prob": p} for t, p in lr["strikes"]],
        }
        e["primary_market_id"] = lr["anchor_market"]["market_id"]
        label = (labels[idx] if labels and idx < len(labels) else None) or deterministic_label(sample, underlying)
        e["question"] = label

    BUNDLE.write_text(json.dumps(b, default=str))
    print(f"patched {len(ladders)} LADDER events / {len(b['events'])} total "
          f"(labels: {'Haiku' if labels else 'deterministic'})")


if __name__ == "__main__":
    main()
