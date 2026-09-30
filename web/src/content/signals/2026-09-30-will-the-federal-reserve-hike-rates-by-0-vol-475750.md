---
signal_id: "CMSIG20260930VS00"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-475750"
headline: "Fed Oct hold: 64% on $476K surge"
semantic_title: "Fed hold in October stays the heavy bet"
telemetry: "64% · $476K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T14:33:50+00:00"
event_id: "CM-EVT-FPF77GZ320"
event_slug: "kxfeddecision-26oct"
event_question: "Will the Federal Reserve make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26OCT-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their October 2026 meeting?"
  current_price: 0.64
  volume_24h_usd: 475750.97
  volume_cumulative_usd: 1373491.99
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T18:05:00Z"
bullets:
  - "Kalshi prices a Fed pause at 64%, implying a hold is the clear base case but far from certain."
  - "24h volume of $476K is 35% of all-time, fresh capital flooding in days before the October meeting."
  - "October FOMC is imminent; traders are locking in rate-path positions ahead of the decision."
  - "Resolves on the October 2026 Fed rate announcement."
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
      kalshi_vol_24h_usd: 475750.97
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in October 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-26oct"
    retrieved_at: "2026-09-30T14:33:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy pre-FOMC positioning on Kalshi signals desks are actively hedging rate-path exposure into the October meeting with conviction around a hold but meaningful residual risk priced in.
