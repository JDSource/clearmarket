# ClearMarket

> Institutional reference layer for prediction market data. Structures, classifies, grades, and links markets across Polymarket and Kalshi so research, risk, and data teams can use them like any other asset class.

**Live now:** [clearmarket.fyi](https://clearmarket.fyi) · REST `api.clearmarket.fyi/v1` · MCP `api.clearmarket.fyi/mcp` · daily wire feed at [`/signals`](https://clearmarket.fyi/signals). Open and read-only — no key required.

**Coverage:** ~1,857 events / ~15,138 markets across Kalshi + Polymarket. Every market carries a **Resolution Clarity Grade** (RCG A/B/C), a named resolution source, and cross-venue claim links. Prices refresh hourly.

v0.2 · June 2026

---

## Quickstart

No key, no signup — open and read-only.

```bash
# REST — search the graded universe
curl -s "https://api.clearmarket.fyi/v1/events?q=fed"

# one event, fully graded (markets + resolution provenance + cross-venue links)
curl -s "https://api.clearmarket.fyi/v1/events/kxfed-26jul"

# the daily CM Signal wire feed
curl -s "https://clearmarket.fyi/signals.json"
```

**MCP** (agent clients — Claude Desktop, Cursor, VS Code): streamable HTTP at `https://api.clearmarket.fyi/mcp`, six read-only tools (`list_events`, `get_event`, `get_market`, `list_upcoming_catalysts`, `list_signals`, `get_signal`). One-click install:

[![Add to Cursor](https://img.shields.io/badge/Add_to-Cursor-000000?logo=cursor&logoColor=white)](cursor://anysphere.cursor-deeplink/mcp/install?name=clearmarket&config=eyJ1cmwiOiJodHRwczovL2FwaS5jbGVhcm1hcmtldC5meWkvbWNwIn0=)
[![Install in VS Code](https://img.shields.io/badge/Install_in-VS_Code-0098FF?logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=clearmarket&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapi.clearmarket.fyi%2Fmcp%22%7D)

```bash
# Claude Code
claude mcp add --transport http clearmarket https://api.clearmarket.fyi/mcp
```

…or add it by hand:

```jsonc
// claude_desktop_config.json  /  ~/.cursor/mcp.json
{ "mcpServers": { "clearmarket": { "command": "npx", "args": ["-y", "mcp-remote", "https://api.clearmarket.fyi/mcp"] } } }
```

Every URL also ships a parallel `.json`, embedded JSON-LD, and a row in [`/llms.txt`](https://clearmarket.fyi/llms.txt) — agents never have to scrape HTML.

---

## The problem

Polymarket and Kalshi publish market data that is useful for retail trading but not ingestion-ready for institutional research or risk. Three gaps a buyer hits immediately:

1. **You can't tell where the resolution data comes from.** On 92% of institutional-category Polymarket markets, the resolution source is placeholder language ("a consensus of credible reporting"), not a named authority. Kalshi names sources but loosely ("for example, Google Finance" on S&P 500 contracts).
2. **The same event is priced differently on each platform.** Polymarket lists the Fed April 2026 rate decision as four directional yes/no questions; Kalshi lists eleven rate-level brackets. Nothing in either API tells you they are pricing the same thing.
3. **Related markets aren't grouped, on a single platform or across them.** Nine Polymarket contracts on when the Iran conflict ends sit in the API as nine separate items, with nothing connecting them. Cross-platform, the gap is wider still.

Institutions solving any of these gaps in-house end up with one-off parses that do not generalize. ClearMarket ships a normalized schema, an enrichment pipeline, and machine-readable specimens you can diff against.

---

## Before and after

### What the platforms give you

Polymarket on the April 2026 Fed rate decision (1 of 4 directional markets):

```json
{
  "question": "Will the Fed decrease interest rates by 50+ bps after the April 2026 meeting?",
  "endDate": "2026-04-30T23:00:00Z",
  "resolutionSource": "",
  "volume": 1530000,
  "description": "This market will resolve 'Yes' if ... [rules embedded in prose]"
}
```

Kalshi on the same Fed decision (1 of 11 strike markets):

```json
{
  "ticker": "KXFED-26APR-T3.25",
  "title": "Will the upper bound of the federal funds rate be above 3.25%...",
  "close_time": "2026-04-29T17:55:00Z",
  "rules_primary": "If the upper bound of the target federal funds rate... [prose]",
  "settlement_sources": [{"name": "Federal Reserve Board of Governors", "url": "..."}]
}
```

Empty `resolutionSource`. Rules buried in prose. No catalyst calendar. And nothing telling you these are two of fifteen markets pricing the same Fed meeting.

### What ClearMarket gives you

```json
{
  "event_id": "CMKD3L8N2PRT",
  "slug": "fed-april-2026-rate-decision",
  "question": "What will the Federal Reserve announce at the April 2026 FOMC meeting?",
  "category": "macro",

  // shared labels for searching across both platforms
  "tags": ["macro", "fed-rate-decisions", "fomc", "monetary-policy", "2026"],

  "venues_covered": ["polymarket", "kalshi"],

  // real-world events that move the price
  "catalyst_dates": [
    {"date": "2026-04-29", "event": "FOMC meeting Day 1"},
    {"date": "2026-04-30", "event": "FOMC statement + press conference"}
  ],

  "editorial_notes": "These markets price the Fed's April 29, 2026 target rate decision. Polymarket has four directional questions; Kalshi has eleven rate-level strike markets. Both cite the Federal Reserve Board of Governors as the source."
}
```

One canonical event. Fifteen markets bound across both platforms. The FOMC meeting on the catalyst calendar. The Federal Reserve identified as the underlying source.

Full record (markets, daily marks, per-field provenance) at [`samples/fed-apr-2026/specimen.json`](samples/fed-apr-2026/specimen.json).

---

## What's here

The live product (site, REST API, MCP, daily wire feed) serves the full ~1,857-event universe. This repo is the **open schema + enrichment pipeline + reference specimens** behind it:

- **JSON Schemas** for the four ClearMarket tables (`events`, `markets`, `marks`, `resolution_log`)
- **Postgres DDL** matching the schemas
- **An Enhancement Script** (`enhance.py`) that transforms raw Polymarket + Kalshi API pulls into ClearMarket-shaped records, with AI-drafted editorial enrichment
- **Reference specimens** (15 canonical events, 55 markets) you can diff against — the worked examples below
- **The CFTC ANPRM comment** (`cftc-anprm/`) — the cross-venue resolution-divergence analysis filed with the Commission (RIN 3038-AF65)

All specimens validate against the JSON Schemas. All records carry per-field `field_provenance` flagging whether a value came from the platform API, ClearMarket editorial, a derived computation, an imputed proxy, or a known venue limitation.

---

## The four specimens

| Specimen | Platforms | Events | Markets | What it demonstrates |
|---|---|---|---|---|
| `samples/iran/` | Polymarket | 9 | 9 | Thematic family (9 related questions, shared tag `iran-conflict`). UMA Optimistic Oracle with subjective resolution. Full 4-side CLOB prices for open markets; `resolved_at` timestamps for already-settled children. |
| `samples/fed-apr-2026/` | Polymarket + Kalshi | 1 | 15 | Cross-platform single event. 4 UMA-resolved Polymarket directional markets and 11 staff-resolved Kalshi strike markets, all normalized under one `event_id`. |
| `samples/netanyahu/` | Polymarket | 4 | 4 | Thematic family with deadline variants. Same subjective UMA pattern as Iran. |
| `samples/sp500-2026/` | Kalshi | 1 | 27 | Strike ladder. 27 binary markets resolving to one closing value. Editorial refinement of Kalshi's loose source naming ("for example, Google Finance") to the authoritative calculator (S&P Dow Jones Indices). |
| **Total** | | **15** | **55** | |

Open any `samples/<id>/specimen.json` for the full bundle. The top-level `_meta.editorial_review_notes` block lists every AI-drafted field and the rules that govern them.

---

## The wedge in one sentence

ClearMarket is the independent enrichment layer above those feeds. It parses what the platforms don't publish in structured form: canonical questions, authoritative data sources, parsed resolution structures, cross-platform linkage, thematic families, and per-field provenance.

Two products sit on top of the same schema (a third is on the roadmap):

| Product | What it does | Buyer |
|---|---|---|
| **CM Data** (live) | The reference layer: grade resolution clarity (RCG A/B/C), name resolution sources, link the same claim across venues, per-field provenance. Markit-shape, licensable. | Data distributors (Bloomberg, ICE, Tradeweb, VettaFi), research/risk desks, AI agents. |
| **CM Signal** (live) | Daily wire feed on top of CM Data — news-cycle, volume-spike, cross-venue divergence, and benchmark-drift bulletins, published to web + JSON + MCP. | Analysts and desks tracking prediction-market-implied signal. |
| **Rate** (roadmap) | Quantify dispute risk via historical UMA patterns. Requires UMA subgraph reader. | Swap desks pricing tail risk, middle-office counterparties sizing collateral. |

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
 │       also_on, current_primary_mark                            │
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
 │  4. STORAGE + API (LIVE)                                       │
 │                                                                │
 │     • Cloudflare D1 + Worker: api.clearmarket.fyi/v1/*         │
 │     • REST + MCP (/mcp) + parallel JSON / JSON-LD              │
 │     • Hourly price refresh; daily CM Signal wires              │
 └────────────────────────────────────────────────────────────────┘
```

Every paying consumer read hits cached storage. Zero LLM cost at read time.

---

## The editorial layer, concretely

What AI drafts vs. what the platform ships, per record:

**Markets table, AI-drafted fields:**
- `underlying_reference`: a one-sentence identification of the real-world data source
- `resolution_source`: only when the platform API ships empty (Polymarket only; Kalshi is always authoritative via `settlement_sources`)

**Events table, AI-drafted fields:**
- `editorial_notes`: 2-3 sentence institutional framing
- `tags`: 4-6 tags mixing thematic, attribute, and entity
- `question`: canonical grammar rewrite of raw platform prose when needed

**Everything else** is either a deterministic transform (Python), a derived field (computed at serve time), a platform API value, or flagged with `null_by_venue_limitation` if the venue does not expose it.

### Rules the editorial layer respects

- **Kalshi resolution_source and source_citation are ALWAYS pulled from series `settlement_sources`.** No UMA-style subjective default ever. Kalshi has structured settlement metadata; use it.
- **Polymarket resolution_source uses editorial default language ("Credible news reporting, subjective") ONLY when the Polymarket API ships an empty field.** Where Polymarket description prose names a specific URL (e.g., Fed markets citing federalreserve.gov), the platform-shipped value wins.
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
- **Resolution mechanism vs. resolution source type are separate fields.** `arbitration_model` is who arbitrates (UMA oracle, Kalshi staff, platform auto, etc.). `source_type` is what data is cited (central bank, regulated data vendor, media consensus, subjective, etc.). Previously conflated; split makes it possible to filter for "UMA-resolved but with a named central-bank source" (e.g., Poly Fed markets).
- **`resolution_proposer` enum** on markets captures UMA's MOOV2 upgrade (August 2025, a managed whitelist of 37 proposers), distinct from Kalshi's platform-staff model or permissionless proposals.
- **`field_provenance` on every row.** Per-field flag with five values: `platform_api`, `clearmarket_editorial`, `derived`, `imputed`, `null_by_venue_limitation`. Lets a consumer audit which fields are raw vs. enriched at field granularity.
- **Derived fields are computed at API serve time, not stored.** `spread`, `mid`, `venues_covered`, `also_on`, `current_primary_mark`: all reshaped from the normalized tables on demand.

---

## What's shipped (v0.2)

### Live

- Public site, REST API, and MCP server over the full ~1,857-event universe
- Resolution Clarity Grade (RCG A/B/C) + named resolution source on every market
- Cross-venue claim linking (the same graded claim across Kalshi + Polymarket)
- CM Signal daily wire feed (news-cycle, volume-spike, cross-venue divergence, benchmark-drift)
- Hourly price refresh; four-format output (HTML + JSON-LD + parallel JSON + `llms.txt`)

### In this repo

- 4-table schema (JSON Schema + Postgres DDL)
- Enhancement Script (`enhance.py`) with CLOB + LLM enrichment
- Reference specimens: 15 events, 55 markets, 55 marks
- `field_provenance` on every record
- Deterministic canonical event + market IDs

### Known limitations (called out honestly)

- **`resolution_log` ships empty.** UMA subgraph reader lands in v0.3; Kalshi lifecycle events are editorial-gated. Shipping zero rows beats shipping thin rows that oversell the capability.
- **`open_interest_usd` is null for Polymarket.** Requires on-chain subgraph; v0.2+.
- **`size` fields are top-of-book only.** Full-book depth requires a dedicated crawler; deferred to v0.2.
- **`liquidity` field dropped entirely.** Kalshi ships `liquidity_dollars` as top-of-book; Polymarket ships `liquidityNum` as full-book. They are not comparable. Revisit with an own-crawler for both.
- **`resolution_triggers` parsing of rules prose is deferred.** The raw rules text ships today; LLM-parsed structured triggers, thresholds, and exclusions are next.

### Roadmap

| Version | What lands | Status |
|---|---|---|
| v0.1 | Schema + Enhancement Script + reference specimens | Shipped Apr 2026 |
| v0.2 | Live site + REST API + MCP, RCG grading, cross-venue linking, CM Signal wire feed, hourly prices | **Shipped Jun 2026** |
| v0.3 | `resolution_log` via UMA subgraph reader, dispute-risk `Rate` surface, full-book depth, Polymarket open interest | Planned |

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
├── web/                                Astro site (clearmarket.fyi): pages, components, wire content
├── api/                                Cloudflare Worker: REST /v1/* + MCP /mcp, D1 schema + seed
├── cftc-anprm/                         CFTC ANPRM comment + reproducible analysis (RIN 3038-AF65)
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
├── .env                                (gitignored: API key)
├── .enhance-cache/                     (gitignored: LLM + CLOB cache)
└── .gitignore
```

---

## Acknowledgments

This release uses public data from [Polymarket](https://polymarket.com) and [Kalshi](https://kalshi.com). Editorial enrichment uses [Claude Haiku 4.5](https://docs.anthropic.com/claude/docs/models-overview) from Anthropic. Schema design draws on conventions from Markit, Bloomberg Open Symbology (BSYM), and Refinitiv PermID.

---

## Status

Live. The site, REST API, and MCP server are public over the full universe, and CM Signal wires publish daily. Feedback welcome via GitHub issues or direct contact.

**Built by:** Jeremy Dietz. Ran Digital Products at the Toronto Stock Exchange. VP Product at Coinsquare, the first fully regulated crypto exchange in Canada. Independently built Catalyst Signal, an AI research platform covering 220+ public equities. Now building ClearMarket.
