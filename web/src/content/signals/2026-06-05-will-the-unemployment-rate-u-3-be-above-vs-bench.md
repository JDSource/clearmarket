---
signal_id: "CMSIG20260605BD07"
signal_slug: "will-the-unemployment-rate-u-3-be-above-vs-bench"
headline: "U-3 above 4.1% in May: 94%; FRED rate at 4.3%"
semantic_title: "Unemployment above 4.1 percent lags the FRED baseline already at 4.3"
telemetry: "94% · Unemployment rate (FRED) 4.3%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T12:04:45+00:00"
event_id: "CM-EVT-GX15VWGX92"
event_slug: "kxu3-26may"
event_question: "Unemployment rate (U-3), May 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26MAY-T4.1"
  question_raw: "Will the unemployment rate (U-3) be above 4.1% in May?"
  current_price: 0.94
  volume_cumulative_usd: 76612.51
  resolves_at: "2026-06-05T14:00:00Z"
bullets:
  - "Kalshi prices a 94% chance May U-3 unemployment exceeds 4.1%."
  - "Current FRED unemployment rate stands at 4.3%, already 20 bps above the threshold."
  - "Market underprices the gap, 4.3% current rate makes the 4.1% bar trivial to clear."
  - "Resolution on the May BLS release; any outcome at or above 4.2% resolves yes."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from kalshi API; benchmark Unemployment rate (FRED) = 4.3%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "kalshi_api"
      benchmark_value:
        tier: "mediated"
        method: "Unemployment rate (FRED)"
        source_url: "https://fred.stlouisfed.org/series/UNRATE"
        retrieved_at: "2026-06-05T12:04:45+00:00"
sources:
  - label: "Unemployment rate (FRED): 4.3%"
    url: "https://fred.stlouisfed.org/series/UNRATE"
    retrieved_at: "2026-06-05T12:04:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With the unemployment rate already printing 4.3% against a 4.1% bar, a 94% market price looks low rather than high, the benchmark is already well through the threshold, suggesting the market should be closer to 98-99% absent a dramatic single-month reversal of 20-plus basis points.
