---
signal_id: "CMSIG20260927VS03"
signal_slug: "will-the-republican-party-win-the-ca-46-vol-10807"
headline: "GOP CA-46 House seat: 4% on $11K inflow"
semantic_title: "CA-46 GOP House bid trades at 4% through fresh volume"
telemetry: "4% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-27T13:31:15+00:00"
event_id: "CM-EVT-Q44D460T30"
event_slug: "ca-46-house-election-winner"
event_question: "Will the CA-46 House seat be won by a new representative in the 2026 general election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x544f00d1660aa786d5c535fb0c217246062d70274cbd8bcfddd64703206ab2eb"
  question_raw: "Will the Republican Party win the CA-46 House seat?"
  current_price: 0.04
  volume_24h_usd: 10807.0
  volume_cumulative_usd: 37284.63314
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republican odds in CA-46 at 4%, matching CA-36 as a near-certain Democratic hold."
  - "24h volume of $11K covers 29% of all-time contract activity, a meaningful single-session share."
  - "Paired surge with CA-36 suggests systematic attention to California House races, possibly tied to redistricting review or a coordinated research sweep."
  - "Contract resolves on the 2026 CA-46 House general election outcome."
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
      poly_vol_24h_usd: 10807.0
sources:
  - label: "ClearMarket market record: Will the CA-46 House seat be won by a new representativ"
    url: "https://clearmarket.fyi/events/ca-46-house-election-winner"
    retrieved_at: "2026-09-27T13:31:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous volume spike across CA-36 and CA-46 at identical 4% prices points to coordinated desk-level review of California House exposure rather than isolated retail interest.
