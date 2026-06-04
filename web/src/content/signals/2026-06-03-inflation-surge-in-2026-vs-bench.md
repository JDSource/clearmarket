---
signal_id: "CMSIG20260603BD26"
signal_slug: "inflation-surge-in-2026-vs-bench"
headline: "Kalshi inflation surge 2026: 98%; CPI at 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-03T01:45:00+00:00"
event_id: "CM-EVT-H50NT0MZ04"
event_slug: "kxlcpimaxyoy-27"
event_question: "CPI year-over-year maximum, February 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLCPIMAXYOY-27-P4"
  question_raw: "Inflation surge in 2026?"
  current_price: 0.979
  volume_cumulative_usd: 180919.04
  resolves_at: "2027-02-14T15:00:00Z"
bullets:
  - "Kalshi prices 98% probability of an inflation surge in 2026."
  - "CPI year-over-year (FRED) currently at 3.9%."
  - "Near-certainty pricing with CPI already close to typical 'surge' thresholds."
  - "Resolves against CPI benchmark for 2026."
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
        retrieved_at: "2026-06-03T01:45:00+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-03T01:45:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi's 98% 'inflation surge' price with CPI already at 3.9% suggests the market believes a further acceleration is essentially guaranteed, leaving almost zero probability mass for stabilization or retreat, a notable skew worth flagging to an inflation desk.
