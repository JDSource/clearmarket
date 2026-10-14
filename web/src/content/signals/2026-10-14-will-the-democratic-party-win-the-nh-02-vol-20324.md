---
signal_id: "CMSIG20261014VS04"
signal_slug: "will-the-democratic-party-win-the-nh-02-vol-20324"
headline: "NH-02 Dem seat: 96% on $20K concentrated surge"
semantic_title: "NH-02 Democratic seat priced near certain, volume spikes"
telemetry: "96% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T07:48:34+00:00"
event_id: "CM-EVT-4NDJ6QGJ77"
event_slug: "nh-02-house-election-winner"
event_question: "Who will win the New Hampshire 2nd Congressional District House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1790d20eab125a64b999fe78dd91eb8ed116a20d87dd782fad9f45a1f7b4dd58"
  question_raw: "Will the Democratic Party win the NH-02 House seat?"
  current_price: 0.959
  volume_24h_usd: 20324.184412
  volume_cumulative_usd: 30452.183085999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "96% price leaves almost no room for a Republican path, Polymarket treats this New Hampshire seat as effectively decided."
  - "24h volume of $20K is 67% of all-time handle, a dominant single-session move on a relatively thin contract."
  - "Spike on a near-certain outcome suggests a specific news item, candidate withdrawal, filing deadline, or court ruling, may have triggered positioning."
  - "Resolves 2026 election night; contract has little repricing room absent a dramatic candidate-level development."
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
      poly_vol_24h_usd: 20324.184412
sources:
  - label: "ClearMarket market record: Who will win the New Hampshire 2nd Congressional Distri"
    url: "https://clearmarket.fyi/events/nh-02-house-election-winner"
    retrieved_at: "2026-10-14T07:48:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 67% all-time share at 96% probability on a thin contract is an unusually concentrated signal, desks should check for a candidate or ballot eligibility development that prompted traders to close out residual uncertainty.
