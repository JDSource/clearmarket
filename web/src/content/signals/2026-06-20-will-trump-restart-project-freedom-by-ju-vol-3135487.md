---
signal_id: "CMSIG20260620VS00"
signal_slug: "will-trump-restart-project-freedom-by-ju-vol-3135487"
headline: "Project Freedom restart: 100% on $3.1M surge"
semantic_title: "Capital locks in Project Freedom restart by June 30"
telemetry: "100% · $3.1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-20T10:31:13+00:00"
event_id: "CM-EVT-8BYGC61G14"
event_slug: "will-trump-restart-project-freedom-by"
event_question: "Will Trump restart Project Freedom by 2025?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdfd4d487d004c266493bdf32551d7f018c7eb4b9325f42ac368dd5075eec36a9"
  question_raw: "Will Trump restart Project Freedom by June 30?"
  current_price: 0.999
  volume_24h_usd: 3135487.8375099995
  volume_cumulative_usd: 5328105.882777
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Project Freedom restart by June 30 at certainty, 100% implies event is confirmed or imminent."
  - "24h volume of $3.1M represents 59% of all-time handle, signaling a decisive late-resolution flow."
  - "Near-certain pricing at deadline suggests the market has absorbed confirming information; resolution likely within days."
  - "Contract resolves June 30; any residual trading is likely hedging against edge-case invalidation."
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
      poly_vol_24h_usd: 3135487.8375099995
sources:
  - label: "ClearMarket market record: Will Trump restart Project Freedom by 2025?"
    url: "https://clearmarket.fyi/events/will-trump-restart-project-freedom-by"
    retrieved_at: "2026-06-20T10:31:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a near-resolved contract where volume reflects settlement positioning, not directional speculation, confirm underlying event status before assuming alpha.
