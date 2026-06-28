---
signal_id: "CMSIG20260628VS00"
signal_slug: "will-benjamin-netanyahu-enter-iran-by-ju-vol-4872882"
headline: "Netanyahu enters Iran: 0% on $4.9M surge"
semantic_title: "Markets write off Netanyahu entering Iran by June 30"
telemetry: "0% · $4.9M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:25:52+00:00"
event_id: "CM-EVT-QF15YF74T9"
event_slug: "who-will-enter-iran-by-june-30"
event_question: "Will someone enter Iran by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x83f38b0110a93a4e68d2391dc70868ab1f8a9a074de58b0ef50d5312e3fcfcf7"
  question_raw: "Will Benjamin Netanyahu enter Iran by June 30?"
  current_price: 0.001
  volume_24h_usd: 4872882.423331999
  volume_cumulative_usd: 12067304.357925
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices zero probability Netanyahu physically enters Iran before June 30."
  - "$4.9M traded in 24h, 40% of all-time volume floods in two days before deadline."
  - "Ceasefire-adjacent diplomacy and Iran nuclear talks keep contract alive; capital piles in to sell the tail."
  - "Resolves June 30; near-certain NO locks in barring an extraordinary geopolitical rupture."
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
      poly_vol_24h_usd: 4872882.423331999
sources:
  - label: "ClearMarket market record: Will someone enter Iran by June 30?"
    url: "https://clearmarket.fyi/events/who-will-enter-iran-by-june-30"
    retrieved_at: "2026-06-28T10:25:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $4.9M surge is almost entirely tail-risk sellers closing out a zero-priced contract ahead of Monday's expiry, desks should read this as a liquidity flush, not a signal of any changed geopolitical expectation.
