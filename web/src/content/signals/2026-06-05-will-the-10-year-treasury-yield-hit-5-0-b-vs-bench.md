---
signal_id: "CMSIG20260605BD09"
signal_slug: "will-the-10-year-treasury-yield-hit-5-0-b-vs-bench"
headline: "10-yr yield hits 5% before 2027: 15%; now at 4.49%"
semantic_title: "Ten-year yield at 5% detaches from the FRED baseline"
telemetry: "15% · 10-year Treasury yield (FRED) 4.49%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T12:04:45+00:00"
event_id: "CM-EVT-4F238D6VR7"
event_slug: "how-high-will-10-year-treasury-yield-go-before-2027"
event_question: "Will the 10-year Treasury yield reach a specific high point before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0e159c0d672526d1d65f524b1c512185924aac8f781b6c68549c2a17dec953e0"
  question_raw: "Will the 10-year Treasury yield hit 5.0% before 2027?"
  current_price: 0.15
  volume_cumulative_usd: 57494.576053000004
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 15% chance the 10-year Treasury yield reaches 5.0% before end-2026."
  - "Current FRED 10-year yield stands at 4.49%, roughly 51 bps below the 5% threshold."
  - "Market assigns meaningful but modest odds of a 51 bps surge in roughly seven months."
  - "Resolution requires any intraday or closing print at or above 5.00% before January 2027."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from polymarket API; benchmark 10-year Treasury yield (FRED) = 4.49%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "polymarket_api"
      benchmark_value:
        tier: "mediated"
        method: "10-year Treasury yield (FRED)"
        source_url: "https://fred.stlouisfed.org/series/DGS10"
        retrieved_at: "2026-06-05T12:04:45+00:00"
sources:
  - label: "10-year Treasury yield (FRED): 4.49%"
    url: "https://fred.stlouisfed.org/series/DGS10"
    retrieved_at: "2026-06-05T12:04:45+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With the 10-year at 4.49%, a 15% probability of touching 5.0% within seven months implies the market sees a non-trivial tail risk of a significant yield spike, but the gap of over 50 bps makes the 15% read appear reasonably calibrated, worth flagging as the benchmark is close enough that the drift is modest but directionally notable.
