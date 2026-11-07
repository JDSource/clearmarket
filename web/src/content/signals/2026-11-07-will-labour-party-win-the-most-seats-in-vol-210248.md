---
signal_id: "CMSIG20261107VS02"
signal_slug: "will-labour-party-win-the-most-seats-in-vol-210248"
headline: "NZ Labour most seats: 1% on $210K inflow"
semantic_title: "Labour NZ most-seats odds stay near zero through fresh volume"
telemetry: "1% · $210K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T14:39:51+00:00"
event_id: "CM-EVT-DB92W53ZH3"
event_slug: "new-zealand-legislative-election-winner"
event_question: "Will the New Zealand Labour Party win the most seats in the next legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x741d99d33224258ad4536be7adbfdea7cacdaec616ce88e13755bfafde9c6d19"
  question_raw: "Will Labour Party win the most seats in the New Zealand House of Representatives in the 2026 New Zealand legislative election?"
  current_price: 0.012
  volume_24h_usd: 210248.76537200002
  volume_cumulative_usd: 289408.91242
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-07T00:00:00Z"
bullets:
  - "Polymarket prices Labour winning the most NZ House seats at just 1%, market treats this as near-impossible."
  - "$210K in 24h is 73% of all-time volume, mirroring the simultaneous National Party spike (Spike 1)."
  - "Paired volume across both contracts signals active re-pricing or position flattening on the same underlying event."
  - "Resolution tied to official NZ seat allocation."
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
      poly_vol_24h_usd: 210248.76537200002
sources:
  - label: "ClearMarket market record: Will the New Zealand Labour Party win the most seats in"
    url: "https://clearmarket.fyi/events/new-zealand-legislative-election-winner"
    retrieved_at: "2026-11-07T14:39:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous Labour and National volume spikes are two sides of the same trade; a desk should read this as market participants closing out or rebalancing NZ election exposure rather than a new directional view.
