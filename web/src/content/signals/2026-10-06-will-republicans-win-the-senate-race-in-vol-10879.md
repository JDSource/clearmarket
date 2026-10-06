---
signal_id: "CMSIG20261006VS05"
signal_slug: "will-republicans-win-the-senate-race-in-vol-10879"
headline: "GOP Tennessee Senate: 93% on $10K surge"
semantic_title: "Tennessee Senate GOP odds stay firm at 93% on fresh volume"
telemetry: "93% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-06T14:43:21+00:00"
event_id: "CM-EVT-T9PVHWGH35"
event_slug: "senatetn-26"
event_question: "Will the Tennessee Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATETN-26-R"
  question_raw: "Will Republicans win the Senate race in Tennessee?"
  current_price: 0.93
  volume_24h_usd: 10879.54
  volume_cumulative_usd: 42618.63
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Senate win in Tennessee at 93%, near-certain by market consensus."
  - "26% of all-time volume arrived in 24h, a notable refresh for a race widely seen as settled."
  - "Fresh trading on a locked-in race may reflect cross-market hedging or cycle-basket positioning."
  - "Resolves on 2026 midterm election results."
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
      kalshi_vol_24h_usd: 10879.54
sources:
  - label: "ClearMarket market record: Will the Tennessee Senate race be decided by January 4,"
    url: "https://clearmarket.fyi/events/senatetn-26"
    retrieved_at: "2026-10-06T14:43:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume flowing into a 93% favorite suggests this is likely portfolio-level or hedging activity rather than a reassessment of Tennessee's competitiveness, useful context for desks building Senate majority probability models.
