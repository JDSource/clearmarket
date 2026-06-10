---
signal_id: "CMSIG20260610BD03"
signal_slug: "will-real-gdp-increase-by-more-than-2-vs-bench"
headline: "Real GDP above 2% in Q2 2026: 81%; now 1.6%"
semantic_title: "Markets back US real GDP surging above 2% in Q2 2026"
telemetry: "81% · Real GDP growth, annualized (FRED) 1.6%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-10T11:37:52+00:00"
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
  - "Kalshi prices real GDP growth exceeding 2.0% annualized in Q2 2026 at 81%."
  - "FRED real GDP growth is currently 1.6% annualized, 40 basis points below the threshold."
  - "Market implies a high-conviction acceleration; the latest official print shows a meaningful shortfall."
  - "Resolves against the BEA advance Q2 2026 GDP estimate."
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
        retrieved_at: "2026-06-10T11:37:52+00:00"
sources:
  - label: "Real GDP growth, annualized (FRED): 1.6%"
    url: "https://fred.stlouisfed.org/series/A191RL1Q225SBEA"
    retrieved_at: "2026-06-10T11:37:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 81% probability on GDP topping 2% sits well above what the current 1.6% FRED print would mechanically suggest, indicating Kalshi traders are pricing in a sharp rebound that the existing data does not yet support.
