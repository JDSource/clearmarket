---
signal_id: "CMSIG20260918VS02"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-28964"
headline: "U-3 above 3.9% Sept: 93% on $29K surge"
semantic_title: "U-3 above 3.9% in September stays a heavy favorite"
telemetry: "93% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-18T12:39:43+00:00"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "Will the unemployment rate (U-3) be above 4.0% in September?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T3.9"
  question_raw: "Will the unemployment rate (U-3) be above 3.9% in September?"
  current_price: 0.93
  volume_24h_usd: 28964.96
  volume_cumulative_usd: 36481.07
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "93% price reflects near-consensus that September's official unemployment print will exceed 3.9%."
  - "79% of all-time volume landed in 24 hours, the market is essentially pricing a final verdict before resolution."
  - "The surge likely reflects traders positioning around the September jobs report release."
  - "Resolves on the Bureau of Labor Statistics official U-3 release for September 2026."
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
      kalshi_vol_24h_usd: 28964.96
sources:
  - label: "ClearMarket market record: Will the unemployment rate (U-3) be above 4.0% in Septe"
    url: "https://clearmarket.fyi/events/kxu3-26sep"
    retrieved_at: "2026-09-18T12:39:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 93% price absorbing 79% of lifetime volume in one session signals the desk that the market has essentially closed on this outcome and residual short-side flow is thin.
