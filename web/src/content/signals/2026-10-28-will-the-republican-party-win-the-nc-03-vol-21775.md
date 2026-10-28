---
signal_id: "CMSIG20261028VS04"
signal_slug: "will-the-republican-party-win-the-nc-03-vol-21775"
headline: "Republican NC-03 House seat: 56% on $21.8K surge"
semantic_title: "Republicans lead at 56% in NC-03 through a contested volume push"
telemetry: "56% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T07:50:03+00:00"
event_id: "CM-EVT-MCNRMD34V7"
event_slug: "nc-03-house-election-winner"
event_question: "Will the Republican Party candidate win the NC-03 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x515155dc9997b73728b424721ea4538cad0de3aad6dd1ceba6277e9fc882276d"
  question_raw: "Will the Republican Party win the NC-03 House seat?"
  current_price: 0.56
  volume_24h_usd: 21775.174178000005
  volume_cumulative_usd: 53172.328905
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "56% pricing gives Republicans a narrow edge but leaves the NC-03 seat genuinely competitive."
  - "Polymarket logged $21.8K in 24h, 41% of all-time volume on the Republican-win contract."
  - "Mirror surge on the Democratic contract (see Spike 5) confirms contested two-sided flow."
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
      poly_vol_24h_usd: 21775.174178000005
sources:
  - label: "ClearMarket market record: Will the Republican Party candidate win the NC-03 House"
    url: "https://clearmarket.fyi/events/nc-03-house-election-winner"
    retrieved_at: "2026-10-28T07:50:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous high-volume surges on both the Republican and Democratic NC-03 contracts indicate active two-sided trading on a tight race, desks modeling House seat counts should watch this district as a live toss-up.
