---
signal_id: "CMSIG20260616VS00"
signal_slug: "will-trump-restart-project-freedom-by-ju-vol-3135487"
headline: "Project Freedom restart: 100% on $3.1M surge"
semantic_title: "Traders lock in Project Freedom restart by June 30"
telemetry: "100% · $3.1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-16T12:50:46+00:00"
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
  - "Polymarket prices certainty, 100% implies resolution already triggered or imminent."
  - "24h volume $3.1M is 59% of all-time; fresh capital flooding a near-certain outcome."
  - "Surge pattern consistent with confirming news event driving late settlement flow."
  - "Contract resolves June 30; volume likely compressing final arbitrage basis to zero."
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
    retrieved_at: "2026-06-16T12:50:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a near-resolved contract with volume driven by settlement arbitrage, not directional speculation, monitor for official confirmation to close any residual basis.
