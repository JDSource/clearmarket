---
signal_id: "CMSIG20260714VS02"
signal_slug: "will-bitcoin-reach-80-000-by-december-3-vol-26302"
headline: "BTC $80K by Dec 31: 29% on $26K Polymarket volume"
semantic_title: "Heavy flows stack into $80K Bitcoin year-end recovery bet"
telemetry: "29% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-14T09:55:02+00:00"
event_id: "CM-EVT-2S263KKBP2"
event_slug: "what-price-will-bitcoin-hit-before-2027"
event_question: "What price will Bitcoin reach by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc564e47b7a853f3e52ea7b8e28d69ed99fcb284929364fd0f8024c2bca03ea96"
  question_raw: "Will Bitcoin reach $80,000 by December 31, 2026?"
  current_price: 0.29
  volume_24h_usd: 26302.158521
  volume_cumulative_usd: 80072.98926500003
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "29% price reflects meaningful but minority odds that Bitcoin reclaims $80K before year-end."
  - "$26,302 traded in 24h, 33% of all-time contract volume, indicates a sharp surge in positioning."
  - "Paired spike with the $85K contract suggests systematic layering across Bitcoin recovery thresholds."
  - "Resolution December 31, 2026; current BTC price well below strike, requiring sustained upside."
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
      poly_vol_24h_usd: 26302.158521
sources:
  - label: "ClearMarket market record: What price will Bitcoin reach by the end of 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-before-2027"
    retrieved_at: "2026-07-14T09:55:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes across $80K and $85K strikes on Polymarket point to coordinated threshold-stacking, signaling institutional interest in a structured Bitcoin recovery scenario into year-end.
