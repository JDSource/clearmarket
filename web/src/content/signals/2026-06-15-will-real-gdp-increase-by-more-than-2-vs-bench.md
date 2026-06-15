---
signal_id: "CMSIG20260615BD01"
signal_slug: "will-real-gdp-increase-by-more-than-2-vs-bench"
headline: "US real GDP above 2% Q2: 76%; FRED print at 1.6%"
semantic_title: "Traders pile into US real GDP growth breaking above 2%"
telemetry: "76% · Real GDP growth, annualized (FRED) 1.6%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-15T13:52:56+00:00"
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
  - "Kalshi prices a greater-than-2% Q2 real GDP outcome at 76%."
  - "FRED annualized real GDP growth currently reads 1.6%."
  - "Market implies a sharp rebound of roughly 0.4 percentage points above threshold, well beyond the current print."
  - "Resolves against advance BEA Q2 2026 GDP release, expected late July."
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
        retrieved_at: "2026-06-15T13:52:56+00:00"
sources:
  - label: "Real GDP growth, annualized (FRED): 1.6%"
    url: "https://fred.stlouisfed.org/series/A191RL1Q225SBEA"
    retrieved_at: "2026-06-15T13:52:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi traders are pricing a three-in-four chance of Q2 real GDP exceeding 2% annualized even as the current FRED read sits 40 basis points below that threshold, signaling strong desk conviction in a growth acceleration the official data has not yet shown.
