---
signal_id: "CMSIG20261107VS01"
signal_slug: "will-national-party-win-the-most-seats-i-vol-150294"
headline: "NZ National most seats: 57% on $150K volume spike"
semantic_title: "Traders pile into National Party leading the New Zealand House"
telemetry: "57% · $150K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T07:49:22+00:00"
event_id: "CM-EVT-DB92W53ZH3"
event_slug: "new-zealand-legislative-election-winner"
event_question: "Will the New Zealand Labour Party win the most seats in the next legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xba155b6be6cabf93bf31dfcc56fe2f4e3e88d16b0d490319c635930f2d9fbd04"
  question_raw: "Will National Party win the most seats in the New Zealand House of Representatives in the 2026 New Zealand legislative election?"
  current_price: 0.57
  volume_24h_usd: 150294.94476799996
  volume_cumulative_usd: 247004.18791799998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-07T00:00:00Z"
bullets:
  - "57% pricing gives National a modest but clear plurality edge over Labour."
  - "Polymarket sees $150K in 24h, 61% of all-time, signaling sharp fresh attention."
  - "Paired surge with Spike 2 (Labour at 44%) confirms NZ election is active catalyst."
  - "Resolution tied to official New Zealand general election seat count."
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
      poly_vol_24h_usd: 150294.94476799996
sources:
  - label: "ClearMarket market record: Will the New Zealand Labour Party win the most seats in"
    url: "https://clearmarket.fyi/events/new-zealand-legislative-election-winner"
    retrieved_at: "2026-11-07T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous surge across both NZ party contracts tells a desk that a fresh poll or election-cycle event is driving rapid position-taking, with the market settling on National as the slight plurality favourite.
