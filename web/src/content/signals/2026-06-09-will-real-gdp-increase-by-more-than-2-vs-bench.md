---
signal_id: "CMSIG20260609BD03"
signal_slug: "will-real-gdp-increase-by-more-than-2-vs-bench"
headline: "US real GDP above 2% Q2 2026: 81%; GDP now 1.6%"
semantic_title: "Traders back US GDP accelerating above 2% in Q2 2026"
telemetry: "81% · Real GDP growth, annualized (FRED) 1.6%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-09T10:58:56+00:00"
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
  - "Kalshi prices an 81% chance US real GDP growth exceeds 2% annualized in Q2 2026."
  - "FRED real GDP annualized growth currently stands at 1.6%."
  - "Market implies a 40-basis-point acceleration from the current print is the likely outcome."
  - "Resolves against the BEA advance Q2 2026 GDP release."
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
        retrieved_at: "2026-06-09T10:58:56+00:00"
sources:
  - label: "Real GDP growth, annualized (FRED): 1.6%"
    url: "https://fred.stlouisfed.org/series/A191RL1Q225SBEA"
    retrieved_at: "2026-06-09T10:58:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With GDP currently printing at 1.6% annualized, an 81% probability on exceeding 2% reflects strong trader conviction in a significant near-term rebound that the official data does not yet support.
