---
signal_id: "CMSIG20260603BD10"
signal_slug: "will-the-upper-bound-of-the-target-federal-vs-bench"
headline: "Fed upper bound ≥4.5% by end-2026: 4%; rate at 3.75%"
semantic_title: "Fed funds at 4.5 percent end-2026 lags far below FRED rate"
telemetry: "4% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-03T01:45:00+00:00"
event_id: "CM-EVT-WB85BV4T72"
event_slug: "what-will-the-fed-rate-be-at-the-end-of-2026"
event_question: "Will the upper bound of the target federal funds rate be ≥ 4.5% at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3d20f26deb9b9cc7e24e5e06c10234a722d93bac095ce1105c59b44b503078d7"
  question_raw: "Will the upper bound of the target federal funds rate be ≥ 4.5% at the end of 2026?"
  current_price: 0.038
  volume_cumulative_usd: 2397984.3537230026
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "Polymarket prices only 4% chance the upper bound ends 2026 at ≥4.5%."
  - "Fed funds upper bound (FRED) currently sits at 3.75%."
  - "Market implies near-zero probability of a 75bps+ net hike from current level by year-end."
  - "Resolves on FRED Fed funds upper bound reading at end of 2026."
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

At 4%, the market is pricing an almost negligible chance of the Fed hiking 75bps or more net from 3.75% to reach ≥4.5% by year-end 2026, which is consistent with a hold/cut bias but worth flagging as the rate is already 75bps below the threshold.
