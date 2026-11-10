-- D1 read-path indexes (applied to production 2026-11-10 02:25Z; idempotent).
--
-- Cause of the Nov 3-6, 2026 "D1_ERROR: D1 DB is overloaded" 500s on /v1/status and /v1/marks:
--  1. marks_daily (PK market_id, day; 1.6M rows) had no index on `day`, so the /v1/status latest-day
--     aggregate scanned the table twice per call (3.2M rows read, 1.7-5 s). Every Worker reader of this
--     table looks up by day. Build on prod: 2.6 s, +32 MB.
--  2. /v1/marks orders on COALESCE(row_changed_at,'') for keyset pagination; idx_markets_row_changed
--     (plain column) cannot serve an expression, so every page was a full scan + temp sort. The
--     expression index below is matched textually: keep CHANGED_EXPR in api/src/index.ts identical.
--     Build on prod: 0.8 s.
-- Undo: DROP INDEX idx_marks_daily_day; DROP INDEX idx_markets_changed_mkt;
CREATE INDEX IF NOT EXISTS idx_marks_daily_day ON marks_daily(day, carried_forward);
CREATE INDEX IF NOT EXISTS idx_markets_changed_mkt ON markets(COALESCE(row_changed_at,''), market_id);
