---
signal_id: "CMSIG20260627VS03"
signal_slug: "will-gold-gc-settle-at-6-200-in-june-vol-130942"
headline: "Gold >$6,200 June settle: 0% on $131K"
semantic_title: "Gold $6,200 June settle written off with three days left"
telemetry: "0% · $131K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T01:36:27+00:00"
event_id: "CM-EVT-W8SF1QWYB1"
event_slug: "gc-settle-jun-2026"
event_question: "Will Gold (GC) settle at $5,800-$6,200 in June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7d4227c3c4f79de22bbf5b10301d3e99733151de11a2af04ee5d4fe9147fdb94"
  question_raw: "Will Gold (GC) settle at >$6,200 in June?"
  current_price: 0.001
  volume_24h_usd: 130942.61
  volume_cumulative_usd: 348697.6980530001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T17:30:00Z"
bullets:
  - "Polymarket prices zero chance of GC front-month settling above $6,200 in June."
  - "$131K in 24h is 38% of all-time contract volume, heavy terminal flow."
  - "Gold spot trading well below $6,200; the level would require an unprecedented single-session move."
  - "Final June settlement days are imminent, volume is expiry cleanup, not a macro repricing."
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
      poly_vol_24h_usd: 130942.61
sources:
  - label: "ClearMarket market record: Will Gold (GC) settle at $5,800-$6,200 in June?"
    url: "https://clearmarket.fyi/events/gc-settle-jun-2026"
    retrieved_at: "2026-06-27T01:36:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The flow here is purely mechanical end-of-month contract settlement; no macro signal for gold desks beyond confirmation that $6,200 was never a live consensus target for June.
