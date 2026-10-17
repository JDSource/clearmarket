---
signal_id: "CMSIG20261017VS06"
signal_slug: "will-the-republican-party-win-the-ga-09-vol-14012"
headline: "GA-09 Republican: 96% on $14K Polymarket surge"
semantic_title: "GA-09 Republican seat priced at 96%; buyers pile in"
telemetry: "96% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T11:58:01+00:00"
event_id: "CM-EVT-L84VY22JQ7"
event_slug: "ga-09-house-election-winner"
event_question: "Will the GA-09 House election winner be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcdc8e74776e150e721ed61a4286dcd9fe8441c7e000bf5810bd791b83b7a6508"
  question_raw: "Will the Republican Party win the GA-09 House seat?"
  current_price: 0.965
  volume_24h_usd: 14012.692729
  volume_cumulative_usd: 30765.90611
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republican at 96% in GA-09, a deep-red Georgia district treated as a near-certainty."
  - "24h volume of $14K is 46% of all-time, nearly half of all trading arriving in a single session."
  - "Concentrated flow at an extreme price level points to confirmation trading following a district-specific development."
  - "Resolves on November 2026 election night."
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
      poly_vol_24h_usd: 14012.692729
sources:
  - label: "ClearMarket market record: Will the GA-09 House election winner be determined by N"
    url: "https://clearmarket.fyi/events/ga-09-house-election-winner"
    retrieved_at: "2026-10-17T11:58:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-half of all-time volume in one session on a 96% contract suggests event-driven positioning rather than genuine uncertainty, desks should note this as a baseline-anchor for the Georgia House delegation outlook.
