---
signal_id: "CMSIG20260628VS01"
signal_slug: "will-lebanon-recognize-israel-by-june-30-vol-207205"
headline: "Lebanon recognizes Israel: 54% on $207K spike"
semantic_title: "Lebanon, Israel recognition bid sits at even-money into deadline"
telemetry: "54% · $207K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:25:52+00:00"
event_id: "CM-EVT-C44TBGCDK8"
event_slug: "which-countries-will-recognize-israel-by-june-30"
event_question: "Will additional countries recognize Israel by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x274cec202608757e62a0cf64ec63a3a814a6cc23a1bff1819b437362c5c16732"
  question_raw: "Will Lebanon recognize Israel by June 30?"
  current_price: 0.537
  volume_24h_usd: 207205.8006660001
  volume_cumulative_usd: 287649.828086
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket marks Lebanon, Israel formal recognition at 54%, a coin-flip with two days remaining."
  - "$207K in 24h represents 72% of all-time volume, signaling a late-breaking conviction shift."
  - "Normalization framework talks and U.S. brokerage efforts have accelerated; fresh attention implies near-term diplomatic movement."
  - "Resolves June 30; binary outcome makes price highly sensitive to any communiqué in the next 48 hours."
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
      poly_vol_24h_usd: 207205.8006660001
sources:
  - label: "ClearMarket market record: Will additional countries recognize Israel by June 30?"
    url: "https://clearmarket.fyi/events/which-countries-will-recognize-israel-by-june-30"
    retrieved_at: "2026-06-28T10:25:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 72% all-time volume concentration into the final 48 hours at 54% signals desks are actively hedging diplomatic exposure, the extreme recency of the flow suggests informed or reactive positioning on a real-time negotiating timeline.
