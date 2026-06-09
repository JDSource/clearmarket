"""
Fold the unified layer (structured fields + question_id + tags) onto the RCG-enriched bundle (#4b).

The enriched bundle (web/data/universe-enriched-full.json) has RCG grades + resolution fields
but the mangled native fields. _clearmarket_linked.json has the clean structured fields +
question_id + tags keyed by native_id (= platform_market_id). Join on platform_market_id.

Writes a NEW file (universe-enriched-linked.json) — does NOT overwrite the live bundle
(hold-the-push; review before the API consumes it). Deterministic, no LLM.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
bundle = json.loads((ROOT / "web/data/universe-enriched-full.json").read_text())
linked = json.loads((ROOT / "_clearmarket_linked.json").read_text())["markets"]

fields_by_pmid = {}
for m in linked:
    fields_by_pmid[m["native_id"]] = {
        "settlement_style": m.get("settlement_style"),
        "direction": m.get("direction"),
        "threshold": m.get("threshold"),
        "question_id": m.get("question_id"),
        "tags": m.get("tags"),
    }

matched = 0
for m in bundle.get("markets", []):
    f = fields_by_pmid.get(m.get("platform_market_id"))
    if f:
        matched += 1
        m.update(f)

mkts = bundle.get("markets", [])
linked_ct = sum(1 for m in mkts if m.get("question_id"))
tagged = sum(1 for m in mkts if m.get("tags"))
print(f"bundle markets: {len(mkts)}  |  matched + enriched: {matched} ({matched*100//max(len(mkts),1)}%)")
print(f"  with question_id: {linked_ct}  |  with tags: {tagged}")

(ROOT / "web/data/universe-enriched-linked.json").write_text(json.dumps(bundle, default=str))
print("Saved -> web/data/universe-enriched-linked.json")
