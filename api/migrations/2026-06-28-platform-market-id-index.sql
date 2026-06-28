-- Index platform_market_id so get_market's venue-native id / ticker lookup is a point-query,
-- not a full table scan. Apply to the LIVE D1 at deploy (the index is already in seed/schema.sql
-- for fresh seeds, but the production DB is already seeded, so it needs this one ALTER-style add):
--
--   wrangler d1 execute clearmarket --remote \
--     --file=api/migrations/2026-06-28-platform-market-id-index.sql
--
-- IF NOT EXISTS makes it safe to run more than once.
CREATE INDEX IF NOT EXISTS idx_markets_platform_mkt ON markets(platform_market_id);
