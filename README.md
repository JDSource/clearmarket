# ClearMarket

**Structured intelligence for prediction markets.**

Prediction market platforms publish prices and order books. They don't publish what those markets actually mean — how they resolve, what events move them before resolution, how the same question is structured differently across platforms, or where coverage gaps exist.

ClearMarket is the enrichment layer that fills this gap. Raw market data in, structured intelligence out.

---

## The Problem

An agent trading prediction markets today gets this from the API:

```json
{
  "slug": "russia-x-ukraine-ceasefire-before-2027",
  "price": 0.375,
  "volume": 11771072,
  "end_date": "2026-12-31"
}
```

Four fields. No information about what triggers resolution, what doesn't count (humanitarian pauses? energy-only ceasefires?), when the key diplomatic events that move price are scheduled, whether Kalshi has an equivalent market, or how this relates to the 6 other ceasefire markets on the same platform.

The agent is trading blind on everything except price.

---

## What ClearMarket Adds

ClearMarket enriches raw market data with 5 fields that don't exist anywhere else:

| Field | What it contains | Why it matters |
|---|---|---|
| **resolution_logic** | Parsed triggers, exclusions, and edge cases from prose resolution criteria | The #1 source of disputes and losses. "Ceasefire" excludes energy-only deals, informal agreements, and humanitarian pauses. An agent that doesn't know this will misinterpret resolution risk. |
| **temporal_context** | Close date, resolution date, and a catalyst calendar of events that move price before resolution | Trading stops and payout are different dates. Between now and then, FOMC meetings, GDP releases, and diplomatic summits move prices. Agents that only know the end date miss the calendar. |
| **resolution_source** | Who determines the outcome and how | Kalshi uses centralized CFTC-regulated settlement. Polymarket uses UMA's optimistic oracle with a $750 dispute bond. The same event can resolve differently across platforms. |
| **cross_platform_link** | Equivalent markets on other platforms, with structural notes | Kalshi trades Fed rate decisions as per-meeting binaries. Polymarket trades them as year-end distributions. Same underlying event, completely different structure. A null value here is itself a signal — it means one platform has a coverage gap. |
| **related_markets** | Connected markets on the same platform with typed relationships | Ceasefire markets form temporal clusters (March, April, June, December) and parlays. The term structure between them implies a monthly hazard rate. Individual market prices don't tell you this. |

---

## Before and After

**Before** — what you get from the Polymarket API for a recession market:

```json
{
  "question": "US recession by end of 2026?",
  "price": 0.305,
  "volume": 632960
}
```

**After** — the same market enriched by ClearMarket:

```json
{
  "reference_id": "US-RECESSION-2026",
  "platform": "polymarket",
  "platform_market_id": "will-there-be-a-us-recession-in-2026",
  "question": "US recession by end of 2026?",
  "category": "macro",
  "price_snapshot": {
    "last_price": 0.305,
    "best_bid": 0.30,
    "best_ask": 0.31,
    "volume": 632960,
    "liquidity": 154204
  },
  "resolution_logic": {
    "summary": "Two consecutive quarters of negative real GDP, or NBER declaration",
    "triggers": [
      {
        "metric": "real_gdp_quarterly_change",
        "threshold": "< 0.0%",
        "consecutive": 2,
        "period": "Q2 2025 – Q4 2026",
        "source": "BEA advance estimate"
      },
      {
        "type": "announcement",
        "body": "NBER",
        "deadline": "BEA Q4 2026 advance estimate release"
      }
    ],
    "trigger_logic": "OR",
    "exclusions": [],
    "ambiguity_notes": "Uses advance estimates, which can be revised. First officially released value governs."
  },
  "temporal_context": {
    "closes": "2026-12-31",
    "resolves": "~2027-01-30",
    "catalyst_dates": [
      {"date": "2026-04-30", "event": "BEA Q1 2026 GDP advance estimate"},
      {"date": "2026-07-30", "event": "BEA Q2 2026 GDP advance estimate"},
      {"date": "2026-10-30", "event": "BEA Q3 2026 GDP advance estimate"}
    ],
    "days_to_resolution": 285
  },
  "resolution_source": {
    "name": "BEA + NBER",
    "type": "government_statistical_agency",
    "url": "https://bea.gov",
    "mechanism": "UMA optimistic oracle ($500 USDC dispute bond)"
  },
  "cross_platform_link": {
    "linked_platform": "kalshi",
    "linked_market_id": null,
    "match_confidence": null,
    "structural_notes": "Kalshi has no direct recession market. Nearest proxy: KXZERORATE-2026 (will rates hit zero?). $633K volume on Polymarket with no Kalshi equivalent — significant coverage gap."
  },
  "related_markets": [
    {
      "market_id": "fed-funds-rate-end-of-2026",
      "relationship_type": "causal_indicator",
      "notes": "Aggressive rate cuts would be consistent with recession scenario"
    }
  ]
}
```

Three fields became a complete analytical record. An agent can now programmatically check resolution triggers against real-time GDP data, know exactly when the next catalyst date is, understand that Kalshi has no equivalent market, and see which related markets to monitor.

---

## What ClearMarket Is Not

- **Not a unified API.** Dome (acquired by Polymarket), PolyRouter, and pmxt normalize access and order routing across platforms. ClearMarket consumes their outputs as inputs.
- **Not a trading platform.** No order execution, no portfolio management.
- **Not a price feed.** Price snapshots are included for context but are not real-time.
- **Not a latency play.** If your edge is speed, ClearMarket won't help. If your edge is understanding what you're trading, it will.

---

## Current Coverage

**v0.1** covers macro/economics and geopolitics — the categories with the highest institutional relevance and the most complex resolution criteria.

Enriched records are stored as individual JSON files in `markets/`.

| Category | Markets | Platforms |
|---|---|---|
| Monetary Policy (Fed) | FOMC rate decisions, chair nominations | Polymarket, Kalshi |
| Recession / GDP | US recession 2026 | Polymarket (Kalshi gap) |
| Geopolitics | Russia-Ukraine ceasefire cluster | Polymarket (Kalshi gap) |
| Trade / Tariffs | US-Canada, US-China tariff markets | Polymarket, Kalshi |

Schema definition: [`schema/clearmarket-schema.json`](schema/clearmarket-schema.json)

---

## Who This Is For

- **Bot and agent developers** trading across platforms who need structured resolution logic and cross-platform mapping. If you've been burned by resolution criteria you didn't fully parse, or missed that two "identical" markets on Kalshi and Polymarket have different triggers — this is for you.
- **Quantitative researchers** building models that incorporate prediction market signals alongside traditional data
- **Anyone evaluating prediction market data quality** — coverage gaps, resolution ambiguity, and structural differences across platforms are documented in the records themselves

Prediction market data is increasingly embedded in institutional infrastructure (ICE, Bloomberg Terminal, Tradeweb, Dow Jones). The analytical context around that data — resolution logic, structural mapping, accuracy tracking — doesn't exist yet. ClearMarket is building it.

---

## Roadmap

| Stage | Status |
|---|---|
| Schema definition + enriched records | **Current** |
| Automated enrichment pipeline | Next |
| API or MCP server (query enriched markets programmatically) | When demand warrants |
| Resolution outcome tracking + accuracy dataset | After 6 months of accumulated data — this becomes the moat |

---

## Contributing

ClearMarket is early-stage. If you trade prediction markets, build agents, or work with this data professionally, open an issue or reach out. The schema is the product — feedback on what's missing or wrong is more valuable than code contributions right now.

---

## License

MIT
