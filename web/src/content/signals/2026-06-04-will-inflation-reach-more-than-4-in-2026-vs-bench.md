---
signal_id: "CMSIG20260604BD24"
signal_slug: "will-inflation-reach-more-than-4-in-2026-vs-bench"
headline: "US CPI >4% in 2026: 98%; CPI now 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-04T03:25:24+00:00"
event_id: "CM-EVT-NN523F6SZ3"
event_slug: "how-high-will-inflation-get-in-2026"
event_question: "US inflation rate, 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1f61db83c47fc787f44997af53d517cc4775e813b169d0b8ae2ad3bff316d052"
  question_raw: "Will inflation reach more than 4% in 2026?"
  current_price: 0.978
  volume_cumulative_usd: 247436.1943099977
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 98% chance CPI inflation exceeds 4% at some point in 2026."
  - "FRED benchmark: CPI year-over-year currently 3.9%, just 10 bps below the 4% threshold."
  - "Market is near-certain of a breach; the current reading is barely below the trigger level."
  - "Resolves when any official CPI YoY print exceeds 4% during 2026."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from polymarket API; benchmark CPI inflation, year-over-year (FRED) = 3.9%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "polymarket_api"
      benchmark_value:
        tier: "mediated"
        method: "CPI inflation, year-over-year (FRED)"
        source_url: "https://fred.stlouisfed.org/series/CPIAUCSL"
        retrieved_at: "2026-06-04T03:25:24+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-04T03:25:24+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

CPI sitting at 3.9% makes 98% plausible on its face, but any mean-reversion or tariff impact stalling would defeat the contract, the market is priced for near-certain upside breach with minimal margin.
