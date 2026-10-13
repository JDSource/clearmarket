---
signal_id: "CMSIG20261013VS02"
signal_slug: "will-the-democratic-party-win-the-ny-23-vol-16741"
headline: "NY-23 Democrat: 3% on $17K Polymarket inflow"
semantic_title: "NY-23 Democratic odds stay near zero through a volume surge"
telemetry: "3% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T07:49:07+00:00"
event_id: "CM-EVT-K34TZHDVH7"
event_slug: "ny-23-house-election-winner"
event_question: "NY-23 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6098d023d47306dbb9d9b41675038f09b47718e4e833e46599bef3ae338dbb35"
  question_raw: "Will the Democratic Party win the NY-23 House seat?"
  current_price: 0.027
  volume_24h_usd: 16741.195715
  volume_cumulative_usd: 32291.367899000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic win in NY-23 at just 3%, treating the seat as a heavy Republican hold."
  - "24h volume of $17K is 52% of all-time, majority of lifetime handle landed in a single session."
  - "Fresh activity at near-zero odds suggests traders are either topping off short-Democrat exposure or testing the floor."
  - "Resolves on the NY-23 general election result."
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
      poly_vol_24h_usd: 16741.195715
sources:
  - label: "ClearMarket market record: NY-23 House Election Winner"
    url: "https://clearmarket.fyi/events/ny-23-house-election-winner"
    retrieved_at: "2026-10-13T07:49:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume at a 3% price in a nominally uncompetitive seat warrants attention, desks should note whether this reflects cross-market hedging on a House-control basket or a genuine read on last-minute competitiveness.
