---
signal_id: "CMSIG20260606BD03"
signal_slug: "will-real-gdp-increase-by-more-than-2-vs-bench"
headline: "Real GDP above 2% Q2 2026: 81%; FRED at 1.6%"
semantic_title: "US GDP above 2% in Q2 backed hard despite soft current read"
telemetry: "81% · Real GDP growth, annualized (FRED) 1.6%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-06T10:01:29+00:00"
event_id: "CM-EVT-TTR8WH64R6"
event_slug: "kxgdp-26jul30"
event_question: "Real GDP quarterly growth, Q2 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGDP-26JUL30-T2.0"
  question_raw: "Will **real GDP** increase by more than 2.0% in Q2 2026?"
  current_price: 0.81
  volume_cumulative_usd: 8904.03
  resolves_at: "2026-07-30T14:00:00Z"
bullets:
  - "Kalshi prices Q2 2026 real GDP growth above 2% at 81%."
  - "FRED annualized real GDP growth currently stands at 1.6%."
  - "Market implies a near-40-basis-point acceleration the latest data does not show."
  - "Resolves on the BEA advance GDP release for Q2 2026."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from kalshi API; benchmark Real GDP growth, annualized (FRED) = 1.6%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "kalshi_api"
      benchmark_value:
        tier: "mediated"
        method: "Real GDP growth, annualized (FRED)"
        source_url: "https://fred.stlouisfed.org/series/A191RL1Q225SBEA"
        retrieved_at: "2026-06-06T10:01:29+00:00"
sources:
  - label: "Real GDP growth, annualized (FRED): 1.6%"
    url: "https://fred.stlouisfed.org/series/A191RL1Q225SBEA"
    retrieved_at: "2026-06-06T10:01:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 81% price on GDP exceeding 2% annualized while the current FRED read is 1.6% reflects substantial market optimism about a Q2 rebound that the existing data does not corroborate.
