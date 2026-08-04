---
signal_id: "CMSIG20260804VS03"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-23445"
headline: "U-3 above 4% in July: 90% on $23K surge"
semantic_title: "July U-3 above 4% stays the heavy favorite on fresh volume"
telemetry: "90% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-04T10:33:57+00:00"
event_id: "CM-EVT-4MK3M5Z6K0"
event_slug: "kxu3-26jul"
event_question: "The unemployment rate (U-3) in July"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUL-T4.0"
  question_raw: "Will the unemployment rate (U-3) be above 4.0% in July?"
  current_price: 0.9
  volume_24h_usd: 23445.8
  volume_cumulative_usd: 39049.87
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-06T14:00:00Z"
bullets:
  - "At 90%, Kalshi prices a July unemployment rate above 4% as nearly certain ahead of the BLS release."
  - "24h volume is 60% of all-time, the largest single-session share in this contract's history."
  - "The surge likely reflects positioning ahead of the July jobs report, the contract's imminent resolution catalyst."
  - "Resolves on the BLS-reported U-3 rate for July 2026."
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
      kalshi_vol_24h_usd: 23445.8
sources:
  - label: "ClearMarket market record: The unemployment rate (U-3) in July"
    url: "https://clearmarket.fyi/events/kxu3-26jul"
    retrieved_at: "2026-08-04T10:33:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sixty percent of lifetime volume arriving in one day at 90% odds is a classic pre-release positioning flush, desks should note that a sub-4% print would be an extreme consensus miss.
