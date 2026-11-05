---
signal_id: "CMSIG20261105VS07"
signal_slug: "will-democratic-win-the-house-race-for-a-vol-51635"
headline: "AZ-2 House Dem: 19% on $52K Election Day flow"
semantic_title: "Democrats long shot in AZ-2 House race at 19%"
telemetry: "19% · $52K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T16:03:26+00:00"
event_id: "CM-EVT-23N8BBXJL5"
event_slug: "houseaz2-26"
event_question: "Will the winner of the Arizona 2nd Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEAZ2-26-D"
  question_raw: "Will Democratic win the House race for AZ-2?"
  current_price: 0.19
  volume_24h_usd: 51635.56
  volume_cumulative_usd: 113579.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Market prices a Democratic AZ-2 House win at just 19%, clear underdog position."
  - "$52K in 24h is 45% of all-time; heavy proportional activity on the trailing side."
  - "Paired directly with Spike 2, the opposing Republican contract priced at 80%."
  - "Any narrowing of live returns today would reprice this contract rapidly given thin all-time liquidity."
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
      kalshi_vol_24h_usd: 51635.56
sources:
  - label: "ClearMarket market record: Will the winner of the Arizona 2nd Congressional Distri"
    url: "https://clearmarket.fyi/events/houseaz2-26"
    retrieved_at: "2026-11-05T16:03:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time Democratic AZ-2 volume arriving on Election Day suggests hedging activity against the Republican-favored position, a desk should watch for rapid repricing if early returns tighten the race.
