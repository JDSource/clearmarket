---
signal_id: "CMSIG20261007VS01"
signal_slug: "will-republicans-win-the-senate-race-in-vol-42049"
headline: "TN Senate GOP win: 94% on $42K one-day spike"
semantic_title: "Tennessee Senate odds hold at 94% through a volume surge"
telemetry: "94% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T15:02:49+00:00"
event_id: "CM-EVT-T9PVHWGH35"
event_slug: "senatetn-26"
event_question: "Will the Tennessee Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATETN-26-R"
  question_raw: "Will Republicans win the Senate race in Tennessee?"
  current_price: 0.939
  volume_24h_usd: 42049.42
  volume_cumulative_usd: 85080.48
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican victory in Tennessee at 94%, reflecting a near-settled race with minimal upset risk."
  - "49% of all-time volume, $42K, hit in 24 hours, the single largest day of activity on this contract."
  - "Late-cycle volume at high conviction levels often reflects hedgers and latecomers locking in exposure ahead of Election Day."
  - "Resolves on the certified outcome of the Tennessee Senate general election."
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
      kalshi_vol_24h_usd: 42049.42
sources:
  - label: "ClearMarket market record: Will the Tennessee Senate race be decided by January 4,"
    url: "https://clearmarket.fyi/events/senatetn-26"
    retrieved_at: "2026-10-07T15:02:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume into a 94% contract suggests the market is being used for late hedging or Senate-majority portfolio construction rather than price discovery.
