---
signal_id: "CMSIG20261105VS02"
signal_slug: "will-republican-win-the-house-race-for-a-vol-256113"
headline: "AZ-2 House GOP: 80% on $256K Election Day volume"
semantic_title: "Buyers back Republicans in AZ-2 House race at 80%"
telemetry: "80% · $256K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T16:03:26+00:00"
event_id: "CM-EVT-23N8BBXJL5"
event_slug: "houseaz2-26"
event_question: "Will the winner of the Arizona 2nd Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEAZ2-26-R"
  question_raw: "Will Republican win the House race for AZ-2?"
  current_price: 0.8
  volume_24h_usd: 256113.84
  volume_cumulative_usd: 466121.52
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Market prices a Republican AZ-2 House win at 80%, solid but not settled."
  - "$256K in 24h represents 55% of all-time volume, majority of all trading occurring today."
  - "Election Day 2026 is today; live precinct returns will drive rapid price discovery."
  - "Kalshi contract resolves on certified House race winner for Arizona's 2nd district."
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
      kalshi_vol_24h_usd: 256113.84
sources:
  - label: "ClearMarket market record: Will the winner of the Arizona 2nd Congressional Distri"
    url: "https://clearmarket.fyi/events/houseaz2-26"
    retrieved_at: "2026-11-05T16:03:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of all-time AZ-2 volume arriving on Election Day signals this race drew last-minute attention as a contested swing pickup worth tracking for desk positioning on House majority counts.
