---
signal_id: "CMSIG20260603BD25"
signal_slug: "will-inflation-reach-more-than-4-in-2026-vs-bench"
headline: "Inflation >4% in 2026: 98%; CPI currently 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-03T01:45:00+00:00"
event_id: "CM-EVT-NN523F6SZ3"
event_slug: "how-high-will-inflation-get-in-2026"
event_question: "US inflation rate, 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1f61db83c47fc787f44997af53d517cc4775e813b169d0b8ae2ad3bff316d052"
  question_raw: "Will inflation reach more than 4% in 2026?"
  current_price: 0.976
  volume_cumulative_usd: 241813.010416998
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 98% chance CPI inflation exceeds 4% in 2026."
  - "CPI year-over-year (FRED) currently stands at 3.9%."
  - "Market implies near-certainty that CPI breaches 4%, yet it is only 10bps below that threshold now."
  - "Resolves when any 2026 monthly CPI print is reported above 4% YoY."
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
        retrieved_at: "2026-06-03T01:45:00+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-03T01:45:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI at 3.9% and the contract at 98%, the market is pricing a near-certain breach of the 4% threshold, which is only 10bps away, the high confidence is directionally defensible but the 98% price leaves almost no room for a modest disinflation scenario.
