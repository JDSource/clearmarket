---
signal_id: "CMSIG20260726VS05"
signal_slug: "will-average-gas-prices-be-above-4-vol-10574"
headline: "Avg gas above $4.04: 99% on $10K surge"
semantic_title: "Gas prices above $4.04 locked in at 99%"
telemetry: "99% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-26T09:56:30+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.04"
  question_raw: "Will average **gas prices** be above $4.04?"
  current_price: 0.99
  volume_24h_usd: 10574.42
  volume_cumulative_usd: 18340.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "Kalshi prices average gas above $4.04 at 99%, the market treats the threshold as already breached."
  - "58% of all-time volume in 24h is the highest all-time share in this batch, signaling urgency near expiry."
  - "Current EIA or GasBuddy data almost certainly confirm prices above the threshold, collapsing uncertainty."
  - "Resolution is imminent; volume reflects settlement-driven positioning, not fresh directional bets."
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
      kalshi_vol_24h_usd: 10574.42
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-26T09:56:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 58% all-time share combined with a 99% price is a textbook pre-settlement arb flush, desks are extracting the last basis points before the contract closes, not expressing a new macro view on pump prices.
