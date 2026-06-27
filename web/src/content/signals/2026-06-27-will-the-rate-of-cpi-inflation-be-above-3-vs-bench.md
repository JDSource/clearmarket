---
signal_id: "CMSIG20260627BD00"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.8%: 23%; FRED year-over-year at 4.2%"
semantic_title: "Traders write off US CPI staying above 3.8%"
telemetry: "23% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-27T10:04:04+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.23
  volume_cumulative_usd: 26848.19
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only 23% chance CPI ends above 3.8% for the year ending June 2026."
  - "FRED CPI year-over-year currently sits at 4.2%, already above the 3.8% threshold."
  - "Market implies near-certain drop below 3.8% despite the live print clearing that bar."
  - "Resolves against the official June 2026 CPI year-over-year release."
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
        retrieved_at: "2026-06-27T10:04:04+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-06-27T10:04:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi traders are pricing heavy odds of a sub-3.8% print even though the current FRED reading is 4.2%, a 420-basis-point gap between the live benchmark and what the market is willing to back.
