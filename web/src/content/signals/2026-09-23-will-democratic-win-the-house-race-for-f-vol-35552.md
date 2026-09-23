---
signal_id: "CMSIG20260923VS02"
signal_slug: "will-democratic-win-the-house-race-for-f-vol-35552"
headline: "FL-14 House Dem: 67% on $36K inflow"
semantic_title: "Heavy trading tests the Democrat's edge in FL-14"
telemetry: "67% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T13:18:01+00:00"
event_id: "CM-EVT-H89NH9QH14"
event_slug: "kxhouserace-fl14-26"
event_question: "Will a winner be determined in the FL-14 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL14-26-D"
  question_raw: "Will Democratic win the House race for FL-14?"
  current_price: 0.67
  volume_24h_usd: 35552.4
  volume_cumulative_usd: 120947.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Democrats at 67% in FL-14, a moderate favorite, but far from settled, leaving genuine two-way risk."
  - "24h volume of $36K represents 29% of all-time handle, pointing to a significant single-session re-rating."
  - "FL-14 is a competitive Florida district; activity at 67% implies the market is absorbing new information without reaching consensus."
  - "Resolves on the November 2026 FL-14 House general election."
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
      kalshi_vol_24h_usd: 35552.4
sources:
  - label: "ClearMarket market record: Will a winner be determined in the FL-14 House race by "
    url: "https://clearmarket.fyi/events/kxhouserace-fl14-26"
    retrieved_at: "2026-09-23T13:18:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-30% all-time volume day on a contract sitting at 67% indicates genuine two-sided uncertainty, desks should treat this as an active price-discovery session, not a directional stampede.
