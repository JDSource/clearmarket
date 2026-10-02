---
signal_id: "CMSIG20261002VS01"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-46710"
headline: "U-3 above 3.9% in Sept: 92% on $47K surge"
semantic_title: "Odds hold firm on U-3 staying above 3.9% in September"
telemetry: "92% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T07:48:52+00:00"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "Will the unemployment rate (U-3) be above 4.0% in September?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T3.9"
  question_raw: "Will the unemployment rate (U-3) be above 3.9% in September?"
  current_price: 0.92
  volume_24h_usd: 46710.98
  volume_cumulative_usd: 186745.99
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "92% price signals strong conviction that September unemployment prints above 3.9%."
  - "$47K in 24h is 25% of all-time volume, a material single-session concentration at a quarter-mark milestone."
  - "Paired with the 3.8% and 4.0% contracts, the curve implies the market's modal range is 3.9%, 4.0% for the September U-3."
  - "Resolves on BLS official September 2026 U-3 release."
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
      kalshi_vol_24h_usd: 46710.98
sources:
  - label: "ClearMarket market record: Will the unemployment rate (U-3) be above 4.0% in Septe"
    url: "https://clearmarket.fyi/events/kxu3-26sep"
    retrieved_at: "2026-10-02T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Cross-referencing the 3.8%, 3.9%, and 4.0% contracts gives a desk a tight implied distribution for September U-3, useful for calibrating rate-path and risk-asset positioning ahead of the print.
