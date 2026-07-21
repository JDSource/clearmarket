---
signal_id: "CMSIG20260721VS01"
signal_slug: "will-ethereum-dip-to-1-250-by-december-vol-188630"
headline: "ETH $1,250 by Dec 31: 26% on $189K flow"
semantic_title: "Traders stack tail-risk odds on ETH fading to $1,250"
telemetry: "26% · $189K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-21T10:22:52+00:00"
event_id: "CM-EVT-DSZVH8N0R8"
event_slug: "what-price-will-ethereum-hit-before-2027"
event_question: "What price will Ethereum reach by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x766996108017c3b6452c23db79ab1c714d8d9d9da846a4c316f5e047754a229d"
  question_raw: "Will Ethereum dip to $1,250 by December 31, 2026?"
  current_price: 0.26
  volume_24h_usd: 188630.881579
  volume_cumulative_usd: 347292.5145280002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "26% prices a meaningful but minority probability that Ethereum revisits $1,250 by year-end."
  - "Polymarket sees $189K in 24h, 54% of the contract's all-time volume in a single session."
  - "Fresh inflow at 26% suggests macro or crypto-specific stress concerns are prompting hedging activity."
  - "Resolves December 31, 2026 on Ethereum spot price."
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
      poly_vol_24h_usd: 188630.881579
sources:
  - label: "ClearMarket market record: What price will Ethereum reach by 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-ethereum-hit-before-2027"
    retrieved_at: "2026-07-21T10:22:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that a 26% print with half the all-time volume landing in one session points to institutional hedgers absorbing downside exposure, likely tied to broader risk-off positioning in crypto or macro rate expectations.
