#!/usr/bin/env bash
# reconcile-bundle.sh — the step that used to get forgotten.
#
# After a monthly re-enrich (pull -> enrich -> unify -> link), the linked bundle still carries
# prior-vintage markets VERBATIM (union_vintages keeps settled history per locked decision #4), so a
# chunk of them read status='open' with prices frozen at the old vintage even though the venue settled
# or delisted them — the "zombie" markets. This codifies the two reconciliation steps in the order
# settle_status_sweep.py's docstring requires, so they can't be skipped:
#
#   1. settle_status_sweep.py  — query each carried market's venue, set resolved/closed + true price
#   2. build_resolution_log.py — capture the history table FROM the now-authoritative status
#
# Run AFTER unify/link, BEFORE build-data.sh (which exports the D1 seed + builds the site).
# Kept separate from build-data.sh on purpose: the sweep makes thousands of venue calls (~10 min),
# so a plain site rebuild shouldn't trigger it.
#
#   ./reconcile-bundle.sh            # apply (writes the linked bundle + resolution-log.json)
#   ./reconcile-bundle.sh --dry-run  # sweep in dry-run (no write), still rebuilds the log preview
set -euo pipefail
cd "$(dirname "$0")"
export PATH="/usr/local/opt/node@22/bin:$PATH"

LINKED="web/data/universe-enriched-linked.json"
FRESH="web/data/universe-enriched-full.json"
SWEEP_FLAG="--write"
[ "${1:-}" = "--dry-run" ] && SWEEP_FLAG=""

test -s "$LINKED" || { echo "ERROR: $LINKED missing — run unify/link first"; exit 1; }
test -s "$FRESH"  || { echo "ERROR: $FRESH missing — the sweep needs the fresh -full bundle to find carried markets"; exit 1; }

echo "[1/2] settle_status_sweep — reconcile carried markets against their venue (${SWEEP_FLAG:-dry-run})"
python3 scripts/settle_status_sweep.py $SWEEP_FLAG

echo "[2/2] build_resolution_log — capture history from the reconciled status"
python3 build_resolution_log.py

echo "reconcile-bundle DONE — now run ./build-data.sh to export the D1 seed + build the site."
