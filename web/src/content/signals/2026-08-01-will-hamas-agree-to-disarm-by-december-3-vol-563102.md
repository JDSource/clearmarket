---
signal_id: "CMSIG20260801VS00"
signal_slug: "will-hamas-agree-to-disarm-by-december-3-vol-563102"
headline: "Hamas disarmament by Dec 31: 67% on $563K surge"
semantic_title: "Traders pile into Hamas disarmament by Dec 31 at 67%"
telemetry: "67% · $563K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-01T09:55:41+00:00"
event_id: "CM-EVT-NGWGHQ31H1"
event_slug: "will-hamaz-disarm-by-december-31"
event_question: "Will Hamas agree to disarm by the end of this year?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1e5204036bd51e6ca0e0da6221319c5839bd9940782adc6d0f6fa703aa8a3bf4"
  question_raw: "Will Hamas agree to disarm by December 31?"
  current_price: 0.67
  volume_24h_usd: 563102.757506
  volume_cumulative_usd: 958242.5111519997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T20:00:00Z"
bullets:
  - "Market prices 67% odds Hamas agrees to disarm by December 31, a majority-confidence read on a deal."
  - "24h volume of $563K equals 59% of all-time flow, signaling a decisive single-session conviction shift."
  - "Surge likely tracks fresh ceasefire or hostage-deal framework reporting demanding a disarmament clause."
  - "Resolves December 31, 2026; any breakdown in talks would reprice sharply lower."
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
      poly_vol_24h_usd: 563102.757506
sources:
  - label: "ClearMarket market record: Will Hamas agree to disarm by the end of this year?"
    url: "https://clearmarket.fyi/events/will-hamaz-disarm-by-december-31"
    retrieved_at: "2026-08-01T09:55:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-majority of all-time volume landing in one session tells a desk that a specific diplomatic development, likely a reported disarmament term in active negotiations, has triggered directional conviction, not just noise.
