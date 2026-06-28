---
signal_id: "CMSIG20260628VS05"
signal_slug: "will-the-h200-compute-per-hour-price-be-vol-24399"
headline: "H200 above $4.79/hr: 94% on $24K volume"
semantic_title: "H200 compute floor at $4.79 draws concentrated conviction ahead of close"
telemetry: "94% · $24K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:25:52+00:00"
event_id: "CM-EVT-XQHHCRQHC2"
event_slug: "kxh200q-26jun30"
event_question: "Will the price of NVIDIA H200 compute decrease by June 30, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200Q-26JUN30-4.790"
  question_raw: "Will the H200 compute per hour price be above $4.79 by Jun 30?"
  current_price: 0.94
  volume_24h_usd: 24399.28
  volume_cumulative_usd: 31674.22
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi marks H200 spot above $4.79/hr at 94%, a lower threshold drawing the same conviction as the $4.99 contract."
  - "$24K in 24h is 77% of all-time volume, compressing sharply into the June 30 resolution."
  - "Near-parallel pricing with the $4.99 contract implies the market sees little rate risk between these two bands."
  - "Resolves June 30; residual uncertainty is minimal barring an abrupt compute market dislocation."
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
      kalshi_vol_24h_usd: 24399.28
sources:
  - label: "ClearMarket market record: Will the price of NVIDIA H200 compute decrease by June "
    url: "https://clearmarket.fyi/events/kxh200q-26jun30"
    retrieved_at: "2026-06-28T10:25:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-identical pricing across the $4.79 and $4.99 H200 contracts with heavy late-stage volume suggests the market has priced a tight range for GPU spot rates, useful for desks calibrating AI infrastructure cost-of-capital assumptions.
