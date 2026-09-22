---
signal_id: "CMSIG20260922VS05"
signal_slug: "will-democratic-win-the-house-race-for-s-vol-12651"
headline: "Democrat SC-01 House: 25% on $13K volume surge"
semantic_title: "SC-01 Democratic odds hold at 25% on a near-record volume day"
telemetry: "25% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T07:48:31+00:00"
event_id: "CM-EVT-1VRNWSCZT7"
event_slug: "kxhouserace-sc01-26"
event_question: "SC-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-SC01-26-D"
  question_raw: "Will Democratic win the House race for SC-01?"
  current_price: 0.25
  volume_24h_usd: 12651.5
  volume_cumulative_usd: 17373.37
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in SC-01 at exactly 25%, the market sees this as a long shot in a historically Republican seat."
  - "$12.7K in 24h is 73% of all-time contract volume, nearly the entire trading history of this contract compressed into one session."
  - "This level of volume concentration on a low-price contract signals either a specific catalyst or a new wave of informed attention hitting a previously thin market."
  - "Resolves on 2026 midterm results for SC-01."
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
      kalshi_vol_24h_usd: 12651.5
sources:
  - label: "ClearMarket market record: SC-01 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-sc01-26"
    retrieved_at: "2026-09-22T07:48:31+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Seventy-three percent of all-time volume in a single session on a 25% contract means the SC-01 race is being priced for the first time with real liquidity, any catalyst here is likely fresh and worth sourcing.
