---
signal_id: "CMSIG20261023VS06"
signal_slug: "will-the-democratic-party-win-the-nc-09-vol-21724"
headline: "NC-09 House Dem: 26% on $22K polymarket surge"
semantic_title: "NC-09 draws fresh trading with Democrats under 25%"
telemetry: "26% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T07:49:03+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdc23b5a54616abf57d7f89f57a29dbacc0d836ab6f3994f5533c8c41ba929ebb"
  question_raw: "Will the Democratic Party win the NC-09 House seat?"
  current_price: 0.26
  volume_24h_usd: 21724.049894
  volume_cumulative_usd: 39734.665184
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "26% price puts Democrats just above the 25% threshold, still a clear underdog in NC-09."
  - "$21,724 in 24h trading equals 55% of all-time volume, more than half the market's life turned over today."
  - "NC-09 competitive district attention may reflect new polling, candidate news, or redistricting-related reassessment."
  - "Resolves on 2026 NC-09 House general election."
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
      poly_vol_24h_usd: 21724.049894
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-23T07:49:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 55% all-time volume day on a 26% Democratic contract in NC-09 suggests the market is reassessing competitiveness, worth flagging for desks modeling House majority probability, as this district sits near the margin of control scenarios.
