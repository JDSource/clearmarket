---
signal_id: "CMSIG20261105VS07"
signal_slug: "will-democratic-win-the-house-race-for-a-vol-81607"
headline: "AZ-2 Dem win: 23% as 61% of all-time vol clears"
semantic_title: "Democratic AZ-2 odds stay at 25% despite heavy Election Day trade"
telemetry: "23% · $82K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T07:49:08+00:00"
event_id: "CM-EVT-23N8BBXJL5"
event_slug: "houseaz2-26"
event_question: "Will the winner of the Arizona 2nd Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEAZ2-26-D"
  question_raw: "Will Democratic win the House race for AZ-2?"
  current_price: 0.23
  volume_24h_usd: 81607.2
  volume_cumulative_usd: 133123.04
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in Arizona's 2nd district at 23%, a decided underdog stance against the 77% Republican pricing."
  - "61% of all-time volume, $81K, cleared in one day, the most active session this contract has seen."
  - "With Election Day results live, the market is holding the Democratic side just under 25% despite maximum-attention volume."
  - "Resolves on certified AZ-2 outcome; sustained pricing near 23% under heavy volume suggests real competitive data is not moving the needle toward Democrats."
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
      kalshi_vol_24h_usd: 81607.2
sources:
  - label: "ClearMarket market record: Will the winner of the Arizona 2nd Congressional Distri"
    url: "https://clearmarket.fyi/events/houseaz2-26"
    retrieved_at: "2026-11-05T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The highest-volume day in this contract's life at 23% tells the desk that live AZ-2 results are not yet offering Democrats a path, track precinct returns for any shift above 25% that would signal a tightening race.
