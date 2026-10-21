---
signal_id: "CMSIG20261021VS01"
signal_slug: "will-democratic-win-the-house-race-for-a-vol-22482"
headline: "AZ-6 House Dem win: 86% on $22K volume burst"
semantic_title: "Democrats heavily favored in AZ-6 House race"
telemetry: "86% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T13:25:08+00:00"
event_id: "CM-EVT-2G9FBHFVL0"
event_slug: "houseaz6-26"
event_question: "AZ-06 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEAZ6-26-D"
  question_raw: "Will Democratic win the House race for AZ-6?"
  current_price: 0.86
  volume_24h_usd: 22482.73
  volume_cumulative_usd: 31175.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic candidate at 86%, the contract treats this seat as close to a lock for the party."
  - "72% of all-time volume, $22K, landed in the last 24 hours, the highest single-day concentration on this contract."
  - "Surge at 72% all-time share suggests a fresh catalyst: polling, candidate news, or money-race filing likely in play."
  - "Resolves on certified 2026 midterm results for Arizona's 6th congressional district."
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
      kalshi_vol_24h_usd: 22482.73
sources:
  - label: "ClearMarket market record: AZ-06 House winner?"
    url: "https://clearmarket.fyi/events/houseaz6-26"
    retrieved_at: "2026-10-21T13:25:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When 72% of a contract's entire lifetime volume hits in one day, a desk should treat it as a near-confirmation event, either new polling or an opponent development is collapsing the opposition's case.
