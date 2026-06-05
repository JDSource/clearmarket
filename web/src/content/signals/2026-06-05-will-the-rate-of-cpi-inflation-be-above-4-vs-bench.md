---
signal_id: "CMSIG20260605BD01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-4-vs-bench"
headline: "CPI above 4% thru May 2026: 99%; FRED at 3.9%"
semantic_title: "Capital piles into CPI topping 4% for the May year-end read"
telemetry: "99% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T13:57:02+00:00"
event_id: "CM-EVT-5F0G9L6HV6"
event_slug: "kxcpiyoy-26may"
event_question: "CPI year-over-year, May 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26MAY-T4.0"
  question_raw: "Will the rate of CPI inflation be above 4.0% for the year ending in May 2026?"
  current_price: 0.99
  volume_cumulative_usd: 37236.05
  resolves_at: "2026-06-10T14:00:00Z"
bullets:
  - "Kalshi prices CPI above 4% for the year ending May 2026 at 99% probability."
  - "FRED CPI year-over-year currently reads 3.9%, one tenth below the trigger."
  - "Near-100% pricing implies traders treat a 4% breach as already done, yet the official print disagrees."
  - "Resolves against the May 2026 official CPI year-over-year release."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from kalshi API; benchmark CPI inflation, year-over-year (FRED) = 3.9%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "kalshi_api"
      benchmark_value:
        tier: "mediated"
        method: "CPI inflation, year-over-year (FRED)"
        source_url: "https://fred.stlouisfed.org/series/CPIAUCSL"
        retrieved_at: "2026-06-05T13:57:02+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-05T13:57:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi is essentially fully sold on a above-4% CPI print through May 2026, yet the current FRED read sits at 3.9%, creating a stark divergence between market conviction and the official data in hand.
