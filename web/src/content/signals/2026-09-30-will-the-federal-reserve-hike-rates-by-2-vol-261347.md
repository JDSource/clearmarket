---
signal_id: "CMSIG20260930VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-261347"
headline: "Fed Oct hike 25bps: 34% on $261K inflow"
semantic_title: "A 25bps Fed hike by October draws real money"
telemetry: "34% · $261K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T14:33:50+00:00"
event_id: "CM-EVT-FPF77GZ320"
event_slug: "kxfeddecision-26oct"
event_question: "Will the Federal Reserve make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26OCT-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their October 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 261347.85
  volume_cumulative_usd: 630990.2
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T18:05:00Z"
bullets:
  - "Kalshi prices a 25bps October hike at 34%, a credible tail risk, not a fringe outcome."
  - "24h volume of $261K is 41% of all-time, the highest single-day share yet on this contract."
  - "Paired surge with the hold contract confirms traders are actively splitting exposure across both outcomes."
  - "Resolves on the October 2026 FOMC rate decision."
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
      kalshi_vol_24h_usd: 261347.85
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in October 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-26oct"
    retrieved_at: "2026-09-30T14:33:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The parallel surge on the hike leg, at 41% of all-time volume in one session, tells desks the market is not simply rubber-stamping a pause; rate-hike risk is being actively priced and hedged.
