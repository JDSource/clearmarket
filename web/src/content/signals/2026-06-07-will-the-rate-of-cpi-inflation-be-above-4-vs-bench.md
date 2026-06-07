---
signal_id: "CMSIG20260607BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4% May yr-end: 99%; FRED print 3.9%"
semantic_title: "Capital backs CPI topping 4% for the May 2026 year"
telemetry: "99% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-07T10:27:21+00:00"
event_id: "CM-EVT-5F0G9L6HV6"
event_slug: "kxcpiyoy-26may"
event_question: "CPI year-over-year, May 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26MAY-T4.0"
  question_raw: "Will the rate of CPI inflation be above 4.0% for the year ending in May 2026?"
  current_price: 0.99
  volume_cumulative_usd: 37236.05
  resolves_at: "2026-06-10T14:00:00Z"
bullets:
  - "Kalshi prices a 99% probability that the 12-month CPI ending May 2026 exceeds 4.0%."
  - "FRED CPI year-over-year is currently 3.9%, below the 4.0% contract threshold."
  - "A 99% price implies near-certainty, yet the official benchmark has not cleared the bar."
  - "May 2026 CPI release will resolve this contract; data is imminent given today's date."
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
        retrieved_at: "2026-06-07T10:27:21+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-07T10:27:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi has essentially fully priced a 4%+ CPI print for the May 2026 annual period while the current FRED reading of 3.9% has not yet crossed that line, a striking divergence given the contract resolves on forthcoming data.
