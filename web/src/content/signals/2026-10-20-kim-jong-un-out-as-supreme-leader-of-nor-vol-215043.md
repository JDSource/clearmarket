---
signal_id: "CMSIG20261020VS00"
signal_slug: "kim-jong-un-out-as-supreme-leader-of-nor-vol-215043"
headline: "Kim Jong Un out by Dec 31: 5% on $215K surge"
semantic_title: "Kim Jong Un exit by year-end stays a long shot at 5%"
telemetry: "5% · $215K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T07:48:28+00:00"
event_id: "CM-EVT-HR6HRVY940"
event_slug: "kim-jong-un-out-as-supreme-leader-of-north-korea-before-2027"
event_question: "Will Kim Jong Un no longer be the Supreme Leader of North Korea by December 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9ed2a24391123c685db5c48ea043ee9bd714a144be4a9a0c48d146d521cf9f93"
  question_raw: "Kim Jong Un out as Supreme Leader of North Korea by December 31, 2026?"
  current_price: 0.052
  volume_24h_usd: 215043.90118000004
  volume_cumulative_usd: 417707.738877
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices only 5% odds on Kim Jong Un losing power by December 31, 2026, a near-dismissal of regime change."
  - "$215K traded in 24h is 51% of all-time volume on Polymarket, signaling an extraordinary single-session mobilization."
  - "Fresh attention at this scale typically precedes a credible intelligence signal or regional provocation, desks should monitor."
  - "Contract resolves December 31, 2026; current pricing implies the market is not yet buying any specific catalyst."
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
      poly_vol_24h_usd: 215043.90118000004
sources:
  - label: "ClearMarket market record: Will Kim Jong Un no longer be the Supreme Leader of Nor"
    url: "https://clearmarket.fyi/events/kim-jong-un-out-as-supreme-leader-of-north-korea-before-2027"
    retrieved_at: "2026-10-20T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority of all lifetime volume hitting in one session on a 5% contract suggests a sharp intelligence or media trigger is being priced out, not in, worth flagging for geopolitical risk desks.
