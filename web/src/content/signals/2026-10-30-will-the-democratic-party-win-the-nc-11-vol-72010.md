---
signal_id: "CMSIG20261030VS02"
signal_slug: "will-the-democratic-party-win-the-nc-11-vol-72010"
headline: "NC-11 Dems: 84% on $72K Polymarket spike"
semantic_title: "Democrats backed heavily in NC-11 as odds hit 84%"
telemetry: "84% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T07:48:50+00:00"
event_id: "CM-EVT-DFRWVBVQ98"
event_slug: "nc-11-house-election-winner"
event_question: "Who will win the NC-11 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7fd71c48a98bb515664cadb1f62cf1f27b770fe9cc1216571e183b982a48e42a"
  question_raw: "Will the Democratic Party win the NC-11 House seat?"
  current_price: 0.84
  volume_24h_usd: 72010.14379
  volume_cumulative_usd: 111000.24421799999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices Democrats winning NC-11 at 84%, the mirror of the 14% Republican contract."
  - "24h volume of $72K is 65% of all-time, most NC-11 Democratic liquidity landed today."
  - "Cross-contract activity on both NC-11 sides points to arbitrage or spread-locking near close."
  - "Resolves on NC-11 House race; note companion Spike 0 for Republican side."
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
      poly_vol_24h_usd: 72010.14379
sources:
  - label: "ClearMarket market record: Who will win the NC-11 House election?"
    url: "https://clearmarket.fyi/events/nc-11-house-election-winner"
    retrieved_at: "2026-10-30T07:48:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous spikes on both sides of the NC-11 contract suggest spread arbitrage or position squaring across venues as Election Day approaches.
