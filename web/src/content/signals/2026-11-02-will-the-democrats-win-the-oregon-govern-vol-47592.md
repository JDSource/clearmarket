---
signal_id: "CMSIG20261102VS05"
signal_slug: "will-the-democrats-win-the-oregon-govern-vol-47592"
headline: "Oregon Gov Dem: 84% on $48K inflow"
semantic_title: "Democrats lead the Oregon governor race by a wide margin"
telemetry: "84% · $48K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T07:49:23+00:00"
event_id: "CM-EVT-082HQ0P413"
event_slug: "oregon-governor-winner-2026"
event_question: "Oregon Governor Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8d65ff57f443011c4c10e7aa50aa54b3a3b5e2b940cb3ca97c0357bbcaee0b36"
  question_raw: "Will the Democrats win the Oregon governor race in 2026?"
  current_price: 0.84
  volume_24h_usd: 47592.132471
  volume_cumulative_usd: 140786.741293
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 84% in Oregon's 2026 governor race, a solid favorite with limited tail risk."
  - "$47.6K in 24h accounts for 34% of all-time volume, a meaningful late surge for a state-level race."
  - "Oregon has trended competitive at the gubernatorial level; 84% implies the market sees the current Democratic candidate as structurally advantaged."
  - "Resolves on 2026 Oregon gubernatorial election outcome."
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
      poly_vol_24h_usd: 47592.132471
sources:
  - label: "ClearMarket market record: Oregon Governor Election Winner"
    url: "https://clearmarket.fyi/events/oregon-governor-winner-2026"
    retrieved_at: "2026-11-02T07:49:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-third all-time volume share arriving pre-election at 84% suggests desks are pricing Oregon as a near-call but still see enough residual risk to trade the contract actively.
