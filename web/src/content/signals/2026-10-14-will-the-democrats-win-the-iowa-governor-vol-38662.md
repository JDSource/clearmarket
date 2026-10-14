---
signal_id: "CMSIG20261014VS05"
signal_slug: "will-the-democrats-win-the-iowa-governor-vol-38662"
headline: "Iowa governor Dem win: 91% on $38K volume pop"
semantic_title: "Iowa governor race bets pile into Democratic side at 91%"
telemetry: "91% · $39K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T07:48:34+00:00"
event_id: "CM-EVT-5Q3L341WH8"
event_slug: "iowa-governor-winner-2026"
event_question: "Iowa Governor Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd73a3ca0e0544f2b5bd4f32fca4a7d4fb691a260b431f5afa58f52a41c13d896"
  question_raw: "Will the Democrats win the Iowa governor race in 2026?"
  current_price: 0.91
  volume_24h_usd: 38662.61541099999
  volume_cumulative_usd: 128568.37838599997
  arbitration_model: "uma_oracle"
bullets:
  - "91% price marks Democrats as overwhelming favorites in Iowa's 2026 governor race, a striking stance in a traditionally red state."
  - "24h volume of $38K is 30% of all-time handle, adding a meaningful fresh layer to an already active market."
  - "October attention may reflect Republican candidate weakness, scandal, or a strong Democratic recruitment locking in the field."
  - "Resolves on 2026 election night; a 91% price implies the market sees the GOP path as a tail risk only."
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
      poly_vol_24h_usd: 38662.61541099999
sources:
  - label: "ClearMarket market record: Iowa Governor Election Winner"
    url: "https://clearmarket.fyi/events/iowa-governor-winner-2026"
    retrieved_at: "2026-10-14T07:48:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained all-time volume plus a fresh 30% single-day inflow at 91% signals traders have significant conviction in an unusual Democratic lean in Iowa, worth flagging for any Midwest political risk desk.
