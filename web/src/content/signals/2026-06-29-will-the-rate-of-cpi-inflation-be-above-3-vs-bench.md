---
signal_id: "CMSIG20260629BD00"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.8%: 25%; FRED year-over-year at 4.2%"
semantic_title: "Traders heavily discount CPI staying above 3.8%"
telemetry: "25% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-29T01:48:14+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.25
  volume_cumulative_usd: 29888.81
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only a 25% chance CPI remains above 3.8% for the year ending June 2026."
  - "FRED CPI year-over-year currently reads 4.2%, already above the 3.8% threshold."
  - "Market implies strong conviction that inflation will drop below 3.8%, despite the live print sitting 40 basis points above it."
  - "Resolves against the official BLS CPI year-over-year release for June 2026."
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
        retrieved_at: "2026-06-29T01:48:14+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-06-29T01:48:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi traders assign only 25% odds to a threshold already exceeded by the current FRED print, implying the desk expects a sharp near-term disinflation that the live data does not yet support.
