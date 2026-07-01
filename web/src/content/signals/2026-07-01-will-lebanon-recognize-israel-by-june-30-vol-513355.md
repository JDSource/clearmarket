---
signal_id: "CMSIG20260701VS01"
signal_slug: "will-lebanon-recognize-israel-by-june-30-vol-513355"
headline: "Lebanon recognizes Israel: 3% on $513K inflow"
semantic_title: "Heavy flows discount Lebanon-Israel recognition after June 30"
telemetry: "3% · $513K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-01T11:21:48+00:00"
event_id: "CM-EVT-C44TBGCDK8"
event_slug: "which-countries-will-recognize-israel-by-june-30"
event_question: "Will additional countries recognize Israel by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x274cec202608757e62a0cf64ec63a3a814a6cc23a1bff1819b437362c5c16732"
  question_raw: "Will Lebanon recognize Israel by June 30?"
  current_price: 0.032
  volume_24h_usd: 513355.5511389999
  volume_cumulative_usd: 1455155.1005109984
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket at 3%, market treats formal Lebanon-Israel recognition as a near-dead outcome."
  - "$513K in 24h represents 35% of all-time volume, a substantial single-session directional flush."
  - "June 30 deadline has now passed; capital is repricing the miss and positioning for NO resolution."
  - "Contract resolves imminently; flows reflect late hedgers and arb desks closing exposure."
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
      poly_vol_24h_usd: 513355.5511389999
sources:
  - label: "ClearMarket market record: Will additional countries recognize Israel by June 30?"
    url: "https://clearmarket.fyi/events/which-countries-will-recognize-israel-by-june-30"
    retrieved_at: "2026-07-01T11:21:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume spike at deadline expiry and a 3% price together indicate late-stage resolution arb rather than fresh geopolitical conviction, the normalization trade is effectively priced out.
