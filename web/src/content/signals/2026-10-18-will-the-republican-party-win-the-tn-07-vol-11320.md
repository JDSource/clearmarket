---
signal_id: "CMSIG20261018VS03"
signal_slug: "will-the-republican-party-win-the-tn-07-vol-11320"
headline: "TN-07 Republican seat: 97% on $11K volume pop"
semantic_title: "TN-07 GOP hold backed by fresh volume at 97%"
telemetry: "97% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-18T07:48:11+00:00"
event_id: "CM-EVT-N1Q1LN0697"
event_slug: "tn-07-house-election-winner"
event_question: "Will the winner of the TN-07 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x25bb72b2889af65cebf573aaba1d824b13c0663d2a87ead3f1ffc1d09a4455d1"
  question_raw: "Will the Republican Party win the TN-07 House seat?"
  current_price: 0.968
  volume_24h_usd: 11320.900761
  volume_cumulative_usd: 37620.78909399999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket has the Republican TN-07 candidate at 97%, near the ceiling of contract certainty."
  - "24h volume of $11K is 30% of all-time contract volume, a notable single-day share for a presumed safe seat."
  - "Renewed activity on a near-locked contract may reflect late arbitrage or structured positioning ahead of resolution."
  - "Resolves on the TN-07 House race outcome; 3% residual is the only priced risk remaining."
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
      poly_vol_24h_usd: 11320.900761
sources:
  - label: "ClearMarket market record: Will the winner of the TN-07 House election be determin"
    url: "https://clearmarket.fyi/events/tn-07-house-election-winner"
    retrieved_at: "2026-10-18T07:48:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as cleanup and arb traffic on a deeply Republican-favored seat, the volume is operationally interesting but carries no meaningful directional signal.
