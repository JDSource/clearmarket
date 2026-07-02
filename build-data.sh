#!/usr/bin/env bash
# CM data build pipeline — run before any deploy so every surface (event pages, D1/API)
# serves coherent data. Order matters: sanitize + patch the bundle FIRST, then
# regenerate the D1 seed and the static site from the cleaned bundle.
#
#   ./build-data.sh            # fix + patch + canon + export seed + build site (local)
#   ./build-data.sh --no-llm   # skip the Haiku label pass (deterministic labels)
#
# RUNS ON A FRESH enriched+linked bundle (output of enrich_universe.py [fixed source_conflict prompt
# lives in enhance.py] + unify_events.py + canon_extract.py). The patch steps are NOT idempotent —
# patch_sources nulls hedge sources, so re-running on an already-patched bundle mis-reclassifies.
# Rebuild from the fresh enriched bundle, never from a patched one.
set -euo pipefail
cd "$(dirname "$0")"
export PATH="/usr/local/opt/node@22/bin:$PATH"

echo "[1/7] fix_questions — replace LLM-garbage/placeholder questions with the raw venue question"
python3 fix_questions.py

echo "[2/7] retitle_multidate_events — generalize titles of multi-date series (no single-leg dates)"
python3 retitle_multidate_events.py

echo "[3/7] patch_ladders — reconstruct strike ladders into the bundle"
python3 patch_ladders.py "${1:-}"

echo "[4/7] patch_sources — classify source commitment + cap hedged/placeholder grades"
python3 patch_sources.py --write

echo "[5/7] merge_canon — stamp canonical cross-venue claim_sigs + emit canon-pairs.json (needs canon-registry.json)"
python3 merge_canon.py

echo "[*] date-review — surface residual temporally-suspect markets on the CLEANED bundle (post fix_questions/patch_ladders; informational, never blocks)"
python3 report_date_review.py || true   # exits 1 when non-empty; must run AFTER fix_questions so the queue reflects post-fix state

echo "[6/7] export D1 seed from the cleaned + patched bundle"
( cd api && npm run export )

echo "[7/7] build the static site from the cleaned + patched bundle"
( cd web && npm run build )

cat <<'NEXT'

Build complete. To deploy (when the domain is live + hold-the-push is lifted):
  - API/D1:  cd api && npm run seed:remote   (fresh reseed)  OR  python3 migrate_d1_ladders.py + wrangler d1 execute (incremental)
  - Worker:  cd api && npx wrangler deploy
  - Site:    cd web && npx wrangler pages deploy dist
NEXT
