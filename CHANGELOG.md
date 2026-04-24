# Changelog

All notable changes to ClearMarket are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned (v0.1.1, May 2026)
- GitHub Actions CI validating specimens against JSON Schemas on every PR
- OpenAPI 3.0 spec + ReDoc rendering via GitHub Pages
- Additional specimens across categories (politics, sports, crypto)

### Planned (v0.2, conditional on buyer pull)
- Live HTTP API endpoints: `/events`, `/markets`, `/marks`
- Structured `resolution_triggers` parsed from platform rules prose
- Full-book order-book depth (currently top-of-book only)
- Polymarket `open_interest_usd` via on-chain subgraph
- Normalized `liquidity` field (currently dropped; Kalshi top-of-book vs. Poly full-book non-comparable)

### Planned (v0.3)
- `resolution_log` populated via UMA subgraph reader (Polymarket disputes) + Kalshi lifecycle API diff
- Dispute-risk classification ("Rate" product surface)
- Historical UMA proposer whitelist tracking

---

## [0.1.0] - 2026-04-24

First public release. Schema + enrichment pipeline + four reference specimens.

### Added

**Schema**
- 4-table canonical structure: `events`, `markets`, `marks`, `resolution_log`
- JSON Schema (draft 2020-12) definitions under `schema/`
- Postgres DDL under `schema/ddl.sql` with indexes, foreign keys, and check constraints
- Deterministic 12-character canonical event IDs (format: `CM` + 9-char vowel-free base36 + 1-char mod-10 check digit)

**Enrichment pipeline (`enhance.py`)**
- Deterministic transforms: field mapping, type coercion, status inference, derived-field computation
- Polymarket Gamma API + CLOB API integration (4-side order-book pricing, resolved_at timestamps)
- Kalshi Trade API integration (settlement_sources from series metadata, lifecycle state mapping)
- LLM-drafted editorial fields: `underlying_reference`, `editorial_notes`, `tags`, canonical `question` rewrites
- Local file-based cache for LLM calls and CLOB fetches (re-runs hit cache, zero marginal cost)
- `--no-llm` flag for deterministic-only runs

**Specimens**
- `samples/iran/`: Iran x Israel/US conflict family (9 events, 9 markets, Polymarket-only, UMA subjective resolution)
- `samples/fed-apr-2026/`: Fed April 2026 rate decision (1 event, 15 markets, cross-platform: 4 Polymarket + 11 Kalshi)
- `samples/netanyahu/`: Netanyahu tenure family (4 events, 4 markets, Polymarket-only, deadline variants)
- `samples/sp500-2026/`: S&P 500 year-end 2026 (1 event, 27 strike markets, Kalshi-only, regulated data vendor resolution)
- All 125 records (15 events + 55 markets + 55 marks) validate against the JSON Schemas

**Data quality + provenance**
- Per-field `field_provenance` audit trail across every row
- Five source classifications: `platform_api`, `clearmarket_editorial`, `derived`, `imputed`, `null_by_venue_limitation`
- `ai_drafted: true` marker on all LLM-generated fields for reviewer transparency

**Architecture decisions (locked this release)**
- Flat events with tag-based thematic grouping (no parent/child hierarchy)
- `resolution_mechanism` separated from `resolution_source_type` (who arbitrates vs. what data is cited)
- `proposer_model` enum capturing UMA MOOV2 whitelist (August 2025) vs. permissionless vs. platform-staff
- `editorial_notes` public-facing (surfaced in API responses, not internal-only)
- Unified `field_provenance` enum across all four tables
- `subjective` enum value on `resolution_source_type` for markets lacking a named authoritative data source

### Known limitations in v0.1.0

- **`resolution_log` ships schema-only.** UMA subgraph reader for Polymarket disputes and Kalshi lifecycle API diff land in v0.3. Shipping zero populated rows rather than thin rows that oversell the capability.
- **`open_interest_usd` is null for Polymarket markets.** Requires on-chain subgraph; v0.2.
- **Size fields are top-of-book only.** Full-book depth requires a dedicated crawler; v0.2.
- **`liquidity` field dropped entirely.** Kalshi's `liquidity_dollars` (top-of-book) and Polymarket's `liquidityNum` (full-book CLOB total) are not directly comparable. Revisit in v0.2 with own-crawler for both.
- **No live API endpoints yet.** v0.1 ships the schema + specimens + enhancement pipeline. HTTP endpoints land in v0.2, gated on buyer pull.
- **`resolution_triggers` ships as unparsed JSONB in some specimens.** LLM-based extraction from rules prose lands in v0.2.
