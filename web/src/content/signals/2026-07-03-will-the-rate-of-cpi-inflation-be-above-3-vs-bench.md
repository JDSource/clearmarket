---
signal_id: "CMSIG20260703BD00"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.9%: 18%; year-over-year at 4.2%"
semantic_title: "Traders heavily discount US inflation staying above 3.9%"
telemetry: "18% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-03T10:33:33+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.9"
  question_raw: "Will the rate of CPI inflation be above 3.9% for the year ending in June 2026?"
  current_price: 0.18
  volume_cumulative_usd: 23829.53
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only an 18% chance CPI ends June 2026 above 3.9%."
  - "FRED year-over-year CPI currently reads 4.2%, already above that threshold."
  - "Market implies inflation will fall back below 3.9% despite the current print exceeding it."
  - "Resolves against the June 2026 CPI year-over-year release."
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
        retrieved_at: "2026-07-03T10:33:33+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-03T10:33:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI already printing at 4.2% year-over-year, Kalshi traders pricing only 18% odds of staying above 3.9% represents a strong conviction that inflation will decelerate sharply into June, a notable departure from the current official FRED reading.
