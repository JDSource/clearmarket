---
signal_id: "CMSIG20260604BD28"
signal_slug: "will-the-fed-s-upper-bound-reach-5-25-or-vs-bench"
headline: "Fed Upper Bound ≥5.25% Before 2027: 3%; at 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-04T11:16:22+00:00"
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
  - "Polymarket prices 3% chance the Fed's upper bound reaches 5.25% or higher before 2027."
  - "FRED benchmark: Fed funds upper bound currently at 3.75%."
  - "Market implies the Fed would need to hike 150 bps from here, seen as near-impossible."
  - "Resolves against FRED Fed funds upper bound before January 2027."
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
        retrieved_at: "2026-06-04T11:16:22+00:00"
sources:
  - label: "Fed funds target rate, upper bound (FRED): 3.75%"
    url: "https://fred.stlouisfed.org/series/DFEDTARU"
    retrieved_at: "2026-06-04T11:16:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 150 bps hiking path from 3.75% to 5.25% by end-2026 is priced at just 3% on Polymarket, consistent with the dominant no-hike consensus, but the current level makes the distance to threshold quantifiable and the market's near-dismissal explicit.
