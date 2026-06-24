---
signal_id: "CMSIG20260624VS04"
signal_slug: "spacex-ipo-closing-market-cap-above-1-8-vol-727165"
headline: "SpaceX IPO above $1.8T: 98% on $727K inflow"
semantic_title: "Capital stacks on SpaceX IPO clearing $1.8T at close"
telemetry: "98% · $727K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-24T10:46:26+00:00"
event_id: "CM-EVT-FDQNXYNKT6"
event_slug: "spacex-ipo-closing-market-cap-above"
event_question: "SpaceX IPO closing market cap, 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd4d841659e8b1fe050980ec9b7deae31accc10e529082fe9468ef9699d11aec2"
  question_raw: "SpaceX IPO closing market cap above $1.8T?"
  current_price: 0.982
  volume_24h_usd: 727165.1358640001
  volume_cumulative_usd: 1800066.6684309978
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "98% price treats $1.8T as a virtual certainty, near floor-level conviction."
  - "40% of all-time volume in 24h; fresh capital entering to harvest residual basis, not express a view."
  - "$1.8T is the lowest rung of active SpaceX IPO contracts; its near-certainty anchors the whole ladder."
  - "Resolves at IPO close alongside the broader valuation contract suite."
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
      poly_vol_24h_usd: 727165.1358640001
sources:
  - label: "ClearMarket market record: SpaceX IPO closing market cap, 2027"
    url: "https://clearmarket.fyi/events/spacex-ipo-closing-market-cap-above"
    retrieved_at: "2026-06-24T10:46:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Flows into the $1.8T contract are largely arbitrage-driven yield capture at IPO certainty levels; a desk monitoring genuine valuation uncertainty should focus on the $2.2T, $2.4T contracts.
