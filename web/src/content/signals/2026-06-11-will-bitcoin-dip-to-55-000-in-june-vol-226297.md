---
signal_id: "CMSIG20260611VS06"
signal_slug: "will-bitcoin-dip-to-55-000-in-june-vol-226297"
headline: "Bitcoin dip to $55K: 14% on $226K volume"
semantic_title: "Tail-risk flows probe a Bitcoin $55K dip in June"
telemetry: "14% · $226K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-11T12:08:47+00:00"
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
  - "14% price on Polymarket marks a $55K June touch as a live tail risk, not consensus."
  - "$226K in 24h covers 75% of all-time volume, contract suddenly material after minimal prior activity."
  - "Correlation with $65K contract surge suggests a cohort is hedging a cascading breakdown scenario."
  - "Resolves end of June; a close above $65K through month-end would rapidly collapse this to near zero."
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
    retrieved_at: "2026-06-11T12:08:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes across $65K and $55K strikes tell a desk that hedgers are building layered downside protection, a structured bear scenario, not random retail flow.
