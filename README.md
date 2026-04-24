# ClearMarket

> Institutional reference layer for prediction market data. Structures, classifies, and links markets across Polymarket and Kalshi so research, risk, and data teams can use them like any other asset class.

v0.1.0 — April 2026

---

## The problem

Polymarket and Kalshi publish market data that is useful for retail trading but not ingestion-ready for institutional research or risk. Three gaps a buyer hits immediately:

1. **Resolution logic is opaque.** A 2026 survey of 746 institutional-category Polymarket markets found 0% populate the `resolutionSource` API field, ~8% embed a specific URL in description prose, and ~92% rely on placeholder language ("a consensus of credible reporting"). Kalshi is cleaner but source-naming is loose ("for example, Google Finance" on S&P 500 contracts).
2. **The same question is priced on both platforms under different structures.** Polymarket lists the Fed April 2026 decision as four directional YES/NO questions resolved via UMA; Kalshi lists eleven rate-level strike markets resolved by staff. Nothing in either API tells you they are the same event.
3. **Platforms do not publish an editorial view of what counts as a "family" of related questions.** Nine Polymarket contracts on when the Iran conflict ends are ingestion-level siblings with no connecting metadata.

Institutions solving any of these gaps in-house end up with one-off parses that do not generalize. ClearMarket ships a normalized schema, an enrichment pipeline, and machine-readable specimens you can diff against.

---

## What's here

This repo contains:

- **JSON Schemas** for the four ClearMarket tables (`events`, `markets`, `marks`, `resolution_log`)
- **Postgres DDL** matching the schemas
- **An Enhancement Script** (`enhance.py`) that transforms raw Polymarket + Kalshi API pulls into ClearMarket-shaped records, with AI-drafted editorial enrichment
- **Four v0.1.0 specimens** covering 15 canonical events and 58 markets
- **A sample cache** of the 4 raw API pulls used to generate the specimens (for reproducibility)

All specimens validate against the JSON Schemas. All records carry per-field `field_provenance` flagging whether a value came from the platform API, ClearMarket editorial, a derived computation, an imputed proxy, or a known venue limitation.

---

## The four specimens

| Specimen | Platforms | Events | Markets | What it demonstrates |
|---|---|---|---|---|
| `samples/iran/` | Polymarket | 9 | 9 | Thematic family (9 related questions, shared tag `iran-conflict`). UMA Optimistic Oracle with subjective resolution. Full 4-side CLOB prices for open markets; `resolved_at` timestamps for already-settled children. |
| `samples/fed-apr-2026/` | Polymarket + Kalshi | 1 | 15 | Cross-platform single event. 4 UMA-resolved Polymarket directional markets and 11 staff-resolved Kalshi strike markets, all normalized under one `event_id`. |
| `samples/netanyahu/` | Polymarket | 4 | 4 | Thematic family with deadline variants. Same subjective UMA pattern as Iran. |
| `samples/sp500-2026/` | Kalshi | 1 | 30 | Strike ladder. 30 binary markets resolving to one closing value. Editorial refinement of Kalshi's loose source naming ("for example, Google Finance") to the authoritative calculator (S&P Dow Jones Indices). |
| **Total** | | **15** | **58** | |

Open any `samples/<id>/specimen.json` for the full bundle. The top-level `_meta.editorial_review_notes` block lists every AI-drafted field and the rules that govern them.

---

## The wedge in one sentence

Platforms ship you a market. ClearMarket ships you a canonical question, an authoritative data source, a parsed resolution structure, a cross-platform linkage, a thematic family, and a provenance record saying which fields came from where.

Three product surfaces sit on top of the same schema:

| Surface | What it does | Buyer |
|---|---|---|
| **Screen** | Classify which markets are institutionally tradable vs. which rely on vague placeholder resolution language. | Hedge funds wanting structured exposure without parsing prose at 20K-market scale. |
| **Rate** (v0.3+) | Quantify dispute risk via historical UMA patterns. Requires UMA subgraph reader. | Swap desks pricing tail risk, middle-office counterparties sizing collateral. |
| **Normalize** | Present the same canonical event on Kalshi and Polymarket side by side with uniform fields. | Data distributors (Bloomberg, ICE, Tradeweb, VettaFi) consuming a consistent feed. |

Screen and Normalize are v0.1-shippable. Rate is v0.3 and depends on on-chain UMA data.

---

## Architecture

Three steps. The first two are deterministic Python; the third is the editorial layer that platforms do not ship.

```
 ┌────────────────────────────────────────────────────────────────┐
 │  1. INGESTION (plain HTTP, zero LLM cost)                      │
 │                                                                │
 │     • Polymarket Gamma API   → event + market metadata         │
 │     • Polymarket CLOB API    → 4-side order book               │
 │     • Kalshi Trade API       → markets + series metadata       │
 └────────────────────────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────┐
 │  2. DETERMINISTIC TRANSFORMS (Python, zero LLM cost)           │
 │                                                                │
 │     • Field mapping (Poly endDate → ClearMarket close_at)      │
 │     • Type coercion, status inference                          │
 │     • Derived fields: spread, mid, venues_covered,             │
 │       cross_platform_link, current_primary_mark                │
 │     • field_provenance flags (platform_api vs. editorial)      │
 └────────────────────────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────┐
 │  3. EDITORIAL ENRICHMENT (LLM-based, cached)                   │
 │                                                                │
 │     Per market:                                                │
 │       • underlying_reference   ← named data source             │
 │                                                                │
 │     Per event:                                                 │
 │       • editorial_notes        ← institutional framing         │
 │       • tags                   ← thematic / attribute / entity │
 │       • question               ← canonical grammar rewrite     │
 │                                                                │
 │     Cached to .enhance-cache/llm/ by input hash.               │
 │     Re-runs cost $0 unless the input changes.                  │
 └────────────────────────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────┐
 │  4. STORAGE + API (not yet in v0.1)                            │
 │                                                                │
 │     • Postgres (Supabase) — 4 tables per schema/ddl.sql        │
 │     • Public API — /events/*, /markets/*, /marks/*             │
 │     • All derived fields computed at serve time, not stored    │
 └────────────────────────────────────────────────────────────────┘
```

Every paying consumer read hits cached storage. Zero LLM cost at read time.

---

## The editorial layer, concretely

What AI drafts vs. what the platform ships, per record:

**Markets table, AI-drafted fields:**
- `underlying_reference` — a one-sentence identification of the real-world data source
- `resolution_source_name` — only when the platform API ships empty (Polymarket only; Kalshi is always authoritative via `settlement_sources`)

**Events table, AI-drafted fields:**
- `editorial_notes` — 2-3 sentence institutional framing
- `tags` — 4-6 tags mixing thematic, attribute, and entity
- `question` — canonical grammar rewrite of raw platform prose when needed

**Everything else** is either a deterministic transform (Python), a derived field (computed at serve time), a platform API value, or flagged with `null_by_venue_limitation` if the venue does not expose it.

### Rules the editorial layer respects

- **Kalshi resolution_source_name and resolution_source_url are ALWAYS pulled from series `settlement_sources`.** No UMA-style subjective default ever. Kalshi has structured settlement metadata; use it.
- **Polymarket resolution_source_name uses editorial default language ("Credible news reporting — subjective") ONLY when the Polymarket API ships an empty field.** Where Polymarket description prose names a specific URL (e.g., Fed markets citing federalreserve.gov), the platform-shipped value wins.
- **Index and data-product markets are normalized to the authoritative calculator**, not platform shorthand. "S&P 500" resolves to "S&P Dow Jones Indices," not "Google Finance," regardless of what Kalshi series metadata says.
- **All generated prose anchors on `close_at` or `resolve_at` for the authoritative date.** The AI does not infer future years from present-day reasoning.

These rules are enforced in `enhance.py` system prompts and the per-specimen configuration, not by hoping the model gets it right.

---

## Schema overview

Four tables. Full definitions in `schema/`.

| Table | Role | Rows | PK | Key FKs |
|---|---|---|---|---|
| `events` | Canonical tradable questions. Editorial layer. | One per canonical question. | `event_id` (CM-prefixed 12-char stable ID) | `primary_market_id` → markets |
| `markets` | Per-platform contracts. Raw platform data + editorial fill. | One per market per platform. | `market_id` (BIGSERIAL) | `event_id` → events (nullable) |
| `marks` | Daily pricing snapshots. One per market per UTC date. | High cardinality. | `mark_id` | `market_id` → markets |
| `resolution_log` | Append-only lifecycle audit trail. | Thin in v0.1; expanded in v0.3 via UMA subgraph reader. | `log_id` | `market_id` → markets |

### Design decisions worth noting

- **Flat events with tag-based grouping, not recursive hierarchy.** Every event has ≥1 market. Thematic families (Iran conflict, Fed decisions) are expressed via shared tags, not parent/child hierarchy. Matches Bloomberg / Stripe conventions. Consumers filter families with `GET /events?tag=<name>`.
- **Resolution mechanism vs. resolution source type are separate fields.** `resolution_mechanism` is who arbitrates (UMA oracle, Kalshi staff, platform auto, etc.). `resolution_source_type` is what data is cited (central bank, regulated data vendor, media consensus, subjective, etc.). Previously conflated; split makes it possible to filter for "UMA-resolved but with a named central-bank source" (e.g., Poly Fed markets).
- **`proposer_model` enum** on markets captures UMA's MOOV2 upgrade (August 2025) — a managed whitelist of 37 proposers — distinct from Kalshi's platform-staff model or permissionless proposals.
- **`field_provenance` on every row.** Per-field flag with five values: `platform_api`, `clearmarket_editorial`, `derived`, `imputed`, `null_by_venue_limitation`. Lets a consumer audit which fields are raw vs. enriched at field granularity.
- **Derived fields are computed at API serve time, not stored.** `spread`, `mid`, `venues_covered`, `cross_platform_link`, `current_primary_mark` — all reshaped from the normalized tables on demand.

---

## v0.1.0 scope

### Included

- 4-table schema (JSON Schema + Postgres DDL)
- Enhancement Script (`enhance.py`) with CLOB + LLM enrichment
- 4 specimen events, 15 events, 58 markets, 58 marks
- `field_provenance` on every record
- Deterministic 12-character canonical event IDs

### Known v0.1 limitations (called out honestly)

- **`resolution_log` ships empty.** UMA subgraph reader lands in v0.3; Kalshi lifecycle events are editorial-gated. Shipping zero rows beats shipping thin rows that oversell the capability.
- **`open_interest_usd` is null for Polymarket.** Requires on-chain subgraph; v0.2+.
- **`size` fields are top-of-book only.** Full-book depth requires a dedicated crawler; deferred to v0.2.
- **`liquidity` field dropped entirely.** Kalshi ships `liquidity_dollars` as top-of-book; Polymarket ships `liquidityNum` as full-book. They are not comparable. Revisit in v0.2 with an own-crawler for both.
- **No live API yet.** v0.1 is the schema + specimens. Live HTTP endpoints land in v0.2 conditional on buyer pull.
- **`resolution_triggers` parsing of rules prose is deferred.** v0.1 ships the raw rules text; v0.2 adds LLM-parsed structured triggers, thresholds, and exclusions.

### Roadmap

| Version | What lands | Target |
|---|---|---|
| v0.1.0 | Schema + Enhancement Script + 4 specimens (this release) | Apr 2026 |
| v0.1.1 | CI validation, contract tests, additional specimens | May 2026 |
| v0.2 | Live HTTP API, size depth, `resolution_triggers` parsing, Polymarket open interest via on-chain subgraph | Conditional on buyer pull |
| v0.3 | `resolution_log` populated via UMA subgraph reader, dispute-risk `Rate` surface | Q3 2026 |

---

## Running the Enhancement Script locally

```
# 1. Clone the repo
git clone https://github.com/JDSource/clearmarket.git
cd clearmarket

# 2. Python 3.9+ with a few packages
pip install anthropic python-dotenv requests jsonschema

# 3. Add your Anthropic API key
cat > .env <<'EOF'
ANTHROPIC_API_KEY=sk-ant-api03-...your-key...
EOF

# 4. Point the script at a raw API pull directory
#    (sample raw pulls at raw/clearmarket-api-pulls-apr22/)

# 5. Run
python3 enhance.py

# Output lands in samples/<specimen_id>/specimen.json
# Each file validates against the 4 schemas in schema/
```

The script fetches Polymarket CLOB order books live on first run (cached locally thereafter). It skips CLOB fetches for resolved/closed markets. LLM calls are cached by input hash; re-runs hit cache and cost zero.

Run `python3 enhance.py --no-llm` to skip LLM enrichment and produce structurally valid specimens with rule-based editorial defaults only.

---

## Repository layout

```
clearmarket/
├── README.md                           this file
├── enhance.py                          Enhancement Script
├── schema/
│   ├── events.schema.json              JSON Schema
│   ├── markets.schema.json
│   ├── marks.schema.json
│   ├── resolution_log.schema.json
│   └── ddl.sql                         Postgres DDL
├── samples/
│   ├── iran/specimen.json              4-table bundle for Iran family
│   ├── fed-apr-2026/specimen.json      Cross-platform Fed decision
│   ├── netanyahu/specimen.json         Netanyahu tenure family
│   └── sp500-2026/specimen.json        S&P 500 yearly strike ladder
├── raw/
│   └── clearmarket-api-pulls-apr22/    Raw API dumps used to generate v0.1.0
├── .env                                (gitignored — API key)
├── .enhance-cache/                     (gitignored — LLM + CLOB cache)
└── .gitignore
```

---

## Acknowledgments

This release uses public data from [Polymarket](https://polymarket.com) and [Kalshi](https://kalshi.com). Editorial enrichment uses [Claude Haiku 4.5](https://docs.anthropic.com/claude/docs/models-overview) from Anthropic. Schema design draws on conventions from Markit, Bloomberg Open Symbology (BSYM), and Refinitiv PermID.

---

## Status

Pre-MVP. 20 enriched records in the main branch are being replaced with the four v0.1.0 specimens as of this release. Design-stage feedback welcome via GitHub issues or direct contact.

**Built by:** Jeremy Dietz. Ran Digital Products at the Toronto Stock Exchange. VP Product at Coinsquare, the first fully regulated crypto exchange in Canada. Independently built Catalyst Signal, an AI research platform covering 220+ public equities. Now building ClearMarket.
