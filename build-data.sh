#!/usr/bin/env bash
# CM data build pipeline — run before any deploy so every surface (event pages, D1/API)
# serves coherent, ladder-patched data. Order matters: patch the bundle FIRST, then
# regenerate the D1 seed and the static site from the patched bundle.
#
#   ./build-data.sh            # patch + export seed + build site (local)
#   ./build-data.sh --no-llm   # skip the Haiku label pass (deterministic labels)
set -euo pipefail
cd "$(dirname "$0")"
export PATH="/usr/local/opt/node@22/bin:$PATH"

echo "[1/3] patch_ladders — reconstruct strike ladders into the bundle"
python3 patch_ladders.py "${1:-}"

echo "[2/3] export D1 seed from the patched bundle"
( cd api && npm run export )

echo "[3/3] build the static site from the patched bundle"
( cd web && npm run build )

cat <<'NEXT'

Build complete. To deploy (when the domain is live + hold-the-push is lifted):
  - API/D1:  cd api && npm run seed:remote   (fresh reseed)  OR  python3 migrate_d1_ladders.py + wrangler d1 execute (incremental)
  - Worker:  cd api && npx wrangler deploy
  - Site:    cd web && npx wrangler pages deploy dist
NEXT
