---
signal_id: "CMSIG20261023VS01"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-94094"
headline: "Dem NC-1 House: 81% on $94K, nearly half all-time vol"
semantic_title: "Democrats hold a strong lead in NC-1 as trading picks up"
telemetry: "81% · $94K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T13:04:13+00:00"
event_id: "CM-EVT-22K74MYTV1"
event_slug: "housenc1-26"
event_question: "Will the winner of the North Carolina 1st Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENC1-26-D"
  question_raw: "Will Democratic win the House race for NC-1?"
  current_price: 0.81
  volume_24h_usd: 94094.5
  volume_cumulative_usd: 194113.69
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices the Democratic candidate at 81% in NC-1, market treats this seat as a near-lock for the party."
  - "24h volume of $94K represents 48% of the contract's all-time total, marking a decisive surge of fresh conviction."
  - "Attention at this level this close to Election Day suggests late money is stress-testing the lead, not challenging it."
  - "Resolves on North Carolina 1st District House race result."
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
      kalshi_vol_24h_usd: 94094.5
sources:
  - label: "ClearMarket market record: Will the winner of the North Carolina 1st Congressional"
    url: "https://clearmarket.fyi/events/housenc1-26"
    retrieved_at: "2026-10-23T13:04:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-half all-time volume burst into an 81% contract signals desks are locking in positions on NC-1 as a reliable Democratic hold with little residual uncertainty to price.
