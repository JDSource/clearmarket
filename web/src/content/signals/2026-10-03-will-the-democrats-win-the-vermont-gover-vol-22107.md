---
signal_id: "CMSIG20261003VS03"
signal_slug: "will-the-democrats-win-the-vermont-gover-vol-22107"
headline: "Democrat VT governor: 20% on $22K surge"
semantic_title: "Democrats slip to long-shot odds in Vermont governor race"
telemetry: "20% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T07:48:19+00:00"
event_id: "CM-EVT-R85JKZZ4R6"
event_slug: "vermont-governor-winner-2026"
event_question: "Will the Vermont Governor election be won by the Democratic candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5dacb3919e3eb6372770cba85c42e0f980ddf18b1a767751de700ee272269233"
  question_raw: "Will the Democrats win the Vermont governor race in 2026?"
  current_price: 0.198
  volume_24h_usd: 22107.515570000003
  volume_cumulative_usd: 79183.507211
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democratic win at 20%, mirror of the Republican contract, confirming the GOP is a clear favorite at roughly 4-to-1."
  - "24h volume of $22K is 28% of all-time activity, running in tandem with the Republican-side contract spike."
  - "Simultaneous volume across both sides of the Vermont governor market suggests active two-sided price discovery, not one-directional flow."
  - "Resolves on 2026 Vermont general election certified result."
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
      poly_vol_24h_usd: 22107.515570000003
sources:
  - label: "ClearMarket market record: Will the Vermont Governor election be won by the Democr"
    url: "https://clearmarket.fyi/events/vermont-governor-winner-2026"
    retrieved_at: "2026-10-03T07:48:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The paired spike across Republican and Democratic Vermont governor contracts on the same day signals active arbitrage or rebalancing, a desk should watch for a new poll or endorsement driving both sides simultaneously.
