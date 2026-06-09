---
signal_id: "CMSIG20260609VS06"
signal_slug: "will-bitcoin-dip-to-55-000-in-june-vol-226297"
headline: "Bitcoin $55K dip in June: 14% on $226K"
semantic_title: "Capital stacks against a $55K Bitcoin floor in June"
telemetry: "14% · $226K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-09T10:58:29+00:00"
event_id: "CM-EVT-3PF6P6GGK5"
event_slug: "what-price-will-bitcoin-hit-in-june-2026"
event_question: "Will Bitcoin's price reach a specific level in June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xadebd6bbf401c9509dd2e78b65a16b567f1f386dccd8cac86cd389bb53ec3a58"
  question_raw: "Will Bitcoin dip to $55,000 in June?"
  current_price: 0.138
  volume_24h_usd: 226297.9937449999
  volume_cumulative_usd: 300883.1541469998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-01T04:00:00Z"
bullets:
  - "Polymarket prices 14% odds Bitcoin falls to $55K before June 30, a meaningful but tail risk."
  - "$226K in 24h is 75% of all-time volume, a sharp concentration of capital debating a deep dip."
  - "Paired with the 87% $65K contract, traders see substantial downside risk stopping well above $55K."
  - "June 30 resolution; 14% implies one-in-seven chance of an additional roughly $10K leg down from $65K."
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
      poly_vol_24h_usd: 226297.9937449999
sources:
  - label: "ClearMarket market record: Will Bitcoin's price reach a specific level in June?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-in-june-2026"
    retrieved_at: "2026-06-09T10:58:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $55K contract's 14% price alongside the $65K contract's 87% price draws a precise market-implied range, desks can extract an implied probability distribution for Bitcoin's June floor from these two contracts together.
