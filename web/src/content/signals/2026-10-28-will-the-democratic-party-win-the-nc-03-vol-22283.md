---
signal_id: "CMSIG20261028VS05"
signal_slug: "will-the-democratic-party-win-the-nc-03-vol-22283"
headline: "Democrat NC-03 House seat: 43% on $22.3K surge"
semantic_title: "Democrats trail at 43% in NC-03 with heavy trading on both sides"
telemetry: "43% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T07:50:03+00:00"
event_id: "CM-EVT-MCNRMD34V7"
event_slug: "nc-03-house-election-winner"
event_question: "Will the Republican Party candidate win the NC-03 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa74ddc3ce66416b679703e087afd5d2047a58a2974d7730cab76a0176eda6933"
  question_raw: "Will the Democratic Party win the NC-03 House seat?"
  current_price: 0.43
  volume_24h_usd: 22283.755998999997
  volume_cumulative_usd: 56165.92254099999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "43% odds reflect a slight Democratic deficit, consistent with the 56% Republican contract (Spike 4)."
  - "Polymarket saw $22.3K in 24h, 40% of all-time volume, nearly matching the Republican contract's surge."
  - "Paired volume on opposing contracts confirms genuine two-sided price discovery, not one-directional flow."
  - "Resolves on certified NC-03 House election result."
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
      poly_vol_24h_usd: 22283.755998999997
sources:
  - label: "ClearMarket market record: Will the Republican Party candidate win the NC-03 House"
    url: "https://clearmarket.fyi/events/nc-03-house-election-winner"
    retrieved_at: "2026-10-28T07:50:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-identical 40% all-time volume share on both sides of NC-03 confirms a contested, liquid race, desks should treat 56/43 as a live market price, not a stale estimate, given the fresh two-sided commitment.
