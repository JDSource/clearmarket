---
signal_id: "CMSIG20261023VS05"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-19982"
headline: "Dem MI-7 House: 74% on $20K in renewed trading"
semantic_title: "Democrats hold a clear edge in MI-7 as fresh bets arrive"
telemetry: "74% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T13:04:13+00:00"
event_id: "CM-EVT-8VFB3KQ7V2"
event_slug: "housemi7-26"
event_question: "MI-07 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEMI7-26-D"
  question_raw: "Will Democratic win the House race for MI-7?"
  current_price: 0.74
  volume_24h_usd: 19982.03
  volume_cumulative_usd: 60372.83
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices the Democratic candidate at 74% in MI-7, market leans Democratic but leaves meaningful risk priced."
  - "24h volume of $20K is 33% of all-time total, reflecting a solid one-day influx into an already active contract."
  - "MI-7 has been a competitive target; renewed volume at 74% suggests late confirmation of the Democratic lean."
  - "Resolves on Michigan 7th District House race result."
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
      kalshi_vol_24h_usd: 19982.03
sources:
  - label: "ClearMarket market record: MI-07 House winner?"
    url: "https://clearmarket.fyi/events/housemi7-26"
    retrieved_at: "2026-10-23T13:04:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A third of all-time volume arriving in one day on a 74% Democratic contract in MI-7 signals desks are settling on this seat as a likely but not certain Democratic hold entering the final stretch.
