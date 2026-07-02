#!/usr/bin/env bash
# Date-review queue — surfaces temporally-suspect markets the enrichment auto-fixes did NOT catch
# (residual stale-year questions, missing settlement dates, un-reconciled ladder dates).
# Low-noise by design; safe to run on a cadence. Read-only.
#
# Usage: ./scripts/date-review.sh [bundle.json]   (default: web/data/universe-enriched-linked.json)
# Cron/periodic: exits 1 when the queue is non-empty, so a wrapper can alert only when there's work.
set -euo pipefail
cd "$(dirname "$0")/.."

BUNDLE="${1:-}"
python3 report_date_review.py ${BUNDLE:+"$BUNDLE"}
