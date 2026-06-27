---
signal_id: "CMSIG20260627VS01"
signal_slug: "solana-all-time-high-by-june-30-2026-vol-223112"
headline: "SOL ATH by June 30: 0% on $223K inflow"
semantic_title: "Solana all-time-high by June 30 sits in dead-money territory"
telemetry: "0% · $223K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T10:03:08+00:00"
event_id: "CM-EVT-4PF8HK6P16"
event_slug: "solana-all-time-high-by"
event_question: "Solana all-time high in 2026? (quarterly series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x977b7d56cdeaead422cc48017dade80ec07a60036b19f1c5ab57ad48f52768e5"
  question_raw: "Solana all time high by June 30, 2026?"
  current_price: 0.001
  volume_24h_usd: 223112.16499999998
  volume_cumulative_usd: 623215.8193950005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-01T05:00:00Z"
bullets:
  - "Polymarket at 0%, market has fully discounted a Solana ATH in three days."
  - "$223K in 24h represents 36% of all-time volume, an unusually concentrated end-of-life flush."
  - "SOL would need to breach prior highs imminently; spot price action clearly not supportive."
  - "Resolution June 30, zero price with heavy flows implies last sellers clearing positions."
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
      poly_vol_24h_usd: 223112.16499999998
sources:
  - label: "ClearMarket market record: Solana all-time high in 2026? (quarterly series)"
    url: "https://clearmarket.fyi/events/solana-all-time-high-by"
    retrieved_at: "2026-06-27T10:03:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy terminal-day volume at zero is a reliable signal that desks are recycling freed capital into longer-dated crypto duration rather than this contract.
