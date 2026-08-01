---
signal_id: "CMSIG20260801VS03"
signal_slug: "will-the-h200-compute-per-hour-price-be-vol-27348"
headline: "H200 above $5.49/hr by Dec 31: 99% on $27K spike"
semantic_title: "H200 compute price staying above $5.49 by Dec 31 locks near certainty"
telemetry: "99% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-01T09:55:41+00:00"
event_id: "CM-EVT-MYTG9CGV52"
event_slug: "kxh200max-26dec31"
event_question: "The H200 compute per hour price by Dec 31"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200MAX-26DEC31-5.490"
  question_raw: "Will the H200 compute per hour price be above $5.49 by Dec 31?"
  current_price: 0.99
  volume_24h_usd: 27348.12
  volume_cumulative_usd: 32842.99
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T04:59:59Z"
bullets:
  - "Kalshi prices a 99% chance the H200 hourly compute rate stays above $5.49 through December 31."
  - "24h volume of $27K is 83% of all-time flow, nearly the entire contract history printed today."
  - "Surge implies a repricing event in GPU cloud markets, possibly a new rate card or capacity announcement, that validated elevated pricing."
  - "Resolves December 31, 2026; at 99% this is functionally a settled view."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 27348.12
sources:
  - label: "ClearMarket market record: The H200 compute per hour price by Dec 31"
    url: "https://clearmarket.fyi/events/kxh200max-26dec31"
    retrieved_at: "2026-08-01T09:55:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 83% all-time volume print into a 99% price is a desk signal that the AI-compute pricing floor is being treated as locked in, any cloud capacity expansion thesis that depends on falling H200 rates is being actively faded by this market.
