---
signal_id: "CMSIG20260806VS00"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-51957"
headline: "U-3 July >3.9%: 96% on $52K surge"
semantic_title: "Fresh volume backs U-3 unemployment above 3.9% in July"
telemetry: "96% · $52K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-06T10:36:04+00:00"
event_id: "CM-EVT-4MK3M5Z6K0"
event_slug: "kxu3-26jul"
event_question: "U.S. unemployment rate (U-3), July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUL-T3.9"
  question_raw: "Will the unemployment rate (U-3) be above 3.9% in July?"
  current_price: 0.96
  volume_24h_usd: 51957.26
  volume_cumulative_usd: 60980.29
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-06T14:00:00Z"
bullets:
  - "96% pricing means the market treats above-3.9% unemployment as near-certain for July."
  - "24h volume of $52K is 85% of all-time, near-record activity flooding a single jobs contract."
  - "Surge likely driven by fresh BLS data or pre-release positioning ahead of the July jobs report."
  - "Resolves on official BLS U-3 release; 96% leaves almost no room for a surprise miss."
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
      kalshi_vol_24h_usd: 51957.26
sources:
  - label: "ClearMarket market record: U.S. unemployment rate (U-3), July 2026"
    url: "https://clearmarket.fyi/events/kxu3-26jul"
    retrieved_at: "2026-08-06T10:36:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume-to-all-time ratio signals a near-exhaustive repricing event, a desk should treat this as the market locking in a jobs-report consensus and watch for any residual 4% tail risk.
