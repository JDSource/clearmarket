# ClearMarket

**Structured intelligence for prediction markets.**

Platforms give you prices. ClearMarket gives you what the prices actually mean.

Raw feeds from Polymarket and Kalshi contain almost no information about resolution rules, catalyst events, cross-platform differences, or related markets. ClearMarket adds the missing intelligence layer so agents and institutions can trade with understanding instead of blind price signals.

---

## The Problem

A typical raw API response looks like this:

```json
{
  "slug": "russia-x-ukraine-ceasefire-before-2027",
  "price": 0.375,
  "volume": 11771072,
  "end_date": "2026-12-31"
}
```

No triggers, no exclusions, no catalyst calendar, no cross-platform equivalents, no relationships to other ceasefire markets. Agents are flying blind.

---

## What ClearMarket Adds

Five fields that don't exist anywhere else:

| Field | What it gives you | Why it matters |
|---|---|---|
| `resolution_logic` | Parsed triggers, exclusions, edge cases | The #1 source of disputes and losses |
| `temporal_context` | Close date, resolution date, `catalyst_dates[]` | Know exactly which real-world events move price before resolution |
| `resolution_source` | Who decides + mechanism (UMA vs CFTC) | Same event can resolve differently across platforms |
| `cross_platform_link` | Same question on a **different platform** (e.g., Polymarket vs Kalshi) | Maps how the same event is structured differently across platforms, or flags when only one platform covers it |
| `related_markets` | Connected markets on the **same platform** (e.g., March/April/June ceasefire variants) | Surfaces term structure, parlays, and causal relationships between related contracts |

---

## Before vs After (Real Example)

**Raw Polymarket API** (recession market) — 4 basic fields:

```json
{
  "question": "US recession by end of 2026?",
  "price": 0.305,
  "volume": 632960
}
```

**ClearMarket enriched record** — 10 structured fields including parsed GDP triggers, BEA catalyst dates, Kalshi coverage gap, and causal links to Fed-rate markets:

```json
{
  "reference_id": "US-RECESSION-2026",
  "platform": "polymarket",
  "platform_market_id": "will-there-be-a-us-recession-in-2026",
  "question": "US recession by end of 2026?",
  "category": "macro",
  "price_snapshot": {
    "yes": {
      "last_price": 0.305,
      "best_bid": 0.30,
      "best_ask": 0.31
    },
    "no": {
      "last_price": 0.695,
      "best_bid": 0.69,
      "best_ask": 0.70
    },
    "implied_probability": {
      "yes": 0.305,
      "no": 0.695
    },
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

(See `markets/` for enriched records.)

---

## What ClearMarket Is Not

- **Not a unified API.** Dome (acquired by Polymarket), PolyRouter, and pmxt normalize access and order routing. ClearMarket consumes those outputs as inputs.
- **Not a trading platform.** No order execution, no portfolio management.
- **Not a price feed.** Price snapshots are included for context but are not real-time.
- **Not a latency play.** If your edge is speed, this won't help. If your edge is understanding what you're trading, it will.

---

## Current Coverage

**v0.1** covers macro/economics and geopolitics — the categories with the highest institutional relevance and the most complex resolution criteria.

| Category | Markets | Platforms |
|---|---|---|
| Monetary Policy (Fed) | FOMC rate decisions, chair nominations | Polymarket, Kalshi |
| Recession / GDP | US recession 2026 | Polymarket (Kalshi gap) |
| Geopolitics | Russia-Ukraine ceasefire cluster | Polymarket (Kalshi gap) |
| Trade / Tariffs | US-Canada, US-China tariff markets | Polymarket, Kalshi |

Schema: [`schema/clearmarket-schema.json`](schema/clearmarket-schema.json)

---

## Who This Is For

- **Bot and agent developers** who need machine-readable resolution logic and cross-platform mapping
- **Quantitative researchers** incorporating prediction market signals into models
- **Institutions evaluating prediction market data quality** and coverage gaps

Prediction market data is increasingly embedded in institutional infrastructure (ICE, Bloomberg Terminal, Tradeweb, Dow Jones). The analytical context around that data doesn't exist yet.

---

## Roadmap

| Stage | Status |
|---|---|
| Schema definition + enriched records | **Current** |
| Automated enrichment pipeline | Next |
| API or MCP server | When demand warrants |
| Resolution outcome tracking + accuracy dataset | After 6 months of data — this becomes the moat |

---

## Contributing

Early stage. Feedback on the schema and missing fields is more valuable than code contributions right now. Open an issue or reach out.

---

## License

MIT
