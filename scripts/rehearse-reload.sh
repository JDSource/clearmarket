#!/usr/bin/env bash
# Pre-reload gate: rehearse api/seed/{schema,seed}.sql against a throwaway sqlite file (D1 == SQLite
# semantics; `wrangler d1 execute --local` is unusable at this size — it parses the whole 133MB file in
# JS before committing anything). Proves: fresh load; an identical reload bumps nothing; cron-owned
# state survives; drifted descriptions are restored + flagged; absent open markets are delisted;
# resolved history is untouched; a delisted market that reappears is revived; the hourly cron's
# UPDATE shape still runs.
#
# Usage: ./scripts/rehearse-reload.sh [path.sqlite]   — run after `npm run export`, before `seed:remote`.
set -uo pipefail
cd "$(dirname "$0")/../api"
DB="${1:-/tmp/cm-reload-rehearsal.sqlite}"
rm -f "$DB"
q(){ sqlite3 -json "$DB" "$1"; }
stamp(){ python3 -c "import datetime;print(datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z'))"; }
load(){ sqlite3 "$DB" < seed/seed.sql || { echo "seed load FAILED"; exit 1; }; }

echo "== 0. schema =="; sqlite3 "$DB" < seed/schema.sql || { echo "schema FAILED"; exit 1; }
echo "== 1. first reload (fresh) =="; T0=$(stamp); sleep 1; time load
echo "events=$(q 'SELECT COUNT(*) c FROM events') markets=$(q 'SELECT COUNT(*) c FROM markets') delisted=$(q "SELECT COUNT(*) c FROM markets WHERE status='delisted'") vintage_null=$(q 'SELECT COUNT(*) c FROM markets WHERE bundle_vintage IS NULL') clock_null=$(q 'SELECT COUNT(*) c FROM markets WHERE row_changed_at IS NULL')"
echo "status mix: $(q 'SELECT status, COUNT(*) c FROM markets GROUP BY status')"
echo "/v1/status vintage (MAX events.updated_at): $(q 'SELECT MAX(updated_at) v FROM events')"

echo "== 2. second reload, same bundle (expect 0 clock bumps, counts unchanged) =="
sleep 1; T1=$(stamp); sleep 1; load
echo "markets=$(q 'SELECT COUNT(*) c FROM markets') bumped_after_T1=$(q "SELECT COUNT(*) c FROM markets WHERE row_changed_at > '$T1'")"

echo "== 3. simulate production state, then third reload =="
MID=$(sqlite3 "$DB" "SELECT market_id FROM markets WHERE status='open' ORDER BY market_id LIMIT 1")
MID2=$(sqlite3 "$DB" "SELECT market_id FROM markets WHERE status='open' ORDER BY market_id DESC LIMIT 1")
EID=$(sqlite3 "$DB" "SELECT event_id FROM events LIMIT 1")
echo "cron-resolved: $MID | drifted-description: $MID2 | ghost event: $EID"
sqlite3 "$DB" "UPDATE markets SET status='resolved', last_price=1.0, volume_24h_usd=12345, last_updated_at='2026-10-01T00:00:00Z', reconciled_at='2026-10-01T00:00:00Z', last_checked_at='2026-10-01T00:00:00Z', eligibility_screens='[{\"regime\":\"ciro-26-0076\",\"status\":\"PROD\"}]' WHERE market_id='$MID';
UPDATE markets SET question_raw='DRIFTED IN PROD', resolution_clarity_grade='Z' WHERE market_id='$MID2';
INSERT INTO markets (market_id,event_id,platform,status,question_raw,bundle_vintage) VALUES ('ghost-not-in-bundle','$EID','kalshi','open','ghost',NULL);
INSERT INTO markets (market_id,event_id,platform,status,question_raw,bundle_vintage) VALUES ('ghost-resolved-old','$EID','kalshi','resolved','old resolved ghost',NULL);
INSERT INTO resolution_log (market_id,event_id,platform,event_type,occurred_at,recorded_at,to_value,actor) VALUES ('$MID','$EID','kalshi','resolved','2026-10-01T00:00:00Z','2026-10-01','YES','clearmarket-kalshi-snapshot');"
sleep 1; T2=$(stamp); sleep 1; load
echo "-- cron-resolved market (expect: resolved, price 1.0, vol 12345, clocks + screens kept, bumped=0):"
q "SELECT status,last_price,volume_24h_usd,last_updated_at,reconciled_at,last_checked_at,eligibility_screens,(row_changed_at > '$T2') bumped FROM markets WHERE market_id='$MID'"
echo "-- drifted-description market (expect: question + grade restored from bundle, bumped=1):"
q "SELECT substr(question_raw,1,40) q, resolution_clarity_grade, (row_changed_at > '$T2') bumped FROM markets WHERE market_id='$MID2'"
echo "-- ghosts (expect: open ghost -> delisted + delisted_at + bumped=1; resolved ghost untouched, bumped=0):"
q "SELECT market_id,status,delisted_at,(row_changed_at > '$T2') bumped FROM markets WHERE market_id LIKE 'ghost-%'"
echo "-- total bumped after T2 (expect exactly 2):"
q "SELECT COUNT(*) c FROM markets WHERE row_changed_at > '$T2'"
echo "-- ledger untouched (expect 1 row, the cron's):"
q "SELECT COUNT(*) c, MAX(actor) actor FROM resolution_log"
echo "-- counts: markets=$(q 'SELECT COUNT(*) c FROM markets') delisted=$(q "SELECT COUNT(*) c FROM markets WHERE status='delisted'")"

echo "== 4. revive: a delisted market that reappears in the bundle (expect: status from bundle, delisted_at NULL, bumped=1) =="
sqlite3 "$DB" "UPDATE markets SET status='delisted', delisted_at='x' WHERE market_id='$MID2'"
sleep 1; T3=$(stamp); sleep 1; load
q "SELECT status, delisted_at, (row_changed_at > '$T3') bumped FROM markets WHERE market_id='$MID2'"
echo "== 5. hourly-cron UPDATE shape against the reloaded table (expect no error) =="
sqlite3 "$DB" "UPDATE markets SET last_price=0.5, last_updated_at='2026-10-09T00:00:00Z', last_checked_at='2026-10-09T00:00:00Z', row_changed_at='2026-10-09T00:00:00Z' WHERE market_id='$MID2'" && echo "cron-shaped UPDATE OK"
echo "== done =="
