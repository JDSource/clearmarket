---
signal_id: "CMSIG20261030VS01"
signal_slug: "will-republicans-win-the-senate-race-in-vol-156964"
headline: "Mississippi Senate: 89% on $157K volume"
semantic_title: "Mississippi Senate stays a near-certain Republican hold"
telemetry: "89% · $157K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T07:48:50+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-R"
  question_raw: "Will Republicans win the Senate race in Mississippi?"
  current_price: 0.89
  volume_24h_usd: 156964.59
  volume_cumulative_usd: 519651.79
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans winning Mississippi Senate at 89%, a heavy favourite read."
  - "24h volume of $157K is 30% of all-time $520K, meaningful fresh liquidity on a settled market."
  - "Late-cycle volume on a high-conviction line suggests hedgers, not speculators, driving flow."
  - "Resolution tied to Mississippi Senate election outcome."
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
      kalshi_vol_24h_usd: 156964.59
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-10-30T07:48:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Renewed volume on an already-settled favourite indicates desks are using the Mississippi Senate contract as a low-variance hedge within a broader Senate portfolio.
