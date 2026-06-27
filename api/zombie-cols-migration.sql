-- Zombie-fix columns on the LIVE tables (run ONCE before deploying the Worker that writes them;
-- the generated seed/schema.sql includes these columns going forward, so a full reseed does not need this).
--   cd api && wrangler d1 execute clearmarket --remote --file=zombie-cols-migration.sql   (run from api/)
-- SQLite ADD COLUMN has no IF NOT EXISTS — this is one-time and errors harmlessly ("duplicate column
-- name") if re-run on a DB that already has them.
--
-- markets.last_updated_at : ISO, stamped by the hourly marks cron on every price write.
-- markets.reconciled_at   : ISO, stamped by the daily reconcileStatus cron when it venue-confirms status.
-- resolution_log.from_value : prior state (e.g. 'open') for the status transition; NULL on legacy rows.
ALTER TABLE markets ADD COLUMN last_updated_at TEXT;
ALTER TABLE markets ADD COLUMN reconciled_at TEXT;
ALTER TABLE resolution_log ADD COLUMN from_value TEXT;
