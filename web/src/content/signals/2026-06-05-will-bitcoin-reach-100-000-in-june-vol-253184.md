---
signal_id: "CMSIG20260605VS04"
signal_slug: "will-bitcoin-reach-100-000-in-june-vol-253184"
headline: "Bitcoin $100K in June: 0% on $253K surge"
semantic_title: "Market fades Bitcoin reaching $100K in June to zero"
telemetry: "0% · $253K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-05T11:24:46+00:00"
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
  - "Polymarket prices Bitcoin touching $100K in June at 0%, market has effectively closed the door."
  - "24h volume of $253K is 85% of the contract's entire all-time handle, an outsized terminal flush."
  - "With Bitcoin currently well below $100K and June nearly half over, the contract is likely past any realistic probability window."
  - "Flows are mechanical settlement positioning, not a fresh directional view on Bitcoin price trajectory."
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
    retrieved_at: "2026-06-05T11:24:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Eighty-five percent of all-time volume in a single day at zero price is a classic expiry sweep, the desk takeaway is that the $100K June strike is dead, and attention should shift to July or Q3 strike contracts.
