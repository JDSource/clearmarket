---
signal_id: "CMSIG20261027VS05"
signal_slug: "scotus-accepts-sports-event-contract-cas-vol-77741"
headline: "SCOTUS sports contract cert: 31% on $78K"
semantic_title: "SCOTUS sports-contract case acceptance stays a long shot at 31%"
telemetry: "31% · $78K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T07:49:11+00:00"
event_id: "CM-EVT-FLWXD81WN4"
event_slug: "scotus-accepts-sports-event-contract-case-by-july-31-2026"
event_question: "Will SCOTUS accept a sports event contract case by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x68e2344a2ce725ca99f3b93df06f27a71f3a893a38e8a6a78f8d85bd2698eb20"
  question_raw: "SCOTUS accepts sports event contract case by December 31, 2026?"
  current_price: 0.31
  volume_24h_usd: 77741.915969
  volume_cumulative_usd: 165766.851938
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "31% price reflects a below-even chance the Supreme Court agrees to hear a sports event contract case by Dec 31, 2026."
  - "$78K in 24h is 47% of all-time volume, nearly half the contract's history in a single session."
  - "Volume concentration near a deadline suggests the market is reacting to a cert petition filing or scheduling order news."
  - "Resolves on whether SCOTUS formally accepts the case before December 31, 2026."
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
      poly_vol_24h_usd: 77741.915969
sources:
  - label: "ClearMarket market record: Will SCOTUS accept a sports event contract case by the "
    url: "https://clearmarket.fyi/events/scotus-accepts-sports-event-contract-case-by-july-31-2026"
    retrieved_at: "2026-10-27T07:49:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-50% single-day share of all-time volume on a SCOTUS cert contract implies a specific procedural event, desks with sports-rights or event-contract exposure should check the Court's conference schedule.
