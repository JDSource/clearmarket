---
signal_id: "CMSIG20261008VS05"
signal_slug: "will-isaias-be-the-first-named-hurricane-vol-12845"
headline: "Isaias first Atlantic hurricane: 99% on $12.8K"
semantic_title: "Isaias as 2026's first Atlantic hurricane is all but priced in"
telemetry: "99% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T07:49:04+00:00"
event_id: "CM-EVT-VWP9GBVJX7"
event_slug: "kxfirsthurricane-26dec01atl"
event_question: "What will be the name of the first hurricane in the Atlantic this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFIRSTHURRICANE-26DEC01ATL-ISA"
  question_raw: "Will Isaias be the first named hurricane in the Atlantic in 2026?"
  current_price: 0.99
  volume_24h_usd: 12845.83
  volume_cumulative_usd: 38012.83
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-01T15:00:00Z"
bullets:
  - "Kalshi prices Isaias as the first named Atlantic hurricane of 2026 at 99%, leaving almost no uncertainty."
  - "34% of all-time volume, $12.8K, arrived in 24 hours, likely confirming a storm already in progress or imminently named."
  - "Near-certainty pricing with fresh volume suggests the market is settling rather than discovering, final capital positioning at the finish line."
  - "Resolves once Isaias is officially classified as the first hurricane of the 2026 Atlantic season."
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
      kalshi_vol_24h_usd: 12845.83
sources:
  - label: "ClearMarket market record: What will be the name of the first hurricane in the Atl"
    url: "https://clearmarket.fyi/events/kxfirsthurricane-26dec01atl"
    retrieved_at: "2026-10-08T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 99% price backed by a 34% all-time volume surge signals a near-resolved contract being closed out by traders locking in gains, not a genuine pricing event, useful as a real-time confirmation of NHC classification status.
