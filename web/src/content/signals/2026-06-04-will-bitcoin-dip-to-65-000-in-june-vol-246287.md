---
signal_id: "CMSIG20260604VS05"
signal_slug: "will-bitcoin-dip-to-65-000-in-june-vol-246287"
headline: "BTC dips $65K in June: 87% on $246K"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-04T03:24:48+00:00"
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
  - "Polymarket prices 87% probability Bitcoin touches $65K at some point in June."
  - "$246K 24h volume equals 71% of all-time; high-conviction positioning into contract."
  - "Current BTC spot price implies $65K breach already occurred or is near-certain."
  - "Contract resolves June 30; high probability reflects observed or imminent price level."
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
    retrieved_at: "2026-06-04T03:24:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

87% probability with majority of lifetime volume in one day indicates this downside level has likely already been touched, driving confirmation trades to YES.
