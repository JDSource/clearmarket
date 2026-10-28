---
signal_id: "CMSIG20261028VS04"
signal_slug: "will-the-democratic-party-win-the-nc-09-vol-72439"
headline: "Dems NC-09 House seat: 33% on $72K surge"
semantic_title: "Democrats trail in NC-09 as heavy trading tests the 33% line"
telemetry: "33% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T14:50:28+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdc23b5a54616abf57d7f89f57a29dbacc0d836ab6f3994f5533c8c41ba929ebb"
  question_raw: "Will the Democratic Party win the NC-09 House seat?"
  current_price: 0.33
  volume_24h_usd: 72439.838701
  volume_cumulative_usd: 165565.27022900002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats at 33% in NC-09, a clear underdog read in a competitive swing district."
  - "44% of all-time volume, $72K, cleared in 24 hours, signaling renewed attention on the race."
  - "Volume at this stage of the cycle often precedes polling releases, candidate news, or late ad-spending data."
  - "Resolves on the certified NC-09 House election result."
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
      poly_vol_24h_usd: 72439.838701
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-28T14:50:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume burst on a 33% Democratic price warrants monitoring for incoming district-level data that could move odds sharply in either direction.
