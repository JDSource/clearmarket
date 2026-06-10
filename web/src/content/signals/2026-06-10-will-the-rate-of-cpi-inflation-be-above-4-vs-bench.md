---
signal_id: "CMSIG20260610BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4% May 2026: 99%; FRED print 3.9%"
semantic_title: "Capital fully backs CPI above 4% for the May 2026 year"
telemetry: "99% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-10T11:37:52+00:00"
event_id: "CM-EVT-5F0G9L6HV6"
event_slug: "kxcpiyoy-26may"
event_question: "CPI year-over-year, May 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26MAY-T4.0"
  question_raw: "Will the rate of CPI inflation be above 4.0% for the year ending in May 2026?"
  current_price: 0.99
  volume_cumulative_usd: 37236.05
  resolves_at: "2026-06-10T14:00:00Z"
bullets:
  - "Kalshi prices the May 2026 year-ending CPI above 4.0% at 99%."
  - "FRED CPI year-over-year is currently 3.9%, one-tenth below the threshold."
  - "Market assigns near-zero odds to inflation staying at or below 4%; the data has not confirmed the breach."
  - "Resolves against the official BLS CPI release for the 12 months ending May 2026."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from kalshi API; benchmark CPI inflation, year-over-year (FRED) = 3.9%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "kalshi_api"
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
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi's 99% price on CPI exceeding 4% for the May 2026 year leaves essentially no room for the benchmark to hold at its current 3.9%, making this the starkest threshold-drift of the batch, one data point separates the print from the level, yet the market treats it as done.
