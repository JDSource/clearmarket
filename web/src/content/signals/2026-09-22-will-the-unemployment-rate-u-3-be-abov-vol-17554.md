---
signal_id: "CMSIG20260922VS07"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-17554"
headline: "U-3 above 3.9% in Sept: 91% on $18K volume surge"
semantic_title: "September U-3 above 3.9% stays the strong consensus bet at 91%"
telemetry: "91% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T07:48:31+00:00"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "Will the unemployment rate (U-3) be above 4.0% in September?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T3.9"
  question_raw: "Will the unemployment rate (U-3) be above 3.9% in September?"
  current_price: 0.91
  volume_24h_usd: 17554.09
  volume_cumulative_usd: 55881.9
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi prices September U-3 unemployment above 3.9% at 91%, the market treats elevated unemployment as a near-done deal."
  - "$17.6K in 24h equals 31% of all-time contract volume, suggesting active pre-release positioning ahead of the September jobs report."
  - "At 91%, fresh volume likely reflects traders locking in consensus ahead of BLS data rather than expressing a contrarian view."
  - "Resolves on official BLS September 2026 U-3 unemployment release."
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
      kalshi_vol_24h_usd: 17554.09
sources:
  - label: "ClearMarket market record: Will the unemployment rate (U-3) be above 4.0% in Septe"
    url: "https://clearmarket.fyi/events/kxu3-26sep"
    retrieved_at: "2026-09-22T07:48:31+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-conviction pricing with 31% all-time volume in one session signals the September jobs print is imminent and desks are squaring macro exposure, monitor BLS release timing closely.
