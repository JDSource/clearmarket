---
signal_id: "CMSIG20260604BD25"
signal_slug: "inflation-surge-in-2026-vs-bench"
headline: "Kalshi Inflation Surge 2026: 97%; CPI at 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-04T03:25:24+00:00"
event_id: "CM-EVT-H50NT0MZ04"
event_slug: "kxlcpimaxyoy-27"
event_question: "CPI year-over-year maximum, February 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLCPIMAXYOY-27-P4"
  question_raw: "Inflation surge in 2026?"
  current_price: 0.973
  volume_cumulative_usd: 186657.73
  resolves_at: "2027-02-14T15:00:00Z"
bullets:
  - "Kalshi prices 97% probability of an inflation surge in 2026."
  - "FRED benchmark: CPI year-over-year currently 3.9%."
  - "Market nearly certain of a surge; definition likely implies a threshold above current 3.9% reading."
  - "Resolves per Kalshi's inflation-surge contract definition against official CPI data."
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
        retrieved_at: "2026-06-04T03:25:24+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-04T03:25:24+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 3.9% CPI, a 97% surge probability implies the market defines the trigger at or just above current levels, making this nearly tautological, the desk should verify Kalshi's exact threshold to assess true drift.
