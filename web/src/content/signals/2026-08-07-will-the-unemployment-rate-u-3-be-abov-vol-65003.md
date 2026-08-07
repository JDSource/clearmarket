---
signal_id: "CMSIG20260807VS03"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-65003"
headline: "July U-3 above 3.9%: 95% on $65K surge"
semantic_title: "July U-3 above 3.9% holds at 95% as volume tops half of all-time"
telemetry: "95% · $65K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-07T08:54:29+00:00"
event_id: "CM-EVT-4MK3M5Z6K0"
event_slug: "kxu3-26jul"
event_question: "U.S. unemployment rate (U-3), July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUL-T3.9"
  question_raw: "Will the unemployment rate (U-3) be above 3.9% in July?"
  current_price: 0.95
  volume_24h_usd: 65003.89
  volume_cumulative_usd: 124891.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-06T14:00:00Z"
bullets:
  - "At 95%, Kalshi market treats a sub-3.9% July print as nearly impossible."
  - "$65K in 24h equals 52% of all-time volume, majority of lifetime activity in one session."
  - "August 7 timing aligns with imminent BLS July employment report release."
  - "Resolves on the official July U-3 unemployment rate."
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
      kalshi_vol_24h_usd: 65003.89
sources:
  - label: "ClearMarket market record: U.S. unemployment rate (U-3), July 2026"
    url: "https://clearmarket.fyi/events/kxu3-26jul"
    retrieved_at: "2026-08-07T08:54:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of all-time volume arriving at a 95% price the day of the BLS release signals a macro desk that the high-threshold unemployment read is effectively consensus, with residual flow likely hedging tail risk.
