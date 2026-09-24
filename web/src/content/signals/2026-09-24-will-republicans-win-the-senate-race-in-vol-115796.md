---
signal_id: "CMSIG20260924VS01"
signal_slug: "will-republicans-win-the-senate-race-in-vol-115796"
headline: "Alaska Senate GOP: 29% on $116K Kalshi surge"
semantic_title: "Republicans slip to 29% in Alaska Senate race on fresh volume"
telemetry: "29% · $116K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T13:08:49+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-R"
  question_raw: "Will Republicans win the Senate race in Alaska?"
  current_price: 0.29
  volume_24h_usd: 115796.6
  volume_cumulative_usd: 328718.24
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "29% odds put Republicans as clear underdogs in the Alaska Senate contest."
  - "$116K in 24h represents 35% of all-time Kalshi volume on this contract."
  - "Heavy fresh activity suggests new polling or candidate news is driving rapid repricing."
  - "Resolves on Alaska Senate race election result."
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
      kalshi_vol_24h_usd: 115796.6
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-09-24T13:08:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A third of all-time volume arriving in one day points to a catalyst, likely new polling or an endorsement shift, that desks should track before the Alaska race hardens into consensus.
