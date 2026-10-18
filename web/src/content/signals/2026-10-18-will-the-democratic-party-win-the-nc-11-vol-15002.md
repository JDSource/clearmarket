---
signal_id: "CMSIG20261018VS02"
signal_slug: "will-the-democratic-party-win-the-nc-11-vol-15002"
headline: "NC-11 Dem win: 80% on $15K single-session spike"
semantic_title: "Democratic NC-11 win stays above 75% through volume surge"
telemetry: "80% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-18T07:48:11+00:00"
event_id: "CM-EVT-DFRWVBVQ98"
event_slug: "nc-11-house-election-winner"
event_question: "Who will win the NC-11 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7fd71c48a98bb515664cadb1f62cf1f27b770fe9cc1216571e183b982a48e42a"
  question_raw: "Will the Democratic Party win the NC-11 House seat?"
  current_price: 0.8
  volume_24h_usd: 15002.906302
  volume_cumulative_usd: 26904.630376999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices Democratic NC-11 win at 80%, well above the 75% threshold, strong implied probability of a flip."
  - "24h volume of $15K is 56% of all-time contract volume, mirroring the simultaneous Republican-side surge."
  - "Coordinated volume across both sides of NC-11 points to a fresh repricing event, likely driven by new polling or candidate news."
  - "Resolves on the NC-11 House race outcome; high odds here are the direct mirror of Spike 1's 17% Republican read."
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
      poly_vol_24h_usd: 15002.906302
sources:
  - label: "ClearMarket market record: Who will win the NC-11 House election?"
    url: "https://clearmarket.fyi/events/nc-11-house-election-winner"
    retrieved_at: "2026-10-18T07:48:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Back-to-back sessions of heavy two-sided NC-11 volume at 80/17 is a strong signal for a desk that this race has moved materially Democratic, potential catalyst warrants a news check.
