---
signal_id: "CMSIG20261016VS02"
signal_slug: "will-the-democratic-party-win-the-wi-07-vol-15547"
headline: "WI-07 Dem seat: 4% on $15K volume burst"
semantic_title: "WI-07 Democratic win priced out at 4%"
telemetry: "4% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-16T12:59:44+00:00"
event_id: "CM-EVT-Y39KV4JZ48"
event_slug: "wi-07-house-election-winner"
event_question: "Will the Democratic Party win the WI-07 House seat?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x13b9606ad402c20bab0badf41eba042a2784bfdfbf5bfa95572f80da13b499dc"
  question_raw: "Will the Democratic Party win the WI-07 House seat?"
  current_price: 0.035
  volume_24h_usd: 15547.350255
  volume_cumulative_usd: 49231.106485000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket holds Democrats at 4% in WI-07, market treats the seat as effectively off the board."
  - "24h volume of $15K is 32% of all-time contract flow, a notable mid-cycle acceleration."
  - "Paired spike with FL-18 at identical odds suggests broad House seat scanning, not district-specific news."
  - "Resolves on November 2026 general election outcome."
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
      poly_vol_24h_usd: 15547.350255
sources:
  - label: "ClearMarket market record: Will the Democratic Party win the WI-07 House seat?"
    url: "https://clearmarket.fyi/events/wi-07-house-election-winner"
    retrieved_at: "2026-10-16T12:59:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes in multiple deep-red House districts at near-zero Democratic odds point to portfolio-level House control hedging rather than any single district catalyst.
