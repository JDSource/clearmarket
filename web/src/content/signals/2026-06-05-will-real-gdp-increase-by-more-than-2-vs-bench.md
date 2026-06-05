---
signal_id: "CMSIG20260605BD03"
signal_slug: "will-real-gdp-increase-by-more-than-2-vs-bench"
headline: "Real GDP above 2% in Q2 2026: 81%; GDP at 1.6%"
semantic_title: "Real GDP growth above 2% backed hard despite soft Q1 print"
telemetry: "81% · Real GDP growth, annualized (FRED) 1.6%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T13:57:02+00:00"
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
  - "Kalshi prices real GDP growth exceeding 2% in Q2 2026 at 81% probability."
  - "FRED annualized real GDP growth currently stands at 1.6%, well below the 2% threshold."
  - "Market implies a strong rebound of roughly 0.4 points or more above the current pace."
  - "Resolves against the official BEA Q2 2026 advance GDP estimate."
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
        retrieved_at: "2026-06-05T13:57:02+00:00"
sources:
  - label: "Real GDP growth, annualized (FRED): 1.6%"
    url: "https://fred.stlouisfed.org/series/A191RL1Q225SBEA"
    retrieved_at: "2026-06-05T13:57:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi assigns an 81% chance of real GDP topping 2% annualized in Q2 2026, while the current FRED print of 1.6% sits meaningfully below that bar, indicating traders are pricing in a substantial acceleration the data has not yet shown.
