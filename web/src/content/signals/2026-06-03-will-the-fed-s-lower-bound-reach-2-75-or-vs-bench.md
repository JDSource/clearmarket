---
signal_id: "CMSIG20260603BD23"
signal_slug: "will-the-fed-s-lower-bound-reach-2-75-or-vs-bench"
headline: "Fed lower bound ≤2.75% before 2027: 6%; rate at 3.75%"
semantic_title: "Fed lower bound at 2.75 percent trails well behind FRED rate"
telemetry: "6% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-03T01:45:00+00:00"
event_id: "CM-EVT-RLQQ3VJDS6"
event_slug: "what-will-fed-rate-hit-before-2027"
event_question: "Will the Federal Reserve's policy rate reach or exceed a specific level before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2bb4294142c311763ca6be27ceffcef132f5ac8281f98a62abe02f6e6a8c0107"
  question_raw: "Will the Fed’s lower bound reach 2.75% or lower before 2027?"
  current_price: 0.063
  volume_cumulative_usd: 309024.4398519993
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 6% chance the Fed lower bound reaches 2.75% or below before 2027."
  - "Fed funds upper bound (FRED) currently 3.75%, implying lower bound near 3.5%."
  - "Market implies cuts of 75bps+ from current lower bound are very unlikely before year-end."
  - "Resolves on FRED Fed funds lower bound before January 2027."
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
        retrieved_at: "2026-06-03T01:45:00+00:00"
sources:
  - label: "Fed funds target rate, upper bound (FRED): 3.75%"
    url: "https://fred.stlouisfed.org/series/DFEDTARU"
    retrieved_at: "2026-06-03T01:45:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With the lower bound currently around 3.5%, a 6% probability for reaching ≤2.75% implies traders see fewer than three 25bps cuts as highly probable, yet the 67% 'no cuts' pricing on Polymarket (candidate 3) creates internal tension about the distribution of cut scenarios.
