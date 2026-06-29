---
signal_id: "CMSIG20260629VS00"
signal_slug: "will-lebanon-recognize-israel-by-june-30-vol-373887"
headline: "Lebanon recognizes Israel by Jun 30: 18% on $374K"
semantic_title: "Lebanon-Israel recognition sits deep in tail-risk territory"
telemetry: "18% · $374K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T01:47:13+00:00"
event_id: "CM-EVT-C44TBGCDK8"
event_slug: "which-countries-will-recognize-israel-by-june-30"
event_question: "Will additional countries recognize Israel by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x274cec202608757e62a0cf64ec63a3a814a6cc23a1bff1819b437362c5c16732"
  question_raw: "Will Lebanon recognize Israel by June 30?"
  current_price: 0.184
  volume_24h_usd: 373887.5666909997
  volume_cumulative_usd: 547453.4186240016
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices 18%, market treats recognition as unlikely but non-trivial inside 24 hours."
  - "$374K traded in 24h, 68% of all-time volume; majority of lifetime liquidity deployed in a single session."
  - "Deadline expires tomorrow; surge signals last-hour positioning ahead of contract resolution."
  - "Resolves June 30, any diplomatic confirmation or denial closes the market within hours."
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
      poly_vol_24h_usd: 373887.5666909997
sources:
  - label: "ClearMarket market record: Will additional countries recognize Israel by June 30?"
    url: "https://clearmarket.fyi/events/which-countries-will-recognize-israel-by-june-30"
    retrieved_at: "2026-06-29T01:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as terminal-day resolution hedging, not a directional call, the 68% lifetime-in-one-day print reflects mechanical deadline arbitrage rather than fresh geopolitical intelligence.
