---
signal_id: "CMSIG20260927VS00"
signal_slug: "will-the-republicans-win-the-south-carol-vol-39456"
headline: "SC Senate GOP hold: 87% on $39K surge"
semantic_title: "Republicans stay heavy favorites in SC Senate race"
telemetry: "87% · $39K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-27T13:31:15+00:00"
event_id: "CM-EVT-44DJH0XML6"
event_slug: "south-carolina-senate-election-winner"
event_question: "Will a winner be declared in the South Carolina Senate election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1c017cbb38a9d0ab233ebb265b25c78290317e6a2470657ca18a73a112397b55"
  question_raw: "Will the Republicans win the South Carolina Senate race in 2026?"
  current_price: 0.87
  volume_24h_usd: 39456.455298
  volume_cumulative_usd: 146708.50427200002
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republican win at 87%, reflecting a near-lock on the seat with limited upset risk."
  - "24h volume of $39K represents 27% of all-time contract volume, a sharp single-day concentration."
  - "Fresh attention to a lopsided race often precedes a polling release or candidate development sharpening conviction."
  - "Contract resolves on 2026 South Carolina Senate election outcome."
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
      poly_vol_24h_usd: 39456.455298
sources:
  - label: "ClearMarket market record: Will a winner be declared in the South Carolina Senate "
    url: "https://clearmarket.fyi/events/south-carolina-senate-election-winner"
    retrieved_at: "2026-09-27T13:31:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 27% single-session volume share on an 87% contract signals desks are actively layering exposure into a high-confidence position, worth monitoring for any catalyst that could compress that edge.
