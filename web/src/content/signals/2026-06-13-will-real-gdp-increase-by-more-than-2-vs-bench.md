---
signal_id: "CMSIG20260613BD01"
signal_slug: "will-real-gdp-increase-by-more-than-2-vs-bench"
headline: "US Q2 real GDP above 2%: 76%; FRED Q1 at 1.6%"
semantic_title: "Traders pile into US real GDP growth topping 2%"
telemetry: "76% · Real GDP growth, annualized (FRED) 1.6%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-13T10:26:41+00:00"
event_id: "CM-EVT-TTR8WH64R6"
event_slug: "kxgdp-26jul30"
event_question: "Real GDP quarterly growth, Q2 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGDP-26JUL30-T2.0"
  question_raw: "Will **real GDP** increase by more than 2.0% in Q2 2026?"
  current_price: 0.76
  volume_cumulative_usd: 9310.55
  resolves_at: "2026-07-30T14:00:00Z"
bullets:
  - "Kalshi prices a Q2 real GDP print above 2% at 76%."
  - "FRED annualized real GDP growth last recorded at 1.6% in Q1 2026."
  - "Market implies a near-certain acceleration of more than 40 basis points above the latest official read."
  - "Resolves on BEA's advance Q2 2026 GDP release."
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
        retrieved_at: "2026-06-13T10:26:41+00:00"
sources:
  - label: "Real GDP growth, annualized (FRED): 1.6%"
    url: "https://fred.stlouisfed.org/series/A191RL1Q225SBEA"
    retrieved_at: "2026-06-13T10:26:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi traders assign a 76% probability to real GDP exceeding 2% in Q2 despite the current FRED print sitting at 1.6%, implying the market expects a sharp rebound that the data have not yet validated.
