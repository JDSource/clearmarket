---
signal_id: "CMSIG20260605VS01"
signal_slug: "us-x-iran-permanent-peace-deal-by-june-1-vol-2480648"
headline: "US-Iran peace deal: 14% on $2.5M inflow"
semantic_title: "Fresh capital tests a US-Iran permanent peace deal by June 15"
telemetry: "14% · $2.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-05T11:24:46+00:00"
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
  - "Polymarket prices a permanent US-Iran peace deal by June 15 at just 14%, deep tail territory."
  - "24h volume of $2.5M represents 28% of all-time handle, indicating a sharp discrete attention spike."
  - "Diplomatic signals or back-channel leak may be pulling new money in; 14% implies the market is absorbing optimism but not endorsing it."
  - "Resolution deadline is June 15, ten days out, compressing time value and magnifying any fresh news."
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
    retrieved_at: "2026-06-05T11:24:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 28% all-time-volume day on a hard-dated geopolitical contract this close to expiry tells a macro desk that credible diplomatic noise has surfaced, even as consensus prices the outcome as unlikely.
