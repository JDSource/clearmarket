---
signal_id: "CMSIG20260606VS04"
signal_slug: "will-bitcoin-reach-100-000-in-june-vol-253184"
headline: "BTC $100K in June: 0% on $253K volume"
semantic_title: "Market writes off Bitcoin touching $100K in June"
telemetry: "0% · $253K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-06T10:01:03+00:00"
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
  - "Zero percent signals the market has fully ruled out a $100K Bitcoin print this month."
  - "$253K 24h is 85% of all-time, nearly the entire contract lifetime volume printed in one session."
  - "With Bitcoin trading well below $100K and June already underway, the move required is prohibitive."
  - "Contract likely approaching expiry; flow reflects final settlement rather than new directional conviction."
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
    retrieved_at: "2026-06-06T10:01:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 85% all-time volume concentration at 0% is a terminal settlement flush, crypto desks should note this as a clean near-term resistance ceiling being formally priced out by the market.
