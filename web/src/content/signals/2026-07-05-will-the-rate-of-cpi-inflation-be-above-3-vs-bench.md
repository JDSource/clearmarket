---
signal_id: "CMSIG20260705BD00"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.8%: 22%; FRED y/y at 4.2%"
semantic_title: "Traders write off US inflation staying above 3.8%"
telemetry: "22% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-05T10:09:12+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.22
  volume_cumulative_usd: 33337.21
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only a 22% chance CPI ends June 2026 above 3.8%."
  - "FRED CPI year-over-year currently sits at 4.2%, already above that threshold."
  - "Market implies inflation will fall below 3.8% despite current reading being above it."
  - "Resolves on the June 2026 CPI year-over-year print."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from kalshi API; benchmark CPI inflation, year-over-year (FRED) = 4.2%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "kalshi_api"
      benchmark_value:
        tier: "mediated"
        method: "CPI inflation, year-over-year (FRED)"
        source_url: "https://fred.stlouisfed.org/series/CPIAUCNS"
        retrieved_at: "2026-07-05T10:09:12+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-05T10:09:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi traders assign only 22% probability to CPI remaining above 3.8% for the year ending June 2026, while FRED already shows CPI at 4.2%, a sharp discount of the current official reading that implies the desk expects significant near-term disinflation.
