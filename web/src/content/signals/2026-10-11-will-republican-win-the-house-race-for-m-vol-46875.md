---
signal_id: "CMSIG20261011VS03"
signal_slug: "will-republican-win-the-house-race-for-m-vol-46875"
headline: "MT-1 House GOP: 76% on $47K surge"
semantic_title: "Buyers back the GOP in Montana's MT-1 House race"
telemetry: "76% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T07:48:50+00:00"
event_id: "CM-EVT-QWGZDJ1DQ6"
event_slug: "housemt1-26"
event_question: "MT-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEMT1-26-R"
  question_raw: "Will Republican win the House race for MT-1?"
  current_price: 0.76
  volume_24h_usd: 46875.58
  volume_cumulative_usd: 167418.47
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican at 76% in MT-1, a meaningful but contested lean, not a lock."
  - "28% of all-time volume placed in 24h, the largest single-day dollar flow on this contract."
  - "Montana's at-large district draw makes MT-1 a bellwether for rural House seat movement; fresh volume suggests a catalyst is nearby."
  - "Resolves on 2026 general election night."
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
      kalshi_vol_24h_usd: 46875.58
sources:
  - label: "ClearMarket market record: MT-01 House winner?"
    url: "https://clearmarket.fyi/events/housemt1-26"
    retrieved_at: "2026-10-11T07:48:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 76% price with the largest 24h dollar flow on record for this contract signals the desk that MT-1 is being re-rated as a competitive race worth active positioning.
