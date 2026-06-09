---
signal_id: "CMSIG20260609VS01"
signal_slug: "us-x-iran-permanent-peace-deal-by-june-1-vol-2480648"
headline: "US-Iran peace deal: 14% on $2.5M inflow"
semantic_title: "Fresh capital hedges against a US-Iran permanent peace deal"
telemetry: "14% · $2.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-09T10:58:29+00:00"
event_id: "CM-EVT-TQTJ2MLTV8"
event_slug: "us-x-iran-permanent-peace-deal-by"
event_question: "US x Iran permanent peace deal in 2026? (multi-deadline series)"
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
  - "Polymarket prices 14% odds of a permanent US-Iran peace deal by June 15, a meaningful tail."
  - "$2.5M in 24h represents 28% of all-time volume, signaling sharp escalation in trader attention."
  - "June 15 deadline is days away; volume surge implies fresh intelligence or diplomatic signal driving positioning."
  - "Resolution window is extremely tight, making this a high-velocity binary event for geopolitical desks."
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
  - label: "ClearMarket market record: US x Iran permanent peace deal in 2026? (multi-deadline"
    url: "https://clearmarket.fyi/events/us-x-iran-permanent-peace-deal-by"
    retrieved_at: "2026-06-09T10:58:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 14% price with 28% of all-time volume in a single session suggests desks are absorbing new diplomatic signal, attention this concentrated this close to expiry warrants geopolitical event-risk monitoring.
