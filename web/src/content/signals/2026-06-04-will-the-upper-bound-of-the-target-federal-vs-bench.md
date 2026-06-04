---
signal_id: "CMSIG20260604BD10"
signal_slug: "will-the-upper-bound-of-the-target-federal-vs-bench"
headline: "FFR ≥4.5% End-2026: 3%; rate at 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-04T03:25:24+00:00"
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
  - "Polymarket prices only 3% chance fed funds upper bound reaches 4.5% by end-2026."
  - "FRED benchmark: fed funds upper bound currently 3.75%, already 75 bps below the 4.5% threshold."
  - "Market implies near-zero probability of a net hike cycle, despite rate sitting just 75 bps away."
  - "Resolves on FRED fed funds upper bound at 2026 year-end."
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
        retrieved_at: "2026-06-04T03:25:24+00:00"
sources:
  - label: "Fed funds target rate, upper bound (FRED): 3.75%"
    url: "https://fred.stlouisfed.org/series/DFEDTARU"
    retrieved_at: "2026-06-04T03:25:24+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With the upper bound at 3.75%, only a 75 bps net hike is needed to breach 4.5%, yet Polymarket assigns just 3%, suggesting the desk sees hikes as structurally off the table.
