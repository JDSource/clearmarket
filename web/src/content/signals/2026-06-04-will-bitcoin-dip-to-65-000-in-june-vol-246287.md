---
signal_id: "CMSIG20260604VS05"
signal_slug: "will-bitcoin-dip-to-65-000-in-june-vol-246287"
headline: "BTC dip to $65K in June: 87% on $246K"
semantic_title: "Bitcoin touching $65K in June nears full pricing on flows"
telemetry: "87% · $246K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-04T11:15:28+00:00"
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
  - "Polymarket prices 87% probability Bitcoin touches $65K or below during June 2026."
  - "Polymarket: $246K 24h, 71% of $344K all-time; strong conviction flow in compressed window."
  - "Implies current BTC spot is near or below $65K, or trajectory strongly points there within June."
  - "Contract expires end of June; 87% reflects broad market consensus on downside range."
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
    retrieved_at: "2026-06-04T11:15:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

87% probability with 71% of all-time volume signals the crypto desk consensus is firmly positioned for BTC trading at or through $65K this month, implying significant spot weakness.
