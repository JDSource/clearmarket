---
signal_id: "CMSIG20261014VS05"
signal_slug: "will-the-democrats-win-the-iowa-governor-vol-38377"
headline: "Dem Iowa governor win: 91% on $38K volume pickup"
semantic_title: "Iowa governor odds hold strong for Democrats on fresh volume"
telemetry: "91% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T13:17:59+00:00"
event_id: "CM-EVT-5Q3L341WH8"
event_slug: "iowa-governor-winner-2026"
event_question: "Iowa Governor Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd73a3ca0e0544f2b5bd4f32fca4a7d4fb691a260b431f5afa58f52a41c13d896"
  question_raw: "Will the Democrats win the Iowa governor race in 2026?"
  current_price: 0.91
  volume_24h_usd: 38377.813754
  volume_cumulative_usd: 128705.02672899999
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices 91%, heavy Democratic favoritism baked into the Iowa governor contract."
  - "$38K in 24h is 30% of all-time volume on a $128K contract, a steady mid-cycle liquidity addition."
  - "Iowa governor race drawing fresh capital as the broader 2026 gubernatorial map comes into focus."
  - "Resolves on 2026 Iowa gubernatorial election result."
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
      poly_vol_24h_usd: 38377.813754
sources:
  - label: "ClearMarket market record: Iowa Governor Election Winner"
    url: "https://clearmarket.fyi/events/iowa-governor-winner-2026"
    retrieved_at: "2026-10-14T13:17:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Steady volume accumulation at 91% in Iowa suggests capital is building a position rather than reacting to a single catalyst, worth tracking for any Republican development that could compress the price.
