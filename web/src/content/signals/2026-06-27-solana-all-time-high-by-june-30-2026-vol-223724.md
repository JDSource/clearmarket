---
signal_id: "CMSIG20260627VS02"
signal_slug: "solana-all-time-high-by-june-30-2026-vol-223724"
headline: "Solana all-time high by June 30 priced at zero into expiry"
semantic_title: "Market discounts Solana all-time high before June 30"
telemetry: "0% · $224K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T01:36:27+00:00"
event_id: "CM-EVT-4PF8HK6P16"
event_slug: "solana-all-time-high-by"
event_question: "Solana all-time high in 2026? (quarterly series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x977b7d56cdeaead422cc48017dade80ec07a60036b19f1c5ab57ad48f52768e5"
  question_raw: "Solana all time high by June 30, 2026?"
  current_price: 0.001
  volume_24h_usd: 223724.66099999996
  volume_cumulative_usd: 623215.6193950005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-01T05:00:00Z"
bullets:
  - "Zero probability priced, consensus is Solana cannot reclaim its all-time high in three days."
  - "$224K in 24h represents 36% of the contract's entire lifetime volume."
  - "Solana ATH stands well above current spot; gap is treated as technically unbridgeable near-term."
  - "Contract expires June 30, volume reflects final settlement, not a directional repricing."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 223724.66099999996
sources:
  - label: "ClearMarket market record: Solana all-time high in 2026? (quarterly series)"
    url: "https://clearmarket.fyi/events/solana-all-time-high-by"
    retrieved_at: "2026-06-27T01:36:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Late-stage volume at zero price is a mechanical settlement signal, not fresh bearish conviction; desks should not extrapolate this as a new Solana short thesis.
