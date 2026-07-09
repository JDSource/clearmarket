---
signal_id: "CMSIG20260709BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-3-vs-bench"
headline: "CPI above 3.8%: 21%; year-over-year at 4.2%"
semantic_title: "Capital fades US inflation staying above 3.8%"
telemetry: "21% · CPI inflation, year-over-year (FRED) 4.2%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-07-09T10:58:02+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will inflation in June 2026 be measured by year-over-year CPI?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.21
  volume_cumulative_usd: 35455.01
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "Kalshi prices only 21% odds that CPI inflation exceeds 3.8% for the year ending June 2026."
  - "FRED CPI year-over-year currently sits at 4.2%, already above the 3.8% threshold."
  - "Market implies an aggressive drop below 3.8% is likely, despite the live print being 40 basis points above it."
  - "Resolves on the June 2026 CPI year-over-year release."
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
        retrieved_at: "2026-07-09T10:58:02+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 4.2%"
    url: "https://fred.stlouisfed.org/series/CPIAUCNS"
    retrieved_at: "2026-07-09T10:58:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI currently printing 4.2%, Kalshi traders pricing only 21% for above 3.8% implies the desk expects a sharp near-term disinflationary move that the current data does not yet support.
