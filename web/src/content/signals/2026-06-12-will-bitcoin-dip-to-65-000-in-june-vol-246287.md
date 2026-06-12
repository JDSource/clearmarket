---
signal_id: "CMSIG20260612VS05"
signal_slug: "will-bitcoin-dip-to-65-000-in-june-vol-246287"
headline: "Bitcoin dip $65K June: 87% on $246K surge"
semantic_title: "Traders stack conviction on a $65K Bitcoin dip in June"
telemetry: "87% · $246K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-12T11:42:43+00:00"
event_id: "CM-EVT-3PF6P6GGK5"
event_slug: "what-price-will-bitcoin-hit-in-june-2026"
event_question: "Will Bitcoin's price reach a specific level in June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1d5b3e1146f2f976b44314f7c8c52684f6f221420e4a6f5d6808340f4c995f7b"
  question_raw: "Will Bitcoin dip to $65,000 in June?"
  current_price: 0.87
  volume_24h_usd: 246287.95848699994
  volume_cumulative_usd: 344465.50290800014
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-01T04:00:00Z"
bullets:
  - "87% price implies the market near-fully prices a sub-$65K print before June 30."
  - "$246K in 24h is 71% of all-time, dominant single-session engagement on a bearish leg."
  - "Paired with the 0% on $100K, flows paint a consensus bearish June Bitcoin macro read."
  - "Resolves end of June on any confirmed $65K or lower daily print."
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
      poly_vol_24h_usd: 246287.95848699994
sources:
  - label: "ClearMarket market record: Will Bitcoin's price reach a specific level in June?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-in-june-2026"
    retrieved_at: "2026-06-12T11:42:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat the 87% price alongside the $100K zero as a coherent bearish Bitcoin complex, prediction-market participants are aligned on downside, which can serve as a sentiment input for crypto options desks pricing June puts.
