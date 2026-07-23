-- Fix 23 reconcileStatus misses, venue-confirmed 2026-07-23 (worklog entry same date).
-- H200 ladder KXH200Q-26JUN30: Kalshi finalized Jun 30/Jul 1, expiration_value 5.03
--   -> strikes <= 4.99 settled YES (1.0), strikes >= 5.19 settled NO (0.0)
-- KXTRUMPUFC-26JUL-DJT: Kalshi finalized Jul 12, result no (0.0)
-- Lebanon-recognize-Israel June 30 (0x274cec...): Gamma closed, umaStatus resolved, outcomePrices ["0","1"] -> NO

UPDATE markets SET status='resolved', last_price=1.0, reconciled_at=datetime('now')
WHERE platform='kalshi' AND platform_market_id IN (
 'KXH200Q-26JUN30-1.990','KXH200Q-26JUN30-2.190','KXH200Q-26JUN30-2.390','KXH200Q-26JUN30-2.590',
 'KXH200Q-26JUN30-2.790','KXH200Q-26JUN30-2.990','KXH200Q-26JUN30-3.190','KXH200Q-26JUN30-3.390',
 'KXH200Q-26JUN30-3.590','KXH200Q-26JUN30-3.790','KXH200Q-26JUN30-3.990','KXH200Q-26JUN30-4.190',
 'KXH200Q-26JUN30-4.390','KXH200Q-26JUN30-4.590','KXH200Q-26JUN30-4.790','KXH200Q-26JUN30-4.990');

UPDATE markets SET status='resolved', last_price=0.0, reconciled_at=datetime('now')
WHERE platform='kalshi' AND platform_market_id IN (
 'KXH200Q-26JUN30-5.190','KXH200Q-26JUN30-5.390','KXH200Q-26JUN30-5.590','KXH200Q-26JUN30-5.790',
 'KXTRUMPUFC-26JUL-DJT');

UPDATE markets SET status='resolved', last_price=0.0,
  close_at=COALESCE(close_at,'2026-06-30T23:59:59Z'),
  resolve_at=COALESCE(resolve_at,'2026-06-30T23:59:59Z'),
  reconciled_at=datetime('now')
WHERE platform='polymarket' AND platform_market_id='0x274cec202608757e62a0cf64ec63a3a814a6cc23a1bff1819b437362c5c16732';
