---
signal_id: "CMSIG20261015VS07"
signal_slug: "will-the-democratic-party-win-the-mn-06-vol-21909"
headline: "MN-06 Dem win: 3% on $21.9K Polymarket surge"
semantic_title: "MN-06 Democratic odds collapse to near zero on fresh volume"
telemetry: "3% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T13:03:58+00:00"
event_id: "CM-EVT-N100WHW0Q2"
event_slug: "mn-06-house-election-winner"
event_question: "Will the Minnesota 6th Congressional District House election winner be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5da40d2769967a08075c5e1ba2f7181cff82b970a04287c469669a5584b2321c"
  question_raw: "Will the Democratic Party win the MN-06 House seat?"
  current_price: 0.027
  volume_24h_usd: 21909.121365000003
  volume_cumulative_usd: 61905.180763
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Democrats priced at just 3% in MN-06, the market has effectively conceded this seat to Republicans."
  - "$21.9K in 24h is 35% of all-time, showing meaningful fresh engagement despite the lopsided price."
  - "Volume flowing into a near-certain Republican outcome suggests House-composition hedging or late position closing."
  - "Resolves on 2026 MN-06 House election result."
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
      poly_vol_24h_usd: 21909.121365000003
sources:
  - label: "ClearMarket market record: Will the Minnesota 6th Congressional District House ele"
    url: "https://clearmarket.fyi/events/mn-06-house-election-winner"
    retrieved_at: "2026-10-15T13:03:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 3% Democratic price absorbing a third of the contract's lifetime volume in one day reads as portfolio-level hedging on Republican House margin rather than any new information about MN-06 competitiveness.
