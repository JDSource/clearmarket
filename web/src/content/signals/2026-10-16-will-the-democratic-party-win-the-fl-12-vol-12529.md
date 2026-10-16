---
signal_id: "CMSIG20261016VS03"
signal_slug: "will-the-democratic-party-win-the-fl-12-vol-12529"
headline: "FL-12 Democrat: 5% on $12K Polymarket inflow"
semantic_title: "Trading picks up on the FL-12 Democratic long shot at 5%"
telemetry: "5% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-16T07:48:37+00:00"
event_id: "CM-EVT-5MPVYCWL84"
event_slug: "fl-12-house-election-winner"
event_question: "Will the Republican or Democratic candidate win the FL-12 House Election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x144e24d919c77093a495211c3439c98726ec9500283b0fed336c417933021181"
  question_raw: "Will the Democratic Party win the FL-12 House seat?"
  current_price: 0.05
  volume_24h_usd: 12529.022142
  volume_cumulative_usd: 47739.200539000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic win in FL-12 at 5%, keeping the Tampa-area seat firmly in the Republican column."
  - "The 24h volume of $12K is 26% of all-time contract volume, a meaningful single-day share for a low-liquidity market."
  - "Alongside FL-18 activity today, paired Florida district volume spikes may indicate coordinated House-map repricing or hedging."
  - "Resolves on November 2026 House general election results."
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
      poly_vol_24h_usd: 12529.022142
sources:
  - label: "ClearMarket market record: Will the Republican or Democratic candidate win the FL-"
    url: "https://clearmarket.fyi/events/fl-12-house-election-winner"
    retrieved_at: "2026-10-16T07:48:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes in FL-12 and FL-18 at near-identical odds levels suggest desks are running Florida House district sweeps, likely as part of chamber-control scenario analysis rather than conviction on individual seats.
