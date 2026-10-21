---
signal_id: "CMSIG20261021VS01"
signal_slug: "will-republican-win-the-house-race-for-o-vol-20307"
headline: "OH-10 House race: 66% on fresh $20K Kalshi volume"
semantic_title: "Republicans hold the lead in OH-10 House contest"
telemetry: "66% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T07:48:52+00:00"
event_id: "CM-EVT-TY2DWD9XJ0"
event_slug: "kxhouserace-oh10-26"
event_question: "OH-10 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-OH10-26-R"
  question_raw: "Will Republican win the House race for OH-10?"
  current_price: 0.66
  volume_24h_usd: 20307.47
  volume_cumulative_usd: 61761.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "66% prices Republicans as clear but not dominant favorites, meaningful residual risk remains."
  - "33% of all-time volume arriving in 24h points to a specific catalyst drawing renewed attention."
  - "A two-thirds price in a competitive district suggests late money sees a durable but contested edge."
  - "Resolves on certified Ohio 10th congressional district House race result."
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
      kalshi_vol_24h_usd: 20307.47
sources:
  - label: "ClearMarket market record: OH-10 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-oh10-26"
    retrieved_at: "2026-10-21T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume at 33% of all-time in a single session on a two-thirds price signals that this race has entered competitive-watch territory, worth tracking alongside any late OH-10 polling drops or ad-spend data.
