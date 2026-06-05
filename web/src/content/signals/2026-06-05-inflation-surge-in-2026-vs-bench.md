---
signal_id: "CMSIG20260605BD25"
signal_slug: "inflation-surge-in-2026-vs-bench"
headline: "Inflation surge in 2026: 97%; CPI currently at 3.9%"
semantic_title: "Inflation surge pricing challenges CPI benchmark at 3.9 percent"
telemetry: "97% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T11:25:34+00:00"
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
  - "Kalshi prices a 97% probability of an inflation surge occurring in 2026."
  - "FRED: CPI year-over-year currently 3.9 percent."
  - "Near-full pricing of a surge implies the market sees current 3.9% as a floor, not a peak."
  - "Resolves against Kalshi's surge definition benchmark."
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
        retrieved_at: "2026-06-05T11:25:34+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-05T11:25:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 97%, Kalshi effectively treats an inflation surge as a done deal while CPI sits at 3.9%, the market is pricing the current level as the launching pad for further acceleration rather than a cyclical peak.
