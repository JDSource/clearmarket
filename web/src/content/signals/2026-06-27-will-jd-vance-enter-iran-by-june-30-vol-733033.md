---
signal_id: "CMSIG20260627VS01"
signal_slug: "will-jd-vance-enter-iran-by-june-30-vol-733033"
headline: "Vance Iran entry: 0% on $733K volume spike"
semantic_title: "Heavy flows defend the 'No' on Vance entering Iran by June 30"
telemetry: "0% · $733K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T01:36:27+00:00"
event_id: "CM-EVT-QF15YF74T9"
event_slug: "who-will-enter-iran-by-june-30"
event_question: "Will someone enter Iran by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x77eafa497fe8ff7a41f540e2920e8897540b01f06b82477d168c4a21a7f9e57a"
  question_raw: "Will JD Vance enter Iran by June 30?"
  current_price: 0.003
  volume_24h_usd: 733033.1373319998
  volume_cumulative_usd: 2598050.1104819993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Price sits at 0%, market assigns no realistic chance of entry before June 30."
  - "$733K in 24h is 28% of all-time volume, the largest single-day print on this contract."
  - "Parallel surge alongside Kushner contract suggests coordinated diplomatic-risk positioning."
  - "June 30 hard deadline; resolution imminent with three calendar days remaining."
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
      poly_vol_24h_usd: 733033.1373319998
sources:
  - label: "ClearMarket market record: Will someone enter Iran by June 30?"
    url: "https://clearmarket.fyi/events/who-will-enter-iran-by-june-30"
    retrieved_at: "2026-06-27T01:36:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous spike across both Iran-entry contracts signals desks are closing out residual tail exposure on a now-dead diplomatic scenario, not repricing a live risk.
