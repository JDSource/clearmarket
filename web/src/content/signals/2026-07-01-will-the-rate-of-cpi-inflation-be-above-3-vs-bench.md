---
signal_id: "CMSIG20260701BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.9%: 15%; year-over-year now at 4.2%"
semantic_title: "Capital discounts US inflation staying above 3.9%"
telemetry: "15% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-01T11:22:48+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.9"
  question_raw: "Will the rate of CPI inflation be above 3.9% for the year ending in June 2026?"
  current_price: 0.15
  volume_cumulative_usd: 18863.11
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only 15% odds that CPI inflation exceeds 3.9% for the year ending June 2026."
  - "FRED CPI year-over-year currently sits at 4.2%, already above the 3.9% threshold in question."
  - "Market implies near-certain collapse below 3.9% despite the live print clearing that bar by 30 basis points."
  - "Resolves against the June 2026 CPI year-over-year release from BLS."
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
        retrieved_at: "2026-07-01T11:22:48+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-01T11:22:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI currently printing 4.2% year-over-year, Kalshi traders pricing only 15% for above 3.9% implies the desk sees an imminent and steep disinflationary move as the near-certain base case, a strong fade of the current official data.
