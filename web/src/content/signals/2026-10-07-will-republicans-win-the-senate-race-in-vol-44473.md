---
signal_id: "CMSIG20261007VS01"
signal_slug: "will-republicans-win-the-senate-race-in-vol-44473"
headline: "TN Senate GOP: 91% on $44K volume spike"
semantic_title: "Tennessee Senate seat stays firmly in Republican hands"
telemetry: "91% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T07:48:37+00:00"
event_id: "CM-EVT-T9PVHWGH35"
event_slug: "senatetn-26"
event_question: "Will the Tennessee Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATETN-26-R"
  question_raw: "Will Republicans win the Senate race in Tennessee?"
  current_price: 0.911
  volume_24h_usd: 44473.95
  volume_cumulative_usd: 81171.28
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 91%, Kalshi traders treat a Republican Tennessee Senate win as near-certain."
  - "24h volume of $44K is 55% of the contract's entire all-time volume, majority of all trading in one session."
  - "Surge likely driven by late-cycle positioning as election approaches and arbitrageurs compress residual risk."
  - "Resolves on Tennessee Senate race outcome."
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
      kalshi_vol_24h_usd: 44473.95
sources:
  - label: "ClearMarket market record: Will the Tennessee Senate race be decided by January 4,"
    url: "https://clearmarket.fyi/events/senatetn-26"
    retrieved_at: "2026-10-07T07:48:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half the contract's lifetime volume arriving in a single day at 91% suggests a desk could find limited edge but should note any sharp repricing as an early warning on Tennessee race news.
