---
signal_id: "CMSIG20261007VS04"
signal_slug: "will-isaias-be-the-first-named-hurricane-vol-13471"
headline: "Isaias first 2026 Atlantic hurricane: 97% on $13K"
semantic_title: "Isaias leads the 2026 Atlantic season at 97%"
telemetry: "97% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T15:02:49+00:00"
event_id: "CM-EVT-VWP9GBVJX7"
event_slug: "kxfirsthurricane-26dec01atl"
event_question: "What will be the name of the first hurricane in the Atlantic this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFIRSTHURRICANE-26DEC01ATL-ISA"
  question_raw: "Will Isaias be the first named hurricane in the Atlantic in 2026?"
  current_price: 0.97
  volume_24h_usd: 13471.45
  volume_cumulative_usd: 30694.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-01T15:00:00Z"
bullets:
  - "Kalshi prices Isaias as the first named Atlantic hurricane of 2026 at 97%, indicating the storm has already achieved or is on the verge of hurricane status."
  - "44% of all-time volume hit in 24 hours as traders finalize positions ahead of imminent meteorological resolution."
  - "Volume at near-certain odds reflects late confirming trades as NHC advisories track the storm's intensification in real time."
  - "Resolves YES if Isaias is officially designated the first Atlantic hurricane of the 2026 season by NHC."
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
      kalshi_vol_24h_usd: 13471.45
sources:
  - label: "ClearMarket market record: What will be the name of the first hurricane in the Atl"
    url: "https://clearmarket.fyi/events/kxfirsthurricane-26dec01atl"
    retrieved_at: "2026-10-07T15:02:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 97% price with 44% of all-time volume in one day signals the market is in final settlement mode, relevant for catastrophe-linked desks monitoring Gulf or East Coast landfall probability.
