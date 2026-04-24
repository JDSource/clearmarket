-- ClearMarket v0.1.0 — Postgres DDL
-- Generated from JSON Schema files in outputs/clearmarket/schema/
-- Last updated: 2026-04-23 (Pattern 3 — flat events + tag-based grouping)
--
-- Target: Supabase / Postgres 15+
-- Extensions required: none in v0.1 (pgvector deferred to v0.2+)
--
-- Order: events → markets (FK to events) → marks (FK to markets) → resolution_log (FK to markets)

BEGIN;

-- =============================================================
-- 1. EVENTS — canonical tradable question, editorial layer
-- =============================================================
CREATE TABLE events (
    event_id                CHAR(12) PRIMARY KEY
                            CHECK (event_id ~ '^CM[0-9A-Z]{10}$'),
    slug                    TEXT NOT NULL,
    question                TEXT NOT NULL,
    category                TEXT NOT NULL
                            CHECK (category IN ('macro','geopolitics','politics','crypto','sports')),
    tags                    TEXT[] NOT NULL DEFAULT '{}',

    -- Headline market (nullable until first market linked)
    primary_market_id       BIGINT,
    primary_market_locked   BOOLEAN NOT NULL DEFAULT FALSE,

    -- Timing (resolution dates live on markets, not here)
    catalyst_dates          JSONB NOT NULL DEFAULT '[]'::jsonb,

    -- Governance
    published               BOOLEAN NOT NULL DEFAULT FALSE,
    editorial_notes         TEXT,  -- public-facing per Apr 23 decision

    -- Provenance
    field_provenance        JSONB NOT NULL DEFAULT '{}'::jsonb,

    -- Plumbing
    created_at              TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX events_slug_idx ON events (slug);
CREATE INDEX events_category_idx   ON events (category);
CREATE INDEX events_tags_gin_idx   ON events USING GIN (tags);
CREATE INDEX events_published_idx  ON events (published) WHERE published = TRUE;

COMMENT ON TABLE events IS
  'Canonical tradable question. Editorial layer on top of platform markets. '
  'Every event has >=1 market linked. Thematic grouping via tags, not hierarchy.';
COMMENT ON COLUMN events.event_id IS
  'ClearMarket canonical ID. Format: CM + 9-char vowel-free base36 + 1-char mod-10 check. Stable forever.';
COMMENT ON COLUMN events.tags IS
  'Cross-cutting filter + theme tags. Family grouping: lowercase-hyphenated (iran-conflict, fed-rate-decisions).';
COMMENT ON COLUMN events.editorial_notes IS
  'Public-facing editorial context. Surfaced in API responses. The editorial layer platforms do not ship.';


-- =============================================================
-- 2. MARKETS — per-platform contracts + editorial fill
-- =============================================================
CREATE TABLE markets (
    market_id               BIGSERIAL PRIMARY KEY,
    platform                TEXT NOT NULL
                            CHECK (platform IN ('kalshi','polymarket')),
    platform_market_id      TEXT NOT NULL,

    -- Linking to ClearMarket event (nullable — not every market earns an event)
    event_id                CHAR(12) REFERENCES events(event_id) ON DELETE SET NULL,
    platform_event_id       TEXT,

    -- Raw platform data
    question_raw            TEXT,
    description_raw         TEXT,
    category_raw            TEXT,

    -- Contract specs
    contract_type           TEXT NOT NULL
                            CHECK (contract_type IN ('binary','scalar')),
    settlement_currency     TEXT NOT NULL
                            CHECK (settlement_currency IN ('USD','USDC')),
    tick_size               NUMERIC,
    contract_multiplier     NUMERIC,
    underlying_reference    TEXT,  -- editorial

    -- Timing + lifecycle
    close_at                TIMESTAMPTZ,
    last_trading_date       TIMESTAMPTZ,
    resolve_at              TIMESTAMPTZ,
    status                  TEXT NOT NULL
                            CHECK (status IN ('open','closed','resolved','amended')),

    -- Resolution (the wedge)
    resolution_rules_raw    TEXT,
    resolution_triggers     JSONB,  -- editorial parsed structure

    resolution_mechanism    TEXT
                            CHECK (resolution_mechanism IN (
                                'uma_oracle','kalshi_staff','polymarket_staff',
                                'platform_auto','determinations_committee','other'
                            )),
    proposer_model          TEXT
                            CHECK (proposer_model IN (
                                'permissionless','managed_whitelist',
                                'platform_staff','gov_agency'
                            )),
    resolution_source_name  TEXT,
    resolution_source_url   TEXT,
    resolution_source_type  TEXT
                            CHECK (resolution_source_type IN (
                                'gov_stat_agency','central_bank','regulated_data_vendor',
                                'media_consensus','court_filing','issuer_announcement',
                                'scheduled_event','subjective','other'
                            )),
    contract_terms_url      TEXT,

    -- Settlement
    resolution_outcome      TEXT,
    resolution_value        NUMERIC,
    resolved_at             TIMESTAMPTZ,

    -- Provenance
    field_provenance        JSONB NOT NULL DEFAULT '{}'::jsonb,

    -- Plumbing
    first_seen_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_updated_at         TIMESTAMPTZ NOT NULL DEFAULT now(),

    UNIQUE (platform, platform_market_id)
);

CREATE INDEX markets_event_id_idx         ON markets (event_id);
CREATE INDEX markets_platform_idx         ON markets (platform);
CREATE INDEX markets_status_idx           ON markets (status);
CREATE INDEX markets_res_mechanism_idx    ON markets (resolution_mechanism);
CREATE INDEX markets_res_source_type_idx  ON markets (resolution_source_type);
CREATE INDEX markets_resolve_at_idx       ON markets (resolve_at);

-- Deferred FK from events.primary_market_id (needs markets to exist first)
ALTER TABLE events
    ADD CONSTRAINT events_primary_market_fk
    FOREIGN KEY (primary_market_id) REFERENCES markets(market_id) ON DELETE SET NULL;

COMMENT ON TABLE markets IS
  'One row per platform contract. Raw venue data + ClearMarket editorial fill. '
  'Auto-ingested daily from Kalshi and Polymarket. Events are assigned editorially.';
COMMENT ON COLUMN markets.resolution_mechanism IS
  'Who arbitrates disputes (separate from data source). Apr 22 split.';
COMMENT ON COLUMN markets.proposer_model IS
  'Who may propose outcomes. managed_whitelist = UMA MOOV2 (Aug 2025, 37-proposer whitelist).';


-- =============================================================
-- 3. MARKS — daily pricing snapshots
-- =============================================================
CREATE TABLE marks (
    mark_id                 BIGSERIAL PRIMARY KEY,
    market_id               BIGINT NOT NULL REFERENCES markets(market_id) ON DELETE CASCADE,
    snapshot_date           DATE NOT NULL,

    snapshot_at             TIMESTAMPTZ NOT NULL,
    source_updated_at       TIMESTAMPTZ NOT NULL,

    -- Quote prices (4-side)
    yes_bid                 NUMERIC CHECK (yes_bid BETWEEN 0 AND 1),
    yes_ask                 NUMERIC CHECK (yes_ask BETWEEN 0 AND 1),
    no_bid                  NUMERIC CHECK (no_bid  BETWEEN 0 AND 1),
    no_ask                  NUMERIC CHECK (no_ask  BETWEEN 0 AND 1),

    -- Sizes USD, top-of-book only
    yes_bid_size_usd        NUMERIC CHECK (yes_bid_size_usd >= 0),
    yes_ask_size_usd        NUMERIC CHECK (yes_ask_size_usd >= 0),
    no_bid_size_usd         NUMERIC CHECK (no_bid_size_usd  >= 0),
    no_ask_size_usd         NUMERIC CHECK (no_ask_size_usd  >= 0),

    -- Last trade + implied prob
    yes_last_price          NUMERIC CHECK (yes_last_price BETWEEN 0 AND 1),
    implied_probability     NUMERIC CHECK (implied_probability BETWEEN 0 AND 1),

    -- Volume + open interest
    volume_24h_usd          NUMERIC CHECK (volume_24h_usd   >= 0),
    volume_total_usd        NUMERIC CHECK (volume_total_usd >= 0),
    open_interest_usd       NUMERIC CHECK (open_interest_usd >= 0),  -- NULL for Poly in v0.1

    -- Quality + provenance
    mark_method             TEXT NOT NULL
                            CHECK (mark_method IN (
                                'venue_snapshot','imputed_carry_forward','editorial_override'
                            )),
    stale_flag              BOOLEAN NOT NULL,
    source_count            INTEGER NOT NULL CHECK (source_count >= 0),
    raw_payload             JSONB,

    field_provenance        JSONB NOT NULL DEFAULT '{}'::jsonb,

    UNIQUE (market_id, snapshot_date)
);

CREATE INDEX marks_market_id_date_idx  ON marks (market_id, snapshot_date DESC);
CREATE INDEX marks_snapshot_at_idx     ON marks (snapshot_at);
CREATE INDEX marks_stale_idx           ON marks (stale_flag) WHERE stale_flag = TRUE;

COMMENT ON TABLE marks IS
  'Daily pricing + liquidity snapshot. One row per market per UTC date. '
  'Normalizes Kalshi + Polymarket into single USD feed. '
  'Sizes are top-of-book only; full-book depth deferred to v0.2.';
COMMENT ON COLUMN marks.stale_flag IS
  'TRUE if (snapshot_at - source_updated_at) > 4 hours. Bakes <4hr freshness commitment.';


-- =============================================================
-- 4. RESOLUTION_LOG — append-only audit trail
-- =============================================================
CREATE TABLE resolution_log (
    log_id                  BIGSERIAL PRIMARY KEY,
    market_id               BIGINT NOT NULL REFERENCES markets(market_id) ON DELETE CASCADE,
    event_type              TEXT NOT NULL
                            CHECK (event_type IN (
                                'status_change','rule_change','resolution_proposed',
                                'disputed','resolved','amended','reversed'
                            )),
    occurred_at             TIMESTAMPTZ NOT NULL,
    recorded_at             TIMESTAMPTZ NOT NULL DEFAULT now(),

    from_value              TEXT,
    to_value                TEXT,
    diff                    JSONB,

    source                  TEXT NOT NULL
                            CHECK (source IN (
                                'platform_api','uma_subgraph','editorial_observation',
                                'platform_announcement','cftc_filing'
                            )),
    source_ref              TEXT,
    actor                   TEXT
);

CREATE INDEX resolution_log_market_id_idx   ON resolution_log (market_id, occurred_at DESC);
CREATE INDEX resolution_log_event_type_idx  ON resolution_log (event_type);

COMMENT ON TABLE resolution_log IS
  'Append-only audit trail of market lifecycle events. Never UPDATE or DELETE. '
  'v0.1 populates status_change / rule_change / resolved via API diffs. '
  'resolution_proposed + disputed require UMA subgraph reader (v0.3+).';


-- =============================================================
-- Triggers — auto-update updated_at on events
-- =============================================================
CREATE OR REPLACE FUNCTION set_updated_at() RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER events_set_updated_at
    BEFORE UPDATE ON events
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE OR REPLACE FUNCTION set_last_updated_at() RETURNS TRIGGER AS $$
BEGIN
    NEW.last_updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER markets_set_last_updated_at
    BEFORE UPDATE ON markets
    FOR EACH ROW EXECUTE FUNCTION set_last_updated_at();


COMMIT;

-- =============================================================
-- Notes
-- =============================================================
-- 1. Derived API fields (venues_covered, current_primary_mark, cross_platform_link,
--    spread, mid, divergence_from_primary, hours_since_source_update,
--    resolution_source_classification, resolution_mechanism_display) are NOT columns.
--    They are computed at API serve time. See schema-working-spec.md "Public API derived fields".
--
-- 2. resolution_log has NO UNIQUE constraint — append-only, duplicates distinguished by provenance.
--
-- 3. events.primary_market_id uses deferred FK (added after markets table exists).
--    This lets events be seeded first when needed, though normal flow is markets first.
--
-- 4. Staleness constant (4 hours) is enforced by the ingestion layer, not the DDL.
--    Schema-level documentation only.
--
-- 5. v0.1 excludes: pgvector, open_interest_usd for Polymarket (requires on-chain subgraph),
--    liquidity depth fields (Kalshi/Poly non-comparable), market_relationships table.
