---
signal_id: "CMSIG20261018VS01"
signal_slug: "will-the-republican-party-win-the-nc-11-vol-16982"
headline: "NC-11 GOP win: 17% as $17K floods the contract"
semantic_title: "NC-11 Republican odds slip to 17% under heavy volume"
telemetry: "17% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-18T07:48:11+00:00"
event_id: "CM-EVT-DFRWVBVQ98"
event_slug: "nc-11-house-election-winner"
event_question: "Who will win the NC-11 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe64ec54460a1f1b250c9785968e6ebecfb0fd542a34300a161f64460c7a811df"
  question_raw: "Will the Republican Party win the NC-11 House seat?"
  current_price: 0.17
  volume_24h_usd: 16982.062131
  volume_cumulative_usd: 30464.597665
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket has the Republican NC-11 candidate at just 17%, reflecting a strong Democratic lean in the district."
  - "24h volume of $17K is 56% of all-time contract volume, more than half of lifetime activity hit in one session."
  - "The surge alongside a low Republican price signals fresh conviction that this seat is trending Democratic."
  - "Resolves on the NC-11 House race; paired directly with Spike 2 on the Democratic side of the same contract."
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
      poly_vol_24h_usd: 16982.062131
sources:
  - label: "ClearMarket market record: Who will win the NC-11 House election?"
    url: "https://clearmarket.fyi/events/nc-11-house-election-winner"
    retrieved_at: "2026-10-18T07:48:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The paired volume across both NC-11 contracts tells a desk that new money is actively repricing this race as a likely Democratic pickup, worth monitoring for corroborating polling.
