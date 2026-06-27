---
signal_id: "CMSIG20260627BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4%: 5%; current print at 4.2%"
semantic_title: "Capital fades US inflation staying above 4%"
telemetry: "5% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-27T01:37:20+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T4.0"
  question_raw: "Will the rate of CPI inflation be above 4.0% for the year ending in June 2026?"
  current_price: 0.05
  volume_cumulative_usd: 7499.14
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only 5% chance CPI remains above 4% for the year ending June 2026."
  - "FRED CPI year-over-year currently sits at 4.2%, already above the 4% threshold."
  - "Market implies near-certain cooling below 4% despite the live print exceeding that level."
  - "Resolves against the June 2026 CPI year-over-year release from BLS/FRED."
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
        retrieved_at: "2026-06-27T01:37:20+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-06-27T01:37:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI already printing 4.2% year-over-year, Kalshi traders are pricing only a 5% chance of a sub-month resolution above 4%, implying the desk sees a sharp imminent drop in the June print as near-certain, a strong bearish inflation conviction the current FRED data does not yet support.
