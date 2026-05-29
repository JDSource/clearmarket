"""
Compute cross_venue_spread per claim (#4 — closes the loop on the spread layer).

For each claim_sig spanning both venues, normalize polarity (a 'below' market -> P(at-or-above)
= 1 - price) so prices are comparable, then spread = |kalshi_prob - polymarket_prob|. This is
the deterministic CM number CM Signal reads to detect divergence.

v1 caveat: multi-deadline touch ladders use a representative (first priced) market per venue —
true comparison aligns by deadline (refinement). No LLM. Reads _clearmarket_linked.json.
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
markets = json.loads((ROOT / "_clearmarket_linked.json").read_text())["markets"]

def norm(m):
    p = m.get("price")
    if p is None:
        return None
    return (1.0 - p) if m.get("direction") == "below" else p

groups = defaultdict(lambda: {"kalshi": [], "polymarket": []})
for m in markets:
    if m.get("claim_sig"):
        groups[m["claim_sig"]][m["venue"]].append(m)

spreads = []
for sig, g in groups.items():
    kp = next((norm(m) for m in g["kalshi"] if norm(m) is not None), None)
    pp = next((norm(m) for m in g["polymarket"] if norm(m) is not None), None)
    if kp is None or pp is None:
        continue
    k0, p0 = g["kalshi"][0], g["polymarket"][0]
    spreads.append({"sig": sig, "subject": k0["subject"], "style": k0["settlement_style"],
                    "threshold": k0.get("threshold"), "kalshi_prob": round(kp, 3),
                    "polymarket_prob": round(pp, 3), "spread": round(abs(kp - pp), 3),
                    "k": k0["raw_q"], "p": p0["raw_q"]})

print(f"claims with a computable spread (both venues priced): {len(spreads)} / {len(groups)}")
mat = [s for s in spreads if s["spread"] >= 0.05]
print(f"material divergences (>=5pp): {len(mat)}\n")
print("--- top 15 cross-venue divergences ---")
for s in sorted(spreads, key=lambda x: -x["spread"])[:15]:
    thr = f" @{s['threshold']}" if s["threshold"] is not None else ""
    print(f"  Δ{s['spread']*100:4.0f}pp  K {s['kalshi_prob']*100:3.0f}% / P {s['polymarket_prob']*100:3.0f}%  "
          f"[{s['style']}] {s['subject']!r}{thr}")
    print(f"          K: {s['k'][:52]!r}  P: {s['p'][:52]!r}")

(ROOT / "_clearmarket_spreads.json").write_text(json.dumps(spreads, indent=2, default=str))
print("\nSaved -> _clearmarket_spreads.json")
