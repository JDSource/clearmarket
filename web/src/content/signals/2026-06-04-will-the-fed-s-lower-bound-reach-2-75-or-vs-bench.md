---
signal_id: "CMSIG20260604BD22"
signal_slug: "will-the-fed-s-lower-bound-reach-2-75-or-vs-bench"
headline: "FFR Lower Bound ≤2.75% Before 2027: 5%; at 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-04T03:25:24+00:00"
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
  - "Polymarket prices 5% chance the fed funds lower bound hits 2.75% or below before 2027."
  - "FRED benchmark: fed funds upper bound currently 3.75%, implying lower bound near 3.5%."
  - "Market implies at least 75 bps of cuts would be needed; 5% probability looks tight given easing bias elsewhere."
  - "Resolves if FRED lower bound prints ≤2.75% at any point before Jan 2027."
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

With the lower bound near 3.5% and other markets pricing meaningful cut probability in 2026, the 5% on reaching 2.75% looks low relative to the implied cumulative-cut distribution.
