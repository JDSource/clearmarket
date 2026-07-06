-- Event/child resolution-fix columns on the LIVE tables (run ONCE before an incremental deploy;
-- the generated seed/schema.sql already includes these going forward, so a full reseed does NOT need this).
--   cd api && wrangler d1 execute clearmarket --remote --file=event-child-cols-migration.sql   (run from api/)
-- SQLite ADD COLUMN has no IF NOT EXISTS — this is one-time and errors harmlessly ("duplicate column
-- name") if re-run on a DB that already has them.
--
-- events.bundle_type          : categorical|date_ladder|strike_ladder|augmented_negrisk|singleton
-- events.resolution_reference : generic subject-free event-level resolution ontology (OCC class-level rule)
-- markets.group_item_title    : per-child subject (the OSI-symbol analog; composes underlying_reference)
ALTER TABLE events ADD COLUMN bundle_type TEXT;
ALTER TABLE events ADD COLUMN resolution_reference TEXT;
ALTER TABLE events ADD COLUMN rcg_factors TEXT;          -- JSON: 5 LLM factor ratings + "why" (audit)
ALTER TABLE markets ADD COLUMN group_item_title TEXT;
ALTER TABLE markets ADD COLUMN source_of_record TEXT;    -- committed authority the LLM named
ALTER TABLE markets ADD COLUMN rcg TEXT;                 -- JSON per-factor audit breakdown
