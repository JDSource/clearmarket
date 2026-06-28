---
signal_id: "CMSIG20260628VS04"
signal_slug: "will-the-h200-compute-per-hour-price-be-vol-40913"
headline: "H200 above $4.99/hr: 94% on $41K surge"
semantic_title: "Heavy flows defend H200 compute above $4.99 into June close"
telemetry: "94% · $41K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:25:52+00:00"
event_id: "CM-EVT-XQHHCRQHC2"
event_slug: "kxh200q-26jun30"
event_question: "Will the price of NVIDIA H200 compute decrease by June 30, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200Q-26JUN30-4.990"
  question_raw: "Will the H200 compute per hour price be above $4.99 by Jun 30?"
  current_price: 0.94
  volume_24h_usd: 40913.24
  volume_cumulative_usd: 79904.98
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi prices H200 hourly compute above $4.99 at 94%, market expects GPU spot rates to hold elevated."
  - "$41K in 24h is 51% of all-time volume, indicating fresh institutional attention on AI infrastructure pricing."
  - "Persistent hyperscaler demand and constrained H200 supply underpin the high-conviction YES positioning."
  - "Resolves June 30; 6% NO reflects thin tail for a sudden spot-price collapse in the final trading days."
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
      kalshi_vol_24h_usd: 40913.24
sources:
  - label: "ClearMarket market record: Will the price of NVIDIA H200 compute decrease by June "
    url: "https://clearmarket.fyi/events/kxh200q-26jun30"
    retrieved_at: "2026-06-28T10:25:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 51% all-time volume concentration signals desks are actively hedging or expressing views on near-term GPU compute cost floors, relevant for AI infrastructure procurement and cloud margin modeling.
