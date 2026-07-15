// llms.txt as a build-time route so coverage counts come from the bundle, never hand-edited.
// (The old static web/public/llms.txt shipped "~1,850 events" two vintages past its sell-by.)
import type { APIRoute } from 'astro';
import { coverageLabel } from '../lib/universe';

const body = `# ClearMarket

Reference data layer for prediction markets. Cross-venue event linking, graded resolution clarity, resolution-source provenance, and catalysts across Kalshi and Polymarket. Open and free; built to be queried by agents.

## What this is

ClearMarket normalizes Kalshi and Polymarket markets into a single schema:
- events: a venue's bundle of one or more markets under a canonical question, classified, with catalyst dates. Every event is single-venue.
- markets: one row per venue listing, with a Resolution Clarity Grade (A/B/C) and full resolution-source provenance — the source is named where the venue commits to one; where it doesn't, that absence is classified and graded. Markets recognized as the same question across venues or events also carry a question_id (the venue-independent identity of the bet; null when not yet linked) and also_on (the same question priced on other venues).
- cross-venue link: markets sharing a question_id are the same bet across Kalshi and Polymarket; a market's also_on field gives an array of { venue, market_id, price } (one entry per other venue it trades on), or is null when it trades on only one venue.

${coverageLabel()}. Prices refresh hourly. Read-only.

## REST API (open, free, no key)

Base: https://api.clearmarket.fyi

- GET /v1/events?category=&platform=&grade=&q=&limit=&offset= : list and filter events
- GET /v1/events/{slug} : full event, all linked markets, grades, windowed catalysts
- GET /v1/markets/{market_id} : single market, price, resolution provenance
- GET /v1/markets/movers?min_mult=&limit= : day-over-day volume movers (volume-spike signal)
- GET /v1/catalysts/upcoming?days=N : scheduled catalysts across all events
- POST /v1/keys {"email":"..."} : optional free key, lifts the limit to 10,000/day

Open by default: full universe, no key, 1,000 requests/day per IP. CORS open.
Anonymous access is permanent. A free key (email only) additionally gets you advance
notice before any schema change or deprecation — recommended if this API is in a
pipeline. REST responses carry the same offer in an additive \`_notice\` field.
Broken or missing something? hello@clearmarket.fyi reaches a human.

## MCP server (agent-first)

Streamable HTTP at https://api.clearmarket.fyi/mcp. Open, read-only.

Tools:
- list_events : browse or search the universe (short keyword q; returns grade, rcg_score, status per event)
- get_event : full graded record for one event (set detail=concise for a lean grade/price view of big multi-market events)
- get_market : price and resolution provenance for one market (accepts a CM-MKT id, a venue-native id/ticker, or a market URL best-effort — Kalshi URLs resolve; Polymarket needs the conditionId)
- list_upcoming_catalysts : scheduled catalysts in the next N days
- list_signals : browse the CM Signal wire (filter by event_id, category, venue, detection_path)
- get_signal : full wire bulletin by slug

Connect via mcp-remote (Claude Desktop / Cursor): npx -y mcp-remote https://api.clearmarket.fyi/mcp

## CM Signal (daily wire) — under /signals (its own namespace, not /v1/)

- https://clearmarket.fyi/signals/ : wire index (HTML + embedded JSON-LD DataCatalog)
- https://clearmarket.fyi/signals.json : full wire list, newest first
- https://clearmarket.fyi/signals/{slug}.json : single wire record
- https://clearmarket.fyi/signals/for-event/{event_id}.json : every wire for a given CM event
- https://clearmarket.fyi/signals/rss.xml : feed for indexers
- also via MCP: list_signals / get_signal (above)

## Example slugs

- kxgdpyear-26 : will GDP growth in 2026 exceed 2%
- kxinxy-26dec31h1600 : will the S&P 500 close above a level on Dec 31, 2026
- bitcoin-vs-gold-vs-sp-500-in-2026 : will Bitcoin outperform gold and the S&P in 2026

## Eligibility screens

Jurisdiction-specific distribution rule-sets screened per contract. eligibility screens are NOT market quality — quality is the Resolution Clarity Grade. Statuses (eligible / review / not_eligible) describe fit against one named rule-set only. Screening data supporting a dealer's own determination, not a compliance opinion.

- https://clearmarket.fyi/screens/ : index of screens (first regime: ciro-26-0076 — CIRO Administrative Bulletin 26-0076, Canadian dealer distribution under IDPC Rule 2246(2))
- https://clearmarket.fyi/screens/ciro-26-0076/ : per-contract statuses, review clusters, verbatim rule mapping
- https://clearmarket.fyi/screens/ciro-26-0076.json : machine twin (screen summary + market-id lists by status; full per-contract records in the .csv)
- https://clearmarket.fyi/screens/ciro-26-0076.csv : flat per-contract export

## Schema

JSON Schema files (draft 2020-12):
- https://raw.githubusercontent.com/JDSource/clearmarket/main/schema/events.schema.json
- https://raw.githubusercontent.com/JDSource/clearmarket/main/schema/markets.schema.json
- https://raw.githubusercontent.com/JDSource/clearmarket/main/schema/marks.schema.json
- https://raw.githubusercontent.com/JDSource/clearmarket/main/schema/resolution_log.schema.json

## Attribution

Open and free to use. Attribution required: cite ClearMarket (clearmarket.fyi).
Every API and MCP record carries a \`_provenance\` field. The canonical ids are the
citation unit, all in ClearMarket's namespace: market_id (CM-MKT-... — one contract
on one venue), event_id (CM-EVT-... — a single-venue bundle), and question_id (the
venue-independent bet; the same question_id is the cross-venue link). Persist and
reference them so a claim stays traceable to its source.

## Repository

https://github.com/JDSource/clearmarket

## Contact

hello@clearmarket.fyi
`;

export const GET: APIRoute = () =>
  new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
