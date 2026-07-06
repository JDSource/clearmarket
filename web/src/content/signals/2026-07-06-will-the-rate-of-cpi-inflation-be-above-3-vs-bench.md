---
signal_id: "CMSIG20260706BD00"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.8%: 23%; FRED year-over-year at 4.2%"
semantic_title: "Traders write off US CPI holding above 3.8%"
telemetry: "23% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-06T12:01:35+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.23
  volume_cumulative_usd: 35936.77
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only a 23% chance CPI stays above 3.8% for the year ending June 2026."
  - "FRED currently shows CPI year-over-year at 4.2%, already above the 3.8% threshold."
  - "Market implies a steep near-term drop in inflation that official data has not yet confirmed."
  - "Resolves against the June 2026 CPI year-over-year print from BLS via FRED."
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
        retrieved_at: "2026-07-06T12:01:35+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-06T12:01:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI already printing at 4.2% on FRED, a 23% market price on the threshold being breached implies Kalshi traders are aggressively pricing in a rapid disinflation that has no current support in the official data.
