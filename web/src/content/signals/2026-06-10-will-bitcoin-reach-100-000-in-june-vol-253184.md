---
signal_id: "CMSIG20260610VS04"
signal_slug: "will-bitcoin-reach-100-000-in-june-vol-253184"
headline: "Bitcoin $100K in June: 0% on $253K surge"
semantic_title: "Bitcoin's $100K June target written off by exhausted bulls"
telemetry: "0% · $253K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-10T11:37:24+00:00"
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
  - "Zero probability priced, market has fully discounted a Bitcoin rally to $100K before June 30."
  - "$253K in 24h is 85% of all-time volume; near-total lifetime activity concentrated in this session."
  - "With June more than half elapsed and BTC apparently well below $100K, contract is near expiry resolution."
  - "Polymarket contract resolves end of June; capital locking in NO settlement at minimal cost."
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
    retrieved_at: "2026-06-10T11:37:24+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

85% of lifetime volume printing at 0% is a terminal-settlement signature, this is arb-driven cleanup, not new directional bitcoin positioning, and confirms the $100K June level is a dead thesis.
