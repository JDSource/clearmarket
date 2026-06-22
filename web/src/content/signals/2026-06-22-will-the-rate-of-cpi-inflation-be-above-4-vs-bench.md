---
signal_id: "CMSIG20260622BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4% June 2026: 23%; FRED CPI YoY at 4.3%"
semantic_title: "Capital fades US CPI staying above 4% through June 2026"
telemetry: "23% · CPI inflation, year-over-year (FRED) 4.3%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-22T13:33:31+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T4.0"
  question_raw: "Will the rate of CPI inflation be above 4.0% for the year ending in June 2026?"
  current_price: 0.23
  volume_cumulative_usd: 5999.69
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only a 23% chance CPI year-over-year exceeds 4% for the year ending June 2026."
  - "FRED currently shows CPI inflation at 4.3% year-over-year."
  - "Market discounts the live print, implying traders expect inflation to fall below 4% by resolution."
  - "Resolves against the BLS CPI June 2026 year-over-year release."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from kalshi API; benchmark CPI inflation, year-over-year (FRED) = 4.3%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "kalshi_api"
      benchmark_value:
        tier: "mediated"
        method: "CPI inflation, year-over-year (FRED)"
        source_url: "https://fred.stlouisfed.org/series/CPIAUCSL"
        retrieved_at: "2026-06-22T13:33:31+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.3%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-22T13:33:31+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi traders assign just 23% odds to CPI remaining above 4% even as FRED's current year-over-year reading sits at 4.3%, signalling the market is heavily fading the live print and pricing in a near-term drop below the threshold.
