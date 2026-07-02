#!/usr/bin/env bash
# CM data build pipeline — run before any deploy so every surface (event pages, D1/API)
# serves coherent data. Order matters: sanitize + patch the bundle FIRST, then
# regenerate the D1 seed and the static site from the cleaned bundle.
#
#   ./build-data.sh            # fix + patch + canon + export seed + build site (local)
#   ./build-data.sh --no-llm   # skip the Haiku label pass (deterministic labels)
#
# RUNS ON A FRESH enriched+linked bundle (output of enrich_universe.py + unify_events.py +
# canon_extract.py). Source commitment + the RCG grade are now decided at ENRICH time (LLM
# classification, folded into grade_market) — there is no build-time source re-cap. patch_ladders
# still mutates the bundle, so rebuild from the fresh enriched bundle, not a patched one.
set -euo pipefail
cd "$(dirname "$0")"
export PATH="/usr/local/opt/node@22/bin:$PATH"

echo "[1/6] fix_questions — replace LLM-garbage/placeholder questions with the raw venue question"
python3 fix_questions.py

echo "[2/6] retitle_multidate_events — generalize titles of multi-date series (no single-leg dates)"
python3 retitle_multidate_events.py

echo "[3/6] patch_ladders — reconstruct strike ladders into the bundle"
python3 patch_ladders.py "${1:-}"

echo "[4/6] merge_canon — stamp canonical cross-venue claim_sigs + emit canon-pairs.json (needs canon-registry.json)"
python3 merge_canon.py

echo "[*] date-review — surface residual temporally-suspect markets on the CLEANED bundle (post fix_questions/patch_ladders; informational, never blocks)"
python3 report_date_review.py || true   # exits 1 when non-empty; must run AFTER fix_questions so the queue reflects post-fix state

echo "[5/6] export D1 seed from the cleaned + patched bundle"
( cd api && npm run export )

echo "[6/6] build the static site from the cleaned + patched bundle"
( cd web && npm run build )

cat <<'NEXT'

Build complete. To deploy (when the domain is live + hold-the-push is lifted):
  - API/D1:  cd api && npm run seed:remote   (fresh reseed)  OR  python3 migrate_d1_ladders.py + wrangler d1 execute (incremental)
  - Worker:  cd api && npx wrangler deploy
  - Site:    cd web && npx wrangler pages deploy dist
NEXT
