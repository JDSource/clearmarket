-- Commit clock (2026-09-18). Run ONCE before deploying the Worker that writes it:
--   cd api && wrangler d1 execute clearmarket --remote --file=commit-clock-migration.sql
-- markets.row_changed_at : ISO, the Worker's own write time whenever price/volume, status or eligibility
--   screen changes on the row. /v1/marks?since= and its cursor key on THIS column. price_as_of and
--   last_checked_at stay observation clocks (a Kalshi row from the R2 snapshot carries the snapshot's time,
--   which can trail the commit by up to 180 min — keying since= on it silently dropped changes).
ALTER TABLE markets ADD COLUMN row_changed_at TEXT;
CREATE INDEX IF NOT EXISTS idx_markets_row_changed ON markets(row_changed_at);
-- Backfill from the old expression so existing rows keep their position in the incremental stream.
UPDATE markets SET row_changed_at = NULLIF(MAX(COALESCE(last_updated_at,''), COALESCE(reconciled_at,'')), '') WHERE row_changed_at IS NULL;
-- Repair rows where an older snapshot stamp moved the check clock behind the price clock.
UPDATE markets SET last_checked_at = last_updated_at WHERE last_checked_at IS NOT NULL AND last_updated_at IS NOT NULL AND last_checked_at < last_updated_at;
