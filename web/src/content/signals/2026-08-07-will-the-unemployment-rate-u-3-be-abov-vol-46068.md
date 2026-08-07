---
signal_id: "CMSIG20260807VS07"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-46068"
headline: "July U-3 above 4.0%: 88% on $46K inflow"
semantic_title: "Traders back July U-3 above 4.0% at 88% ahead of BLS data"
telemetry: "88% · $46K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-07T08:54:29+00:00"
event_id: "CM-EVT-4MK3M5Z6K0"
event_slug: "kxu3-26jul"
event_question: "U.S. unemployment rate (U-3), July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUL-T4.0"
  question_raw: "Will the unemployment rate (U-3) be above 4.0% in July?"
  current_price: 0.88
  volume_24h_usd: 46068.56
  volume_cumulative_usd: 109946.67
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-06T14:00:00Z"
bullets:
  - "88% price means the market strongly expects July unemployment to clear the 4.0% threshold."
  - "$46K in 24h covers 42% of all-time volume, concentrated on today's likely BLS release."
  - "Paired with the 3.9% contract at 95%, the spread implies consensus for a 4.0%-range print."
  - "Resolves on the official BLS July U-3 unemployment rate."
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
      kalshi_vol_24h_usd: 46068.56
sources:
  - label: "ClearMarket market record: U.S. unemployment rate (U-3), July 2026"
    url: "https://clearmarket.fyi/events/kxu3-26jul"
    retrieved_at: "2026-08-07T08:54:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Reading Spikes 3 and 7 together, a macro desk sees the market pricing July U-3 as almost certain above 3.9% and very likely above 4.0%, compressing the consensus band and reducing surprise risk.
