---
signal_id: "CMSIG20260605BD22"
signal_slug: "will-the-fed-s-lower-bound-reach-2-75-or-vs-bench"
headline: "FFR lower bound at 2.75% before 2027: 5%; now at 3.75%"
semantic_title: "Lower bound to 2.75% lags sharply"
telemetry: "5% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T11:25:34+00:00"
event_id: "CM-EVT-RLQQ3VJDS6"
event_slug: "what-will-fed-rate-hit-before-2027"
event_question: "Will the Federal Reserve's policy rate reach or exceed a specific level before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2bb4294142c311763ca6be27ceffcef132f5ac8281f98a62abe02f6e6a8c0107"
  question_raw: "Will the Fed’s lower bound reach 2.75% or lower before 2027?"
  current_price: 0.053
  volume_cumulative_usd: 322919.9998519993
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 5% probability that the fed funds lower bound reaches 2.75% or below before 2027."
  - "FRED: fed funds upper bound currently 3.75 percent, implying lower bound near 3.5 percent."
  - "Market implies less than one-in-twenty odds of 75 bps or more in net cuts from here by year-end."
  - "Resolves on FRED lower-bound reading before January 2027."
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

With the lower bound roughly 75 bps above 2.75%, a 5% probability signals the market sees deep easing as nearly off the table for 2026, consistent with the dominant no-cut narrative across related contracts.
