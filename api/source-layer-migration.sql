-- Source-layer refactor (2026-07-03): canonical full source list + stamped source judgment.
-- ALTER-only (no reseed required); values populate on the next re-enrich + seed.
-- Run BEFORE deploying the worker that serves these columns (migrate-before-deploy rule).
--   wrangler d1 execute clearmarket --remote --file=api/source-layer-migration.sql
ALTER TABLE markets ADD COLUMN resolution_source_list TEXT;  -- JSON [{name,url,provenance}] — full venue-listed + prose-surfaced sources
ALTER TABLE markets ADD COLUMN source_status TEXT;           -- stamped at enrich: platform_named | no_committed_source | no_source_stated
ALTER TABLE markets ADD COLUMN source_mechanism TEXT;        -- single_authority | precedence | quorum (how multiple sources bind)
