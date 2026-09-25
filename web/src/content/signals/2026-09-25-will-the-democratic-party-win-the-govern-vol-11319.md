---
signal_id: "CMSIG20260925VS04"
signal_slug: "will-the-democratic-party-win-the-govern-vol-11319"
headline: "Vermont Dem governor: 18% on $11K surge"
semantic_title: "Democratic Vermont governor odds slip to 18% on fresh volume"
telemetry: "18% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T07:48:30+00:00"
event_id: "CM-EVT-ZSNM57MQS0"
event_slug: "govpartyvt-26"
event_question: "Vermont Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYVT-26-D"
  question_raw: "Will the Democratic party win the governorship in Vermont"
  current_price: 0.18
  volume_24h_usd: 11319.01
  volume_cumulative_usd: 18897.48
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-05T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 18% to win the Vermont governorship, the mirror contract to the 84% Republican read."
  - "$11K in 24h is 60% of all-time volume for this contract, the most active session on record."
  - "The simultaneous surge on both the Republican and Democratic Vermont governor contracts points to new participants entering both sides."
  - "Resolves on the Vermont gubernatorial election in November 2026."
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
      kalshi_vol_24h_usd: 11319.01
sources:
  - label: "ClearMarket market record: Vermont Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyvt-26"
    retrieved_at: "2026-09-25T07:48:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Record-share volume on both sides of the Vermont governor market in the same session suggests fresh positioning rather than informed directional flow, desks should read this as market-making activity around a clarifying event.
