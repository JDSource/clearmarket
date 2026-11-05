---
signal_id: "CMSIG20261105VS03"
signal_slug: "will-republican-win-the-house-race-for-a-vol-260544"
headline: "AZ-2 GOP win: 77% on 65% of all-time vol today"
semantic_title: "Republicans hold a 75%+ edge in AZ-2 on record volume day"
telemetry: "77% · $261K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T07:49:08+00:00"
event_id: "CM-EVT-23N8BBXJL5"
event_slug: "houseaz2-26"
event_question: "Will the winner of the Arizona 2nd Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEAZ2-26-R"
  question_raw: "Will Republican win the House race for AZ-2?"
  current_price: 0.77
  volume_24h_usd: 260544.96
  volume_cumulative_usd: 400883.69
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican win in Arizona's 2nd district at 77%, a solid but not decisive lean."
  - "65% of all-time contract volume, $260K, hit today, making this the most active session in the contract's life."
  - "Election Day results in AZ-2 are live, and the market is staying above the 75% threshold under pressure."
  - "Resolves on certified AZ-2 House result; the remaining 23% reflects genuine competitive risk."
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
      kalshi_vol_24h_usd: 260544.96
sources:
  - label: "ClearMarket market record: Will the winner of the Arizona 2nd Congressional Distri"
    url: "https://clearmarket.fyi/events/houseaz2-26"
    retrieved_at: "2026-11-05T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two-thirds of all-time volume in one day at 77% tells the desk AZ-2 is a contested lean, not a lock, and live precincts could move this price materially before close.
