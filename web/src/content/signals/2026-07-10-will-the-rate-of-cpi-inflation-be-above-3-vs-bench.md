---
signal_id: "CMSIG20260710BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.8%: 24%; current reading 4.2%"
semantic_title: "Capital fades a CPI break above 3.8% despite a 4.2% print"
telemetry: "24% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-10T10:51:13+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will inflation in June 2026 be measured by year-over-year CPI?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.24
  volume_cumulative_usd: 41663.01
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "Kalshi prices only a 24% chance CPI exceeds 3.8% for the year ending June 2026."
  - "FRED CPI year-over-year currently stands at 4.2%, already above the 3.8% threshold."
  - "Market implies inflation will fall back below 3.8% despite the live print sitting 40 basis points above it."
  - "Resolves against the June 2026 CPI year-over-year release from BLS via FRED."
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
        retrieved_at: "2026-07-10T10:51:13+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-10T10:51:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI already printing 4.2%, traders assigning only 24% odds to a reading above 3.8% implies the desk expects a sharp near-term disinflation that the current data does not yet support.
