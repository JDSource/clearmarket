#!/usr/bin/env bash
# Daily driver for the crawler-history archive: snapshots every not-yet-recorded day within the
# 8-day zone-analytics retention window (self-healing — if the machine was off or a run was missed,
# the next run backfills the gap, as long as no more than ~8 days elapse). Idempotent per day.
# Wire this to launchd/cron (see com.clearmarket.crawler-snapshot.plist).
set -uo pipefail
DIR="$(dirname "$0")"
# Refresh the wrangler OAuth token BEFORE the snapshot scripts grep it out of the config file.
# The token expires between daily runs; a headless `whoami` makes wrangler refresh it in place.
# (Both archive outages — Jul 6-12 and Jul 15-19 — were this exact staleness.) Setting a scoped
# CLOUDFLARE_ZONE_TOKEN in the plist env skips the OAuth path entirely and is the gold fix.
export PATH="/usr/local/opt/node@22/bin:$PATH"
if [ -z "${CLOUDFLARE_ZONE_TOKEN:-}" ]; then
  npx -y wrangler@latest whoami >/dev/null 2>&1 || echo "warn: wrangler OAuth refresh failed ($(date -u +%FT%TZ)); snapshots may auth-fail"
fi
# Snapshot the last 7 complete UTC days (today-7 .. yesterday). Recorded days are skipped cheaply.
for i in 7 6 5 4 3 2 1; do
  d="$(python3 -c "import datetime;print((datetime.datetime.utcnow()-datetime.timedelta(days=$i)).strftime('%Y-%m-%d'))")"
  "$DIR/cf-crawlers-snapshot.sh" "$d"   # zone AI/agent layer (8-day retention — must archive)
  "$DIR/rum-snapshot.sh" "$d"           # human RUM layer (CF keeps it, but we keep our own copy too)
done
