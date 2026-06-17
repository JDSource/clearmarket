---
signal_id: "CMSIG20260617BD02"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4% for year to Jun 2026: 23%; FRED at 4.3%"
semantic_title: "Market fades US CPI staying above 4% despite the live print"
telemetry: "23% · CPI inflation, year-over-year (FRED) 4.3%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-17T12:15:05+00:00"
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
  - "Kalshi traders price only a 23% chance CPI year-over-year exceeds 4% through June 2026."
  - "FRED CPI year-over-year currently reads 4.3%, already above the contract threshold."
  - "Market implies a high probability that inflation will fall back below 4% by the June resolution date."
  - "Resolves on BLS CPI release for June 2026, due mid-July 2026."
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
        retrieved_at: "2026-06-17T12:15:05+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.3%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-17T12:15:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With FRED CPI already at 4.3%, Kalshi traders are writing off a 77% chance the threshold remains breached at resolution, pricing in a notable near-term disinflation that the current official print does not support.
