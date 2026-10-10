---
signal_id: "CMSIG20261010VS02"
signal_slug: "will-republican-win-the-house-race-for-s-vol-20920"
headline: "SC-01 GOP House: 72% on $21K volume spike"
semantic_title: "GOP traders pile into SC-01 House race at 72%"
telemetry: "72% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T14:12:44+00:00"
event_id: "CM-EVT-1VRNWSCZT7"
event_slug: "kxhouserace-sc01-26"
event_question: "SC-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-SC01-26-R"
  question_raw: "Will Republican win the House race for SC-01?"
  current_price: 0.72
  volume_24h_usd: 20920.77
  volume_cumulative_usd: 33291.46
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Republican at 72%, market leans GOP but leaves meaningful room for a Democratic pickup."
  - "$21K in 24h is 63% of all-time contract volume, marking a decisive surge in market attention."
  - "Parallel activity in the Democratic SC-01 contract (Spike 4) confirms traders are actively crossing this race."
  - "Resolves on SC-01 general election outcome."
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
      kalshi_vol_24h_usd: 20920.77
sources:
  - label: "ClearMarket market record: SC-01 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-sc01-26"
    retrieved_at: "2026-10-10T14:12:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes on both sides of SC-01 (GOP and Dem contracts) tell a desk traders are actively debating the seat's competitiveness today, watch for a polling drop or ad-spend report.
