-- marks_daily: end-of-day price/volume time-series (2026-05-29 build).
-- Non-destructive. Creates the table and seeds today's baseline snapshot from the live
-- markets table (linked + primary set, the ones the hourly cron keeps fresh). Real
-- day-over-day begins at the next EOD cron capture.
CREATE TABLE IF NOT EXISTS marks_daily (
  market_id TEXT NOT NULL,
  day TEXT NOT NULL,
  last_price REAL,
  volume_24h_usd REAL,
  volume_total_usd REAL,
  captured_at TEXT,
  PRIMARY KEY (market_id, day)
);
CREATE INDEX IF NOT EXISTS idx_marks_daily_mkt ON marks_daily(market_id);

INSERT INTO marks_daily (market_id, day, last_price, volume_24h_usd, volume_total_usd, captured_at)
SELECT market_id, '2026-05-29', last_price, volume_24h_usd, volume_total_usd, '2026-05-29T00:00:00Z'
  FROM markets
 WHERE last_price IS NOT NULL
   AND (question_id IS NOT NULL
        OR market_id IN (SELECT primary_market_id FROM events WHERE primary_market_id IS NOT NULL))
ON CONFLICT(market_id, day) DO UPDATE SET
  last_price = excluded.last_price,
  volume_24h_usd = excluded.volume_24h_usd,
  volume_total_usd = excluded.volume_total_usd,
  captured_at = excluded.captured_at;
