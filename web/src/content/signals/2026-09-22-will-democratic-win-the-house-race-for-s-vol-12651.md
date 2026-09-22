---
signal_id: "CMSIG20260922VS07"
signal_slug: "will-democratic-win-the-house-race-for-s-vol-12651"
headline: "Democrat SC-01 House: 25% on $13K Kalshi spike"
semantic_title: "SC-01 Democratic bet holds at 25% on record volume day"
telemetry: "25% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T13:04:04+00:00"
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
  - "At 25%, Kalshi prices a Democratic win in South Carolina's 1st district as a long shot."
  - "73% of all-time volume settled in 24 hours, by far the highest lifetime-share ratio in today's batch."
  - "A 73% single-day concentration suggests this contract opened or gained traction very recently, not gradual accumulation."
  - "Resolves on 2026 general election result."
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
    retrieved_at: "2026-09-22T13:04:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 73% lifetime-volume day indicates this contract is newly live or newly visible, a desk should flag SC-01 as a fresh House-control input rather than an established pricing signal.
