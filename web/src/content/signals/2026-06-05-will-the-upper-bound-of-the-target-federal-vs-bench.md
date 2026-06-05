---
signal_id: "CMSIG20260605BD10"
signal_slug: "will-the-upper-bound-of-the-target-federal-vs-bench"
headline: "FFR upper bound above 4.5% end-2026: 3%; now at 3.75%"
semantic_title: "Rate hike path to 4.5% detaches"
telemetry: "3% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T11:25:34+00:00"
event_id: "CM-EVT-WB85BV4T72"
event_slug: "what-will-the-fed-rate-be-at-the-end-of-2026"
event_question: "Will the upper bound of the target federal funds rate be ≥ 4.5% at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3d20f26deb9b9cc7e24e5e06c10234a722d93bac095ce1105c59b44b503078d7"
  question_raw: "Will the upper bound of the target federal funds rate be ≥ 4.5% at the end of 2026?"
  current_price: 0.029
  volume_cumulative_usd: 2398390.2824210026
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "Polymarket prices only a 3% chance the fed funds upper bound reaches 4.5% or higher by end-2026."
  - "FRED: fed funds upper bound currently 3.75 percent."
  - "Market implies a near-zero probability of a 75 bps net hike from current level."
  - "Resolves on FRED year-end reading."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from polymarket API; benchmark Fed funds target rate, upper bound (FRED) = 3.75%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "polymarket_api"
      benchmark_value:
        tier: "mediated"
        method: "Fed funds target rate, upper bound (FRED)"
        source_url: "https://fred.stlouisfed.org/series/DFEDTARU"
        retrieved_at: "2026-06-05T11:25:34+00:00"
sources:
  - label: "Fed funds target rate, upper bound (FRED): 3.75%"
    url: "https://fred.stlouisfed.org/series/DFEDTARU"
    retrieved_at: "2026-06-05T11:25:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With the rate at 3.75%, a 3% probability of reaching 4.5% implies the market sees hiking back toward prior cycle highs as nearly impossible, consistent with an easing bias but worth flagging given the 39% hike probability priced elsewhere.
