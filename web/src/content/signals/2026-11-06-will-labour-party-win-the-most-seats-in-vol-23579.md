---
signal_id: "CMSIG20261106VS02"
signal_slug: "will-labour-party-win-the-most-seats-in-vol-23579"
headline: "Labour NZ most seats: 34% on $24K volume"
semantic_title: "Labour NZ most-seats bid holds well below 50%"
telemetry: "34% · $24K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T07:48:47+00:00"
event_id: "CM-EVT-DB92W53ZH3"
event_slug: "new-zealand-legislative-election-winner"
event_question: "Will the New Zealand Labour Party win the most seats in the next legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x741d99d33224258ad4536be7adbfdea7cacdaec616ce88e13755bfafde9c6d19"
  question_raw: "Will Labour Party win the most seats in the New Zealand House of Representatives in the 2026 New Zealand legislative election?"
  current_price: 0.34
  volume_24h_usd: 23579.641455999998
  volume_cumulative_usd: 70587.689513
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-07T00:00:00Z"
bullets:
  - "Polymarket prices Labour winning the most seats at 34%, leaving the field favoring other parties at 66%."
  - "24h volume of $24K is 33% of all-time volume, a meaningful but not dominant surge, reflecting building interest."
  - "Attention likely tied to tightening polling or an upcoming electoral event in New Zealand drawing fresh capital."
  - "Contract resolves on official New Zealand House of Representatives seat count after the relevant election."
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
      poly_vol_24h_usd: 23579.641455999998
sources:
  - label: "ClearMarket market record: Will the New Zealand Labour Party win the most seats in"
    url: "https://clearmarket.fyi/events/new-zealand-legislative-election-winner"
    retrieved_at: "2026-11-06T07:48:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a 34% price signals desks are testing whether Labour's underdog odds are mispriced ahead of a catalyst, worth monitoring for a price shift if news flow tightens the race.
