---
signal_id: "CMSIG20261002VS00"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-27374"
headline: "U-3 above 3.8% in Sept: 99% on $27K surge"
semantic_title: "Traders lock in U-3 above 3.8% for September"
telemetry: "99% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T07:48:52+00:00"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "Will the unemployment rate (U-3) be above 4.0% in September?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T3.8"
  question_raw: "Will the unemployment rate (U-3) be above 3.8% in September?"
  current_price: 0.99
  volume_24h_usd: 27374.82
  volume_cumulative_usd: 50608.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "99% price treats U-3 clearing 3.8% as a near-certainty ahead of Friday's release."
  - "24h volume of $27K is 54% of all-time handle, majority of lifetime action in one session."
  - "Fresh positioning concentrated at the eve of the September jobs report; attention precedes confirmation."
  - "Resolves on BLS U-3 print for September 2026."
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
      kalshi_vol_24h_usd: 27374.82
sources:
  - label: "ClearMarket market record: Will the unemployment rate (U-3) be above 4.0% in Septe"
    url: "https://clearmarket.fyi/events/kxu3-26sep"
    retrieved_at: "2026-10-02T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as the market treating sub-3.8% unemployment as essentially off the table, with pre-report hedging driving the volume spike.
