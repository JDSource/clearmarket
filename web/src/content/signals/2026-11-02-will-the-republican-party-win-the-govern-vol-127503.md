---
signal_id: "CMSIG20261102VS04"
signal_slug: "will-the-republican-party-win-the-govern-vol-127503"
headline: "Vermont Gov GOP: 67% on $128K surge"
semantic_title: "Republicans stay favored in the Vermont governor race"
telemetry: "67% · $128K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T07:49:23+00:00"
event_id: "CM-EVT-ZSNM57MQS0"
event_slug: "govpartyvt-26"
event_question: "Vermont Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYVT-26-R"
  question_raw: "Will the Republican party win the governorship in Vermont"
  current_price: 0.67
  volume_24h_usd: 127503.58
  volume_cumulative_usd: 395852.42
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-05T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 67%, a clear but not overwhelming favorite in an atypically competitive Vermont race."
  - "$128K in 24h equals 32% of all-time volume, marking a notable pre-election attention spike."
  - "Vermont's governor race drew Republican-leaning odds despite the state's deep-blue presidential lean, volume confirms the anomaly is priced in."
  - "Resolves on Vermont governor election result."
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
      kalshi_vol_24h_usd: 127503.58
sources:
  - label: "ClearMarket market record: Vermont Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyvt-26"
    retrieved_at: "2026-11-02T07:49:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Elevated volume on a 67% GOP-favored Vermont governor contract tells a desk that the state-level race is being treated as genuinely independent of the national partisan lean, worth monitoring for late movement.
