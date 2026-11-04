---
signal_id: "CMSIG20261104VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-9201125"
headline: "MS Senate Dem: 92% on $9.2M surge"
semantic_title: "Heavy trading backs Democrats to take Mississippi Senate"
telemetry: "92% · $9.2M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T15:57:35+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-D"
  question_raw: "Will Democratics win the Senate race in Mississippi?"
  current_price: 0.925
  volume_24h_usd: 9201125.68
  volume_cumulative_usd: 10419737.44
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic win at 92%, market treats this as near-certain."
  - "24h volume of $9.2M is 88% of all-time handle, an extraordinary single-day concentration."
  - "Election-eve flow with votes tallying today; capital is rushing to lock in final positions."
  - "Resolves on certified Mississippi Senate result."
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
      kalshi_vol_24h_usd: 9201125.68
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-11-04T15:57:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 88% all-time volume share on Election Day signals desks are aggressively settling exposure, treating a Democratic Mississippi Senate win as a done deal.
