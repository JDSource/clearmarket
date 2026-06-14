---
signal_id: "CMSIG20260614BD02"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4% for year to Jun 2026: 23%; FRED at 4.3%"
semantic_title: "Market fades CPI staying above 4% despite the live print"
telemetry: "23% · CPI inflation, year-over-year (FRED) 4.3%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-14T10:48:43+00:00"
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
  - "Kalshi prices only a 23% chance CPI year-over-year exceeds 4% through June 2026."
  - "FRED's current CPI year-over-year reading is already 4.3%, above that threshold."
  - "Market is heavily discounting persistence of inflation above 4% even as it sits there now."
  - "Resolves on BLS CPI release for June 2026, due mid-July."
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
        retrieved_at: "2026-06-14T10:48:43+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.3%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-14T10:48:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI already printing 4.3% year-over-year, a 23% market price implies traders strongly expect a rapid disinflation over the remaining resolution window, a conviction the desk should weigh against current momentum in the data.
