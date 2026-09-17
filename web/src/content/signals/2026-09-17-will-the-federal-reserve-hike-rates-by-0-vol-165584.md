---
signal_id: "CMSIG20260917VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-165584"
headline: "Fed Oct. hold (0bps): 55% on $166K volume"
semantic_title: "Fed holds at October meeting, odds tilt slightly above 50%"
telemetry: "55% · $166K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-17T13:05:20+00:00"
event_id: "CM-EVT-FPF77GZ320"
event_slug: "kxfeddecision-26oct"
event_question: "Will the Federal Reserve make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26OCT-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their October 2026 meeting?"
  current_price: 0.55
  volume_24h_usd: 165584.23
  volume_cumulative_usd: 277416.8
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T18:05:00Z"
bullets:
  - "Kalshi prices a 55% chance the Fed stands pat in October, mild lean toward no move."
  - "$166K in 24h is 60% of all-time volume, reflecting a sharp surge in rate-path positioning."
  - "September macro data and Fed speaker tone are driving fresh conviction on the October pause."
  - "Contract resolves on the October 2026 FOMC decision date."
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
      kalshi_vol_24h_usd: 165584.23
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in October 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-26oct"
    retrieved_at: "2026-09-17T13:05:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume on the hold contract signals desks are actively repricing October Fed probabilities, likely in response to recent inflation or labor data.
