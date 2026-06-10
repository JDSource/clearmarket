---
signal_id: "CMSIG20260610BD00"
signal_slug: "will-inflation-reach-more-than-4-in-2026-vs-bench"
headline: "Inflation above 4% in 2026: 98%; CPI now 3.9%"
semantic_title: "Traders pile into US inflation breaking above 4%"
telemetry: "98% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-10T11:37:52+00:00"
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
  - "Polymarket prices a greater-than-4% CPI print in 2026 at 98%."
  - "FRED CPI year-over-year currently sits at 3.9%, just below the threshold."
  - "Market implies near-certainty of a breach; official data shows inflation one-tenth of a point away."
  - "Resolves if any 2026 monthly CPI print exceeds 4% year-over-year."
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
        retrieved_at: "2026-06-10T11:37:52+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-10T11:37:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI at 3.9%, Polymarket's 98% price implies the market treats a move above 4% as virtually guaranteed, leaving almost no premium for the threshold holding, a meaningful overreach given how close the benchmark sits to but still below the line.
