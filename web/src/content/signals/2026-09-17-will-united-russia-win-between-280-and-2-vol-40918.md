---
signal_id: "CMSIG20260917VS07"
signal_slug: "will-united-russia-win-between-280-and-2-vol-40918"
headline: "United Russia 280-294 seats: 3% on $41K"
semantic_title: "United Russia winning 280-294 Duma seats trades near zero"
telemetry: "3% · $41K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-17T13:05:20+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x070312637ff200867e1316b2a4e31c7f2492610c78dd0851608c23f6ef9f3d7a"
  question_raw: "Will United Russia win between 280 and 294 seats in the next Russian State Duma election?"
  current_price: 0.033
  volume_24h_usd: 40918.448335
  volume_cumulative_usd: 113804.10734700001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices just a 3% chance United Russia lands in the 280-294 seat band, near-zero probability."
  - "$41K in 24h is 36% of all-time volume, reflecting fresh but modest engagement on a tail scenario."
  - "The narrow seat range makes this a precision bet; broader United Russia dominance is likely priced elsewhere."
  - "Resolves upon official Russian State Duma election results."
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
      poly_vol_24h_usd: 40918.448335
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-17T13:05:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-zero pricing with meaningful volume suggests traders are using the contract to hedge or express a view on the precision of United Russia's margin, not its outright majority.
