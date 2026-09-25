---
signal_id: "CMSIG20260925VS02"
signal_slug: "will-republican-win-the-house-race-for-p-vol-16503"
headline: "PA-8 GOP House: 33% on $16K volume spike"
semantic_title: "PA-8 House race trades as a competitive toss-up at 33%"
telemetry: "33% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T13:13:41+00:00"
event_id: "CM-EVT-RB6J9TCV17"
event_slug: "housepa8-26"
event_question: "PA-08 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEPA8-26-R"
  question_raw: "Will Republican win the House race for PA-8?"
  current_price: 0.33
  volume_24h_usd: 16503.34
  volume_cumulative_usd: 24759.76
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican at 33%, placing the seat in Democratic-lean territory and making this one of the cycle's genuine competitive flips."
  - "24h volume represents 67% of all-time handle, the largest single-session share in this batch, flagging a dramatic surge in contract activity."
  - "PA-8 is a Biden-era swing district; a two-thirds-of-lifetime volume day implies a specific local catalyst is in play."
  - "Contract resolves on the 2026 PA-8 general election outcome."
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
      kalshi_vol_24h_usd: 16503.34
sources:
  - label: "ClearMarket market record: PA-08 House winner?"
    url: "https://clearmarket.fyi/events/housepa8-26"
    retrieved_at: "2026-09-25T13:13:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 67% all-time share is the sharpest concentration in this batch; a desk should immediately check for a PA-8 candidate development, poll, or redistricting update.
