#!/usr/bin/env bash
# run_unify_all.sh — the missing glue step.
# unify_events.py emits one _unify_<category>.json per category; nothing writes the
# combined _unify_all.json that link_occurrence.py + apply_claim_sigs.py read.
# This runs all 9 CATEGORIES_IN, then concatenates markets + links into _unify_all.json.
# Each event belongs to exactly one category (first-match priority), so the union is the
# full universe with no dups; native_id dedup is a belt-and-suspenders guard.
set -euo pipefail
cd "$(dirname "$0")"
export PATH="/usr/local/opt/node@22/bin:$PATH"

CATS="economics financials crypto companies technology health politics geopolitics climate"
for cat in $CATS; do
  echo "=== unify: $cat ==="
  caffeinate -i python3 unify_events.py "$cat"
done

echo "=== assemble _unify_all.json ==="
python3 - <<'PY'
import json
from pathlib import Path
cats = "economics financials crypto companies technology health politics geopolitics climate".split()
markets, links, seen = [], [], set()
for c in cats:
    p = Path(f"_unify_{c}.json")
    if not p.exists():
        print(f"  WARN: _unify_{c}.json missing"); continue
    d = json.loads(p.read_text())
    for m in d.get("markets", []):
        nid = m.get("native_id")
        if nid in seen:
            continue
        seen.add(nid); markets.append(m)
    links += d.get("links", [])
Path("_unify_all.json").write_text(json.dumps({"markets": markets, "links": links}, indent=2, default=str))
print(f"assembled _unify_all.json: {len(markets)} markets, {len(links)} links")
PY
echo "=== UNIFY STAGE COMPLETE ==="
