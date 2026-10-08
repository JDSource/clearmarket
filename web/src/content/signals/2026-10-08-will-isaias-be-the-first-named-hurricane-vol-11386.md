---
signal_id: "CMSIG20261008VS06"
signal_slug: "will-isaias-be-the-first-named-hurricane-vol-11386"
headline: "Isaias first Atlantic hurricane: 99% on $11K"
semantic_title: "Isaias as the first 2026 Atlantic hurricane trades as a near-certainty"
telemetry: "99% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T15:10:56+00:00"
event_id: "CM-EVT-VWP9GBVJX7"
event_slug: "kxfirsthurricane-26dec01atl"
event_question: "What will be the name of the first hurricane in the Atlantic this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFIRSTHURRICANE-26DEC01ATL-ISA"
  question_raw: "Will Isaias be the first named hurricane in the Atlantic in 2026?"
  current_price: 0.99
  volume_24h_usd: 11386.44
  volume_cumulative_usd: 42714.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-01T15:00:00Z"
bullets:
  - "Market at 99%, contract is effectively resolved in traders' minds, with Isaias already named."
  - "24h volume of $11K is 27% of all-time, latecomers capturing near-riskless value as the contract closes."
  - "Storm has already been named Isaias, making residual trading a settlement arbitrage, not a forecast."
  - "Resolves when official NHC naming sequence for the 2026 Atlantic season is confirmed."
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
      kalshi_vol_24h_usd: 11386.44
sources:
  - label: "ClearMarket market record: What will be the name of the first hurricane in the Atl"
    url: "https://clearmarket.fyi/events/kxfirsthurricane-26dec01atl"
    retrieved_at: "2026-10-08T15:10:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 99% price with late-stage volume is a settlement-arb signal, desks can treat this as resolved for hedging purposes, with the small discount representing operational or timing risk only.
