---
signal_id: "CMSIG20260727VS07"
signal_slug: "will-average-gas-prices-be-above-4-vol-14708"
headline: "US gas above $4.06: 90% on $15K volume"
semantic_title: "Heavy trading tests the $4.06 gas threshold at 90% odds"
telemetry: "90% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-27T11:16:33+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.06"
  question_raw: "Will average **gas prices** be above $4.06?"
  current_price: 0.9
  volume_24h_usd: 14708.35
  volume_cumulative_usd: 38743.73
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "Kalshi prices average US gas above $4.06 at 90%, first strike in the ladder where meaningful doubt appears."
  - "24h volume $15K is 38% of all-time; the contract has more historical depth than the tighter strikes."
  - "The 10% miss probability at $4.06 marks the market's credible upper boundary for the current price cycle."
  - "Contrast with 99% at $4.04 makes $4.06 the key inflection point across the entire gas-price ladder."
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
      kalshi_vol_24h_usd: 14708.35
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-27T11:16:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The drop from 99% to 90% at $4.06 is the first actionable spread in the gas ladder, desks hedging fuel-cost exposure should treat this strike as the live uncertainty boundary for the current EIA reporting window.
