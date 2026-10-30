---
signal_id: "CMSIG20261030VS00"
signal_slug: "will-the-republican-party-win-the-nc-11-vol-128819"
headline: "NC-11 GOP seat: 14% on $129K surge"
semantic_title: "NC-11 Republican long shot holds at 14%"
telemetry: "14% · $129K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T07:48:50+00:00"
event_id: "CM-EVT-DFRWVBVQ98"
event_slug: "nc-11-house-election-winner"
event_question: "Who will win the NC-11 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe64ec54460a1f1b250c9785968e6ebecfb0fd542a34300a161f64460c7a811df"
  question_raw: "Will the Republican Party win the NC-11 House seat?"
  current_price: 0.14
  volume_24h_usd: 128819.79625200001
  volume_cumulative_usd: 170949.30229600004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices Republicans out of NC-11 at just 14%, signaling near-certain Democratic hold."
  - "24h volume of $129K is 75% of all-time, the bulk of lifetime liquidity arrived today."
  - "Surge this close to Election Day suggests final-day positioning, not speculative drift."
  - "Contract resolves on NC-11 House race outcome; election day imminent."
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
      poly_vol_24h_usd: 128819.79625200001
sources:
  - label: "ClearMarket market record: Who will win the NC-11 House election?"
    url: "https://clearmarket.fyi/events/nc-11-house-election-winner"
    retrieved_at: "2026-10-30T07:48:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-total concentration of all-time volume in 24 hours on a 14% contract signals desks are closing out residual Republican exposure in NC-11 ahead of results.
