---
signal_id: "CMSIG20260605BD28"
signal_slug: "will-the-fed-s-upper-bound-reach-5-25-or-vs-bench"
headline: "FFR upper bound at 5.25% before 2027: 3%; now at 3.75%"
semantic_title: "Upper bound to 5.25 percent detaches from 3.75 percent baseline"
telemetry: "3% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T11:25:34+00:00"
event_id: "CM-EVT-RLQQ3VJDS6"
event_slug: "what-will-fed-rate-hit-before-2027"
event_question: "Will the Federal Reserve's policy rate reach or exceed a specific level before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x728246cda497e10289a7145245675e2baece6561ba784760b0914108e6e42c04"
  question_raw: "Will the Fed’s upper bound reach 5.25% or higher before 2027?"
  current_price: 0.026
  volume_cumulative_usd: 141393.90288100002
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 3% probability that the fed funds upper bound reaches 5.25% or higher before 2027."
  - "FRED: fed funds upper bound currently 3.75 percent."
  - "Reaching 5.25% would require 150 bps of net hikes from current level within roughly six months."
  - "Resolves on FRED upper-bound reading before January 2027."
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

A 3% probability of a 150 bps net hiking cycle back to prior peak levels before year-end is consistent with market pricing elsewhere, but the gap between 3.75% today and 5.25% threshold underscores how aggressively restrictive a path the market is discounting.
