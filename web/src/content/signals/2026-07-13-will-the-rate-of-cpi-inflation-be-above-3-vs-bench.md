---
signal_id: "CMSIG20260713BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.9%: 7%; actual CPI at 4.2%"
semantic_title: "Capital fades US inflation staying above 3.9%"
telemetry: "7% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-13T10:57:32+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will inflation in June 2026 be measured by year-over-year CPI?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.9"
  question_raw: "Will the rate of CPI inflation be above 3.9% for the year ending in June 2026?"
  current_price: 0.07
  volume_cumulative_usd: 14198.81
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "Kalshi prices only 7% probability that June 2026 CPI exceeds 3.9%."
  - "FRED CPI year-over-year currently reads 4.2%, already above the 3.9% threshold."
  - "Market implies inflation will fall back below 3.9%, contradicting the live print."
  - "Resolves against the official BLS June 2026 CPI year-over-year release."
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
        retrieved_at: "2026-07-13T10:57:32+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-13T10:57:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi traders assign just 7% odds to CPI remaining above 3.9% even though the current FRED reading is 4.2%, a stark disconnect suggesting the market is aggressively pricing in near-term disinflation that the official data has not yet validated.
