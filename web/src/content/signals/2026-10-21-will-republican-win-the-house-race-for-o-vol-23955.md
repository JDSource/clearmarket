---
signal_id: "CMSIG20261021VS03"
signal_slug: "will-republican-win-the-house-race-for-o-vol-23955"
headline: "OH-10 House GOP win: 76% on $24K volume"
semantic_title: "Republicans favored to hold OH-10 House seat"
telemetry: "76% · $24K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T13:25:08+00:00"
event_id: "CM-EVT-TY2DWD9XJ0"
event_slug: "kxhouserace-oh10-26"
event_question: "OH-10 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-OH10-26-R"
  question_raw: "Will Republican win the House race for OH-10?"
  current_price: 0.76
  volume_24h_usd: 23955.5
  volume_cumulative_usd: 71690.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices the Republican candidate at 76% in Ohio's 10th, a solid but not insurmountable advantage."
  - "$24K in 24h volume represents 33% of all-time handle, a notable single-session concentration."
  - "Fresh volume into a 76% favorite suggests a recent poll, fundraising report, or candidate event is reinforcing the price."
  - "Resolves on certified 2026 midterm results for Ohio's 10th congressional district."
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
      kalshi_vol_24h_usd: 23955.5
sources:
  - label: "ClearMarket market record: OH-10 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-oh10-26"
    retrieved_at: "2026-10-21T13:25:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

One-third of lifetime volume in a single day on a 76% contract tells a desk the market is re-underwriting this seat after a data point, worth monitoring whether the Democratic challenger's position is deteriorating further.
