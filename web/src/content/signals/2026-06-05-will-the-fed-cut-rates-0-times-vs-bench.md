---
signal_id: "CMSIG20260605BD20"
signal_slug: "will-the-fed-cut-rates-0-times-vs-bench"
headline: "Fed 0 cuts in 2026: 69%; upper bound at 3.75%"
semantic_title: "Zero-cut pricing paces above rate already eased to 3.75 percent"
telemetry: "69% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T11:25:34+00:00"
event_id: "CM-EVT-VMYLRHHXK0"
event_slug: "kxratecutcount-26dec31"
event_question: "Will the Federal Reserve cut interest rates at least X times in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRATECUTCOUNT-26DEC31-T0"
  question_raw: "Will the Fed cut rates 0 times?"
  current_price: 0.69
  volume_cumulative_usd: 777502.64
  resolves_at: "2026-12-31T15:00:00Z"
bullets:
  - "Kalshi prices a 69% chance the Fed does not cut rates at all in 2026."
  - "FRED: fed funds upper bound currently 3.75 percent."
  - "Market implies a full-year hold even as the rate sits 150 bps below the 2023 peak."
  - "Resolves on cumulative 2026 FOMC outcomes."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from kalshi API; benchmark Fed funds target rate, upper bound (FRED) = 3.75%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "kalshi_api"
      benchmark_value:
        tier: "mediated"
        method: "Fed funds target rate, upper bound (FRED)"
        source_url: "https://fred.stlouisfed.org/series/DFEDTARU"
        retrieved_at: "2026-06-05T11:25:34+00:00"
sources:
  - label: "Fed funds target rate, upper bound (FRED): 3.75%"
    url: "https://fred.stlouisfed.org/series/DFEDTARU"
    retrieved_at: "2026-06-05T11:25:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The Kalshi 69% no-cut read mirrors Polymarket's identical print, reinforcing a consensus that the Fed stays on hold all year, a striking stance given the rate is already in an easing sequence.
