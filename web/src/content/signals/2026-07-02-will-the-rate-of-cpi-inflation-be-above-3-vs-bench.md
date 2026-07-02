---
signal_id: "CMSIG20260702BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.9%: 16%; current CPI at 4.2%"
semantic_title: "Capital fades US inflation holding above 3.9%"
telemetry: "16% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-02T10:35:57+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will the year-over-year Consumer Price Index inflation rate in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.9"
  question_raw: "Will the rate of CPI inflation be above 3.9% for the year ending in June 2026?"
  current_price: 0.16
  volume_cumulative_usd: 20506.79
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices only a 16% chance CPI exceeds 3.9% for the year ending June 2026."
  - "FRED CPI year-over-year is currently 4.2%, already above the 3.9% threshold."
  - "Market implies a sharp near-term drop in inflation that the current print does not support."
  - "Resolves against the official BLS CPI release for June 2026."
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
        retrieved_at: "2026-07-02T10:35:57+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-02T10:35:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI already printing at 4.2%, Kalshi's 16% probability for a above-3.9% outcome implies traders expect a dramatic and rapid disinflation that the current data does not yet validate, a meaningful divergence warranting scrutiny on resolution mechanics or question framing.
