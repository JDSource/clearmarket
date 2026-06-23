---
signal_id: "CMSIG20260623BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4% June 2026: 23%; FRED CPI at 4.3%"
semantic_title: "Capital fades US CPI staying above 4% despite the live print"
telemetry: "23% · CPI inflation, year-over-year (FRED) 4.3%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-23T11:00:46+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T4.0"
  question_raw: "Will the rate of CPI inflation be above 4.0% for the year ending in June 2026?"
  current_price: 0.23
  volume_cumulative_usd: 5999.69
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only a 23% chance CPI inflation exceeds 4.0% for the year ending June 2026."
  - "FRED CPI year-over-year currently reads 4.3%, already above the threshold."
  - "Market heavily discounts the current print, implying traders expect a rapid drop below 4% by resolution."
  - "Resolves on the BLS CPI release for June 2026."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from kalshi API; benchmark CPI inflation, year-over-year (FRED) = 4.3%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "kalshi_api"
      benchmark_value:
        tier: "mediated"
        method: "CPI inflation, year-over-year (FRED)"
        source_url: "https://fred.stlouisfed.org/series/CPIAUCSL"
        retrieved_at: "2026-06-23T11:00:46+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.3%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-23T11:00:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI already printing at 4.3% above the 4.0% threshold, Kalshi's 23% price is a strong fade of the current official data, implying traders expect a significant disinflation move before the June 2026 measurement.
