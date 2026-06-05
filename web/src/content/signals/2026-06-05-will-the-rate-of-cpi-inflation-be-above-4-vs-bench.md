---
signal_id: "CMSIG20260605BD14"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4% May YoY: 99%; FRED currently 3.9%"
semantic_title: "CPI above 4% for May gaps sharply from the FRED print"
telemetry: "99% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T12:04:45+00:00"
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
  - "Kalshi prices 99% probability that May 2026 CPI YoY exceeds 4.0%."
  - "Current FRED CPI YoY reads 3.9%, sitting just one tenth below the resolution threshold."
  - "Near-certain pricing implies market expects the May print to cross above 4.0% with virtual certainty."
  - "Resolution on the May BLS CPI release; a single-tenth uptick resolves the contract yes."
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
        retrieved_at: "2026-06-05T12:04:45+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-05T12:04:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 99% for a threshold that is currently 10 bps away, Kalshi pricing implies the desk is treating the May CPI cross above 4% as essentially locked in, a meaningful overextension relative to a benchmark that sits only a rounding error below the trigger, leaving almost no probability weight for a flat or lower May print.
