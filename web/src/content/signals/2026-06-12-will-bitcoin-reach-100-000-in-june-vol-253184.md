---
signal_id: "CMSIG20260612VS04"
signal_slug: "will-bitcoin-reach-100-000-in-june-vol-253184"
headline: "Bitcoin $100K in June: 0% on $253K surge"
semantic_title: "$100K Bitcoin by June sits deep in tail-risk territory"
telemetry: "0% · $253K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-12T11:42:43+00:00"
event_id: "CM-EVT-3PF6P6GGK5"
event_slug: "what-price-will-bitcoin-hit-in-june-2026"
event_question: "Will Bitcoin's price reach a specific level in June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x32f5e88162b712d8a1706451b4b52832193b2e961fe49095f873bbf44e492229"
  question_raw: "Will Bitcoin reach $100,000 in June?"
  current_price: 0.004
  volume_24h_usd: 253184.79004200047
  volume_cumulative_usd: 297806.4784230016
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-01T04:00:00Z"
bullets:
  - "0% price means the market has fully abandoned the $100K June scenario with 18 days left."
  - "$253K in 24h is 85% of all-time volume, near-total lifecycle activity compressed into one session."
  - "Surge at zero likely reflects final arbitrage sweeps and expiring long positions being closed."
  - "Resolves end of June; no realistic path priced by Polymarket participants."
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
      poly_vol_24h_usd: 253184.79004200047
sources:
  - label: "ClearMarket market record: Will Bitcoin's price reach a specific level in June?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-in-june-2026"
    retrieved_at: "2026-06-12T11:42:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 85% all-time share at a zero price is a classic terminal-wash signature, a desk can use this as a real-time sentiment gauge confirming Bitcoin spot is trading well below the $100K threshold with no near-term catalyst priced.
