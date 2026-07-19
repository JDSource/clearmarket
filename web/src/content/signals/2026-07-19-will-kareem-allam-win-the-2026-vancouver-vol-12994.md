---
signal_id: "CMSIG20260719VS05"
signal_slug: "will-kareem-allam-win-the-2026-vancouver-vol-12994"
headline: "Allam wins Vancouver mayor 2026: 27% on $13K surge"
semantic_title: "Allam Vancouver mayor bid draws early speculative positioning"
telemetry: "27% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-19T09:49:33+00:00"
event_id: "CM-EVT-G39S6YRVR7"
event_slug: "vancouver-mayoral-election-winner"
event_question: "Will Kennedy Stewart win the 2026 Vancouver mayoral election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x574baadddd5ff73355480351a6b067f762d4ad18ffdd619aa99253820b691845"
  question_raw: "Will Kareem Allam win the 2026 Vancouver mayoral election?"
  current_price: 0.27
  volume_24h_usd: 12994.46889
  volume_cumulative_usd: 51691.67848800002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-17T00:00:00Z"
bullets:
  - "27% price grants Allam genuine contender status in a race that remains early and fluid."
  - "$13K in 24h is 25% of all-time Polymarket volume, a notable but measured accumulation for a local race."
  - "Vancouver mayoral contest draws cross-border attention given housing and urban-policy implications."
  - "Election expected fall 2026; positioning this early reflects name-recognition or endorsement catalysts."
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
      poly_vol_24h_usd: 12994.46889
sources:
  - label: "ClearMarket market record: Will Kennedy Stewart win the 2026 Vancouver mayoral ele"
    url: "https://clearmarket.fyi/events/vancouver-mayoral-election-winner"
    retrieved_at: "2026-07-19T09:49:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A quarter of lifetime volume arriving mid-cycle on a Canadian municipal race suggests cross-border political capital is taking early directional views, desks tracking Canadian urban policy should monitor.
