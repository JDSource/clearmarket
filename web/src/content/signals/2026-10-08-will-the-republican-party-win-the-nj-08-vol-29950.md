---
signal_id: "CMSIG20261008VS00"
signal_slug: "will-the-republican-party-win-the-nj-08-vol-29950"
headline: "NJ-08 GOP win: 1% on heavy $29.9K surge"
semantic_title: "NJ-08 stays a near-certain Democratic hold"
telemetry: "1% · $30K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T07:49:04+00:00"
event_id: "CM-EVT-MGFVWYRY00"
event_slug: "nj-08-house-election-winner"
event_question: "Will the NJ-08 House seat be won by a Republican in the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0bb1b93d62a15087252b42e86b95f82f27232a590f2281da99e2e4cd623c2576"
  question_raw: "Will the Republican Party win the NJ-08 House seat?"
  current_price: 0.01
  volume_24h_usd: 29950.266667
  volume_cumulative_usd: 39361.648827000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republican win at just 1%, implying NJ-08 is all but locked for Democrats."
  - "24h volume of $29.9K equals 76% of all-time, nearly the entire contract history traded in one session."
  - "Surge at 1% suggests fresh capital arriving to sell Republican chances into near-zero, not to buy."
  - "Resolves on NJ-08 House race outcome; no realistic GOP path priced."
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
      poly_vol_24h_usd: 29950.266667
sources:
  - label: "ClearMarket market record: Will the NJ-08 House seat be won by a Republican in the"
    url: "https://clearmarket.fyi/events/nj-08-house-election-winner"
    retrieved_at: "2026-10-08T07:49:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume concentration at 1% signals desks are treating NJ-08 as a near-certain Democratic retention and using the contract to hedge or confirm district-level seat-count models.
