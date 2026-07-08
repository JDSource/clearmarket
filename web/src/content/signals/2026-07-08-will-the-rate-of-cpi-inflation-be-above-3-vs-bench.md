---
signal_id: "CMSIG20260708BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.9% June 2026: 5%; actual at 4.2%"
semantic_title: "Capital writes off CPI staying above 3.9% despite the live print"
telemetry: "5% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-08T10:15:34+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will inflation in June 2026 be measured by year-over-year CPI?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.9"
  question_raw: "Will the rate of CPI inflation be above 3.9% for the year ending in June 2026?"
  current_price: 0.05
  volume_cumulative_usd: 7903.71
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "Kalshi prices only a 5% chance CPI ends June 2026 above 3.9%."
  - "FRED CPI year-over-year currently reads 4.2%, already above that threshold."
  - "Market implies inflation will fall below 3.9% before the June 2026 resolution date, contradicting today's live print."
  - "Resolves against FRED CPI year-over-year for the period ending June 2026."
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
        retrieved_at: "2026-07-08T10:15:34+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-08T10:15:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI already printing 4.2% year-over-year, a 5% market price for 'above 3.9%' implies traders are heavily discounting a sharp near-term disinflation that has not yet appeared in the official data.
