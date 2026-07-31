---
signal_id: "CMSIG20260731VS07"
signal_slug: "israel-x-hamas-ceasefire-phase-ii-by-dec-vol-19675"
headline: "Israel-Hamas Phase II by Dec 31: 62% on $19K"
semantic_title: "Israel-Hamas ceasefire Phase II by Dec 31 trades above 50%"
telemetry: "62% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-31T10:35:22+00:00"
event_id: "CM-EVT-W8BMWJ29B8"
event_slug: "israel-x-hamas-ceasefire-phase-ii-by-october-31"
event_question: "Will Israel and Hamas reach a Ceasefire Phase II? (multi-deadline series, 2025-2026)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa6aa5a20027dd49336ca96b7ccbe0fabad29bf3ec01045cf8dc8535ea80156f2"
  question_raw: "Israel x Hamas Ceasefire Phase II by December 31?"
  current_price: 0.62
  volume_24h_usd: 19675.924909999998
  volume_cumulative_usd: 35124.94947200001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "At 62%, Polymarket leans toward a Phase II ceasefire agreement before year-end."
  - "$19K in 24h covers 56% of all-time volume, majority of lifetime activity in one session."
  - "A 62% read with fresh volume suggests new diplomatic progress or mediator activity."
  - "Resolves on a confirmed Phase II ceasefire agreement by December 31, 2026."
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
      poly_vol_24h_usd: 19675.924909999998
sources:
  - label: "ClearMarket market record: Will Israel and Hamas reach a Ceasefire Phase II? (mult"
    url: "https://clearmarket.fyi/events/israel-x-hamas-ceasefire-phase-ii-by-october-31"
    retrieved_at: "2026-07-31T10:35:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority-lifetime volume surge pushing odds above 50% tells a desk that geopolitical risk pricing has shifted materially, relevant for energy, defense, and EM sovereign spread positioning.
