---
signal_id: "CMSIG20260725VS04"
signal_slug: "will-average-gas-prices-be-above-4-vol-53899"
headline: "Gas above $4.10: 98% on $54K Kalshi volume"
semantic_title: "Gas above $4.10 stays a near-lock at 98% on heavy trading"
telemetry: "98% · $54K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-25T09:43:16+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.10"
  question_raw: "Will average **gas prices** be above $4.10?"
  current_price: 0.98
  volume_24h_usd: 53899.37
  volume_cumulative_usd: 119562.73
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "Kalshi prices average gas above $4.10 at 98%, the market has essentially resolved this threshold as crossed."
  - "$54K in 24h is 45% of all-time volume, a large late-stage flow on a contract already at the ceiling."
  - "At 98%, volume is almost certainly position settlement and final arbitrage, not a new directional view."
  - "See Spike 6 for the companion $4.110 threshold contract, which prices at 80%, the gap between them is the live debate."
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
      kalshi_vol_24h_usd: 53899.37
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-25T09:43:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $4.10 contract is effectively settled at 98%; desks should shift attention to the $4.110 companion contract where the 80% price still reflects genuine uncertainty.
