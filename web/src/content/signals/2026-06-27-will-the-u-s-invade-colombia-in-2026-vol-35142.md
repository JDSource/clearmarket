---
signal_id: "CMSIG20260627VS03"
signal_slug: "will-the-u-s-invade-colombia-in-2026-vol-35142"
headline: "U.S. invades Colombia 2026: 5% on $35K inflow"
semantic_title: "Heavy flows fade a U.S. invasion of Colombia in 2026"
telemetry: "5% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T10:03:08+00:00"
event_id: "CM-EVT-ZTMV2RDX49"
event_slug: "will-the-us-invade-colombia-in-2026"
event_question: "Will the U.S. invade Colombia by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x12d1f08c93c4272c0447b5aebfabc3b4901588615128d6d91d0e04a1e7031d3a"
  question_raw: "Will the U.S. invade Colombia in 2026?"
  current_price: 0.047
  volume_24h_usd: 35142.318199
  volume_cumulative_usd: 138018.01253200008
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket at 5%, market assigns deep tail probability despite ongoing bilateral friction."
  - "$35K in 24h is 25% of all-time volume; renewed attention without meaningful price support."
  - "Cartel-designation tensions and trade rhetoric have periodically refreshed this market; 5% reflects noise, not conviction."
  - "Full-year resolution; sustained low price suggests inflows are fading a narrative rather than building one."
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
      poly_vol_24h_usd: 35142.318199
sources:
  - label: "ClearMarket market record: Will the U.S. invade Colombia by the end of 2026?"
    url: "https://clearmarket.fyi/events/will-the-us-invade-colombia-in-2026"
    retrieved_at: "2026-06-27T10:03:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume spike without price movement is a classic fade signal, desks are absorbing speculative longs at a price they consider generous, reinforcing the low-probability consensus.
