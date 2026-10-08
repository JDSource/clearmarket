---
signal_id: "CMSIG20261008VS05"
signal_slug: "will-cpi-rise-more-than-0-6-in-septembe-vol-10088"
headline: "CPI +0.6% Sep monthly: 20% on $10K"
semantic_title: "Buyers stay light on a 0.6% monthly CPI jump for September"
telemetry: "20% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T15:10:56+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.6"
  question_raw: "Will CPI rise more than 0.6% in September 2026?"
  current_price: 0.2
  volume_24h_usd: 10088.23
  volume_cumulative_usd: 30966.24
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "20% price, market assigns low but non-trivial odds to a hot 0.6% monthly CPI reading for September."
  - "24h volume of $10K is 33% of all-time, solid session flow as the September release window opens."
  - "A 0.6% monthly print would be the hottest reading in over a year; volume reflects tail-risk hedging."
  - "Resolves on BLS September 2026 monthly CPI print."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 10088.23
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-08T15:10:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

One-in-five odds on a 0.6% monthly CPI spike with fresh volume arriving pre-release indicates the desk community is paying for inflation upside tail protection, not expecting it as a base case.
