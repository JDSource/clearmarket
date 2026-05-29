"""
Consolidate cross-venue links: stamp claim_sig onto every market (#4a).

Combines the two linkers:
  - threshold links  -> _unify_all.json "links" (members carry native_id)
  - occurrence links -> _unify_occurrence_links.json (keyed by event_native + subject)

Output: _clearmarket_linked.json — the unified markets with claim_sig populated, ready to
feed enrich_universe.py / the API. Deterministic, no LLM.
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
uni = json.loads((ROOT / "_unify_all.json").read_text())
markets = uni["markets"]
thr_links = uni.get("links", [])
occ_links = json.loads((ROOT / "_unify_occurrence_links.json").read_text())

# threshold: native_id -> sig
sig_by_native = {}
for L in thr_links:
    for m in L["members"]:
        sig_by_native[m["native_id"]] = L["sig"]

# occurrence: (venue, event_native, subject) -> sig
sig_by_evsubj = {}
for L in occ_links:
    sig_by_evsubj[("kalshi", L["kalshi_event"], L["subject"])] = L["sig"]
    for p in L["poly"]:
        sig_by_evsubj[("polymarket", p["event"], L["subject"])] = L["sig"]

src = Counter()
for m in markets:
    sig = sig_by_native.get(m["native_id"])
    if sig:
        src["threshold"] += 1
    else:
        sig = sig_by_evsubj.get((m["venue"], m["event_native"], m["subject"]))
        if sig:
            src["occurrence"] += 1
    m["claim_sig"] = sig

linked = sum(1 for m in markets if m.get("claim_sig"))
sigs = {m["claim_sig"] for m in markets if m.get("claim_sig")}
print(f"markets: {len(markets)}  |  with claim_sig: {linked}  ({src['threshold']} threshold / {src['occurrence']} occurrence)")
print(f"distinct claim_sigs (cross-venue claims): {len(sigs)}")

# coverage by claim_sig group: venues present
by_sig = {}
for m in markets:
    if m.get("claim_sig"):
        by_sig.setdefault(m["claim_sig"], set()).add(m["venue"])
both = sum(1 for v in by_sig.values() if len(v) > 1)
print(f"claim groups spanning BOTH venues: {both} / {len(by_sig)}")

(ROOT / "_clearmarket_linked.json").write_text(json.dumps({"markets": markets}, indent=2, default=str))
print("Saved -> _clearmarket_linked.json")
