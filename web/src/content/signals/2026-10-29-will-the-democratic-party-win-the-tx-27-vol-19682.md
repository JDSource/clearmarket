---
signal_id: "CMSIG20261029VS07"
signal_slug: "will-the-democratic-party-win-the-tx-27-vol-19682"
headline: "TX-27 Dem House: 2% on $19K Polymarket surge"
semantic_title: "TX-27 Democratic win priced out at 2% on half its all-time volume"
telemetry: "2% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T14:56:22+00:00"
event_id: "CM-EVT-SX0N4B8981"
event_slug: "tx-27-house-election-winner"
event_question: "Will a Democratic candidate win the TX-27 House seat in the 2026 general election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x90c0ab6b7fa75ea903689744bc0b24989b646d3ac86cf96cbc96a816a7788137"
  question_raw: "Will the Democratic Party win the TX-27 House seat?"
  current_price: 0.021
  volume_24h_usd: 19682.596669000002
  volume_cumulative_usd: 39059.773821999996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Market gives Democrats a 2% chance of flipping Texas's 27th congressional district."
  - "Polymarket logs $19.7K in 24h, fully 50% of all-time volume arriving in a single session."
  - "Half of all-time volume at 2% odds signals position closing, arbitrage, or event-driven attention."
  - "Resolves on the 2026 TX-27 general election result."
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
      poly_vol_24h_usd: 19682.596669000002
sources:
  - label: "ClearMarket market record: Will a Democratic candidate win the TX-27 House seat in"
    url: "https://clearmarket.fyi/events/tx-27-house-election-winner"
    retrieved_at: "2026-10-29T14:56:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all-time volume concentrating in one day on a near-zero-priced contract is a structural signal, desks should investigate whether a filing deadline, candidate withdrawal, or adjacent race is driving the sudden attention.
