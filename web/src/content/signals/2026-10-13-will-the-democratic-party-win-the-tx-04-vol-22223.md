---
signal_id: "CMSIG20261013VS03"
signal_slug: "will-the-democratic-party-win-the-tx-04-vol-22223"
headline: "TX-04 Democrat: 1% on $22K Polymarket surge"
semantic_title: "TX-04 stays a long shot for Democrats, priced at 1%"
telemetry: "1% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T15:33:23+00:00"
event_id: "CM-EVT-1P68WDW7C0"
event_slug: "tx-04-house-election-winner"
event_question: "TX-04 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x369d012dcaaee5779d4f91d3dcc31a1e1ff1239212214e5db7ba5f791538382f"
  question_raw: "Will the Democratic Party win the TX-04 House seat?"
  current_price: 0.01
  volume_24h_usd: 22223.05
  volume_cumulative_usd: 56410.571298
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats at just 1% in TX-04, functionally treating the seat as a Republican hold."
  - "$22.2K in 24h is 39% of all-time volume; fresh flow into a near-zero contract signals deliberate positioning."
  - "Deep-red East Texas district; volume at 1% likely reflects hedgers or map-sweep bettors covering long-shot scenarios."
  - "Resolves on November 2026 House election result."
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
      poly_vol_24h_usd: 22223.05
sources:
  - label: "ClearMarket market record: TX-04 House Election Winner"
    url: "https://clearmarket.fyi/events/tx-04-house-election-winner"
    retrieved_at: "2026-10-13T15:33:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh capital entering a 1% contract in a safe Republican district is more informative about broad House-map hedging strategies than any genuine Democratic competitiveness in TX-04.
