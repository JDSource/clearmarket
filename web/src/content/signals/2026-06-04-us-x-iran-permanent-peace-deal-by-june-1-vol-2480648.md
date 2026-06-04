---
signal_id: "CMSIG20260604VS01"
signal_slug: "us-x-iran-permanent-peace-deal-by-june-1-vol-2480648"
headline: "US-Iran permanent peace: 14% on $2.5M surge"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-04T11:15:28+00:00"
event_id: "CM-EVT-TQTJ2MLTV8"
event_slug: "us-x-iran-permanent-peace-deal-by"
event_question: "US x Iran permanent peace deal by May 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd86a816093fcd0a0e1ca440bc5ce199bd3c5a8d6139e044b076958164f8c5423"
  question_raw: "US x Iran permanent peace deal by June 15, 2026?"
  current_price: 0.14
  volume_24h_usd: 2480648.4834449994
  volume_cumulative_usd: 8713949.409653056
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-15T00:00:00Z"
bullets:
  - "Polymarket prices 14% probability of permanent US-Iran peace deal by June 15."
  - "Polymarket: $2.5M 24h volume, 28% of $8.7M all-time; significant fresh attention."
  - "Iran nuclear talks and back-channel diplomatic signals driving renewed speculative interest ahead of June 15 deadline."
  - "Contract expires June 15; 11-day window compresses resolution risk sharply."
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
      poly_vol_24h_usd: 2480648.4834449994
sources:
  - label: "ClearMarket market record: US x Iran permanent peace deal by May 31, 2026?"
    url: "https://clearmarket.fyi/events/us-x-iran-permanent-peace-deal-by"
    retrieved_at: "2026-06-04T11:15:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 14% price with 28% of all-time volume in 24 hours signals macro desks are actively hedging or speculating on a near-term diplomatic breakthrough that would reprice energy and EM risk.
