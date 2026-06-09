"""
Deadline-aligned cross-venue spreads (the trustworthy spread layer).

A question_id groups a deadline ladder as ONE claim ("same question"), but a spread is only
meaningful between the SAME deadline. This pairs Kalshi<->Poly markets WITHIN a claim by
nearest deadline (<=TOL days), polarity-normalizes (a 'below' market -> P(at-or-above)),
and computes the spread per aligned pair. Uses the latest marks from marks.jsonl.

Output is the spot-check table: the two matched markets, their deadlines + probabilities,
and the spread. No LLM.
"""
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
TOL = 7  # STRICT: two markets are the "same deadline" only within a week

# GATE: spreads only on threshold-bearing markets (clean structured data). Occurrence/binary
# pairs ship as LINKS (raw prices), never an editorialized spread — precision over recall.
linked = [m for m in json.loads((ROOT / "_clearmarket_linked.json").read_text())["markets"]
          if m.get("question_id") and m.get("threshold") is not None]

# latest mark per native_id
latest = {}
for line in (ROOT / "marks.jsonl").read_text().splitlines():
    r = json.loads(line)
    if r["native_id"] not in latest or r["snapshot_at"] > latest[r["native_id"]]["snapshot_at"]:
        latest[r["native_id"]] = r

def parse_d(w):
    try: return date.fromisoformat((w or "")[:10])
    except ValueError: return None

def norm(m, price):
    return (1.0 - price) if m.get("direction") == "below" else price

groups = defaultdict(lambda: {"kalshi": [], "polymarket": []})
for m in linked:
    mk = latest.get(m["native_id"])
    if mk and mk.get("last_price") is not None:
        groups[m["question_id"]][m["venue"]].append({**m, "price": mk["last_price"], "d": parse_d(m.get("window"))})

pairs, seen = [], set()
for sig, g in groups.items():
    for k in g["kalshi"]:
        if k["d"] is None: continue
        cand = [(abs((k["d"] - p["d"]).days), p) for p in g["polymarket"]
                if p["d"] and p.get("threshold") == k.get("threshold")]
        if not cand: continue
        dist, p = min(cand, key=lambda x: x[0])
        if dist > TOL: continue
        key = (k["native_id"], p["native_id"])
        if key in seen: continue
        seen.add(key)
        kn, pn = norm(k, k["price"]), norm(p, p["price"])
        pairs.append({"subject": k["subject"], "style": k["settlement_style"], "threshold": k.get("threshold"),
                      "spread": round(abs(kn - pn), 3), "gap_days": dist,
                      "k_q": k["raw_q"], "k_d": str(k["d"]), "k_prob": round(kn, 3),
                      "p_q": p["raw_q"], "p_d": str(p["d"]), "p_prob": round(pn, 3)})

mat = [x for x in pairs if x["spread"] >= 0.05]
print(f"deadline-aligned cross-venue pairs (<= {TOL}d apart): {len(pairs)}  |  material (>=5pp): {len(mat)}\n")

print("=== DIVERGENCES (aligned, sorted by spread) ===")
for s in sorted(pairs, key=lambda x: -x["spread"])[:18]:
    thr = f" @{s['threshold']}" if s["threshold"] is not None else ""
    print(f"\n  Δ {s['spread']*100:4.0f}pp   [{s['style']}] {s['subject']!r}{thr}   (deadlines {s['k_d']} ~ {s['p_d']}, {s['gap_days']}d apart)")
    print(f"     Kalshi  {s['k_prob']*100:3.0f}%   {s['k_q'][:58]!r}")
    print(f"     Poly    {s['p_prob']*100:3.0f}%   {s['p_q'][:58]!r}")

print("\n=== AGREEMENT (smallest spreads — sanity that aligned markets track) ===")
for s in sorted(pairs, key=lambda x: x["spread"])[:6]:
    print(f"  Δ{s['spread']*100:3.0f}pp  {s['subject']!r}  K {s['k_prob']*100:.0f}% / P {s['p_prob']*100:.0f}%  "
          f"({s['k_q'][:30]!r} ~ {s['p_q'][:30]!r})")

(ROOT / "_clearmarket_spreads_aligned.json").write_text(json.dumps(pairs, indent=2, default=str))
print(f"\nSaved -> _clearmarket_spreads_aligned.json ({len(pairs)} pairs)")
