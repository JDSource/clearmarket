-- Eligibility screens column on the LIVE markets table (run once before the next
-- full reseed; the generated seed/schema.sql includes the column going forward).
--   wrangler d1 execute clearmarket --remote --file=api/eligibility-migration.sql
-- Populated by api/scripts/export-d1.mjs from web/data/eligibility-ciro-26-0076.json.
-- Shape: JSON [{regime, screen_version, status, reasons, bucket, screened_at}].
-- Rule-set fit (eligible / review / not_eligible), NOT market quality.
ALTER TABLE markets ADD COLUMN eligibility_screens TEXT;
