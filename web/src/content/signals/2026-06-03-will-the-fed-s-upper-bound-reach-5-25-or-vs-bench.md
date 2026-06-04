---
signal_id: "CMSIG20260603BD27"
signal_slug: "will-the-fed-s-upper-bound-reach-5-25-or-vs-bench"
headline: "Fed upper bound ≥5.25% before 2027: 3%; rate at 3.75%"
semantic_title: "Rate path to 5.25 percent detaches sharply from FRED baseline"
telemetry: "3% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-03T01:45:00+00:00"
event_id: "CM-EVT-RLQQ3VJDS6"
event_slug: "what-will-fed-rate-hit-before-2027"
event_question: "Will the Federal Reserve's policy rate reach or exceed a specific level before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x728246cda497e10289a7145245675e2baece6561ba784760b0914108e6e42c04"
  question_raw: "Will the Fed’s upper bound reach 5.25% or higher before 2027?"
  current_price: 0.03
  volume_cumulative_usd: 141016.509875
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 3% chance the upper bound reaches 5.25% or higher before 2027."
  - "Fed funds upper bound (FRED) currently at 3.75%."
  - "Market implies a 150bps+ net hike cycle restarting before year-end is nearly impossible."
  - "Resolves on FRED Fed funds upper bound reading before January 2027."
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

A 3% price on the upper bound reaching 5.25% from 3.75% implies the market sees a 150bps hiking cycle before year-end as nearly inconceivable, consistent with the broader hold/cut bias in related markets.
