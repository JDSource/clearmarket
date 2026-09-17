-- Freshness / integrity columns on the LIVE tables (2026-09-17). Run ONCE before deploying the Worker
-- that writes them:   cd api && wrangler d1 execute clearmarket --remote --file=freshness-migration.sql
-- SQLite ADD COLUMN has no IF NOT EXISTS: re-running errors harmlessly ("duplicate column name").
-- seed/schema.sql carries the same columns/tables, so a full reseed does not need this file.
--
-- markets.last_checked_at   : ISO; stamped by the hourly marks cron for EVERY market seen in a venue's live
--                             feed that run, changed or not (second clock; NULL = not seen since reload).
-- marks_daily.price_as_of   : ISO; the market's last_updated_at at snapshot time (when the price last changed).
-- marks_daily.carried_forward: 1 when the market was not seen in any live feed in the 24h before the snapshot.
-- cron_runs                 : one row per cron step per run — the run ledger /v1/status reports.
-- feed_meta                 : small key/value store for pipeline metadata (sweep/screen run dates, versions).
ALTER TABLE markets ADD COLUMN last_checked_at TEXT;
ALTER TABLE marks_daily ADD COLUMN price_as_of TEXT;
ALTER TABLE marks_daily ADD COLUMN carried_forward INTEGER;
CREATE INDEX IF NOT EXISTS idx_markets_last_updated ON markets(last_updated_at);
CREATE INDEX IF NOT EXISTS idx_markets_last_checked ON markets(last_checked_at);
CREATE INDEX IF NOT EXISTS idx_markets_reconciled ON markets(reconciled_at);
CREATE TABLE IF NOT EXISTS cron_runs (
  run_id TEXT NOT NULL,
  step TEXT NOT NULL,
  venue TEXT NOT NULL DEFAULT '',
  started_at TEXT,
  finished_at TEXT,
  fetched INTEGER,
  changed INTEGER,
  error TEXT,
  PRIMARY KEY (run_id, step, venue)
);
CREATE INDEX IF NOT EXISTS idx_cron_runs_step ON cron_runs(step, started_at);
CREATE TABLE IF NOT EXISTS feed_meta (
  key TEXT PRIMARY KEY,
  value TEXT,
  updated_at TEXT
);
