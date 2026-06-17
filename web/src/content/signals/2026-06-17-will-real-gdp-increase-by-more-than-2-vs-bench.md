---
signal_id: "CMSIG20260617BD01"
signal_slug: "will-real-gdp-increase-by-more-than-2-vs-bench"
headline: "US Q2 real GDP above 2%: 76%; FRED Q1 at 1.6%"
semantic_title: "Capital piles into US real GDP surging above 2%"
telemetry: "76% · Real GDP growth, annualized (FRED) 1.6%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-17T12:15:05+00:00"
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
  - "Kalshi traders price a 76% chance Q2 real GDP growth exceeds 2% annualized."
  - "FRED real GDP growth (annualized) last printed 1.6% in Q1 2026."
  - "Market implies a sharp rebound of over 0.4 percentage points from the current print."
  - "Resolves on BEA Q2 2026 advance GDP release, expected late July 2026."
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
        retrieved_at: "2026-06-17T12:15:05+00:00"
sources:
  - label: "Real GDP growth, annualized (FRED): 1.6%"
    url: "https://fred.stlouisfed.org/series/A191RL1Q225SBEA"
    retrieved_at: "2026-06-17T12:15:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi is pricing a strong majority chance of a recovery well above the current 1.6% FRED print, implying traders expect a significant Q2 acceleration that official data has not yet confirmed.
