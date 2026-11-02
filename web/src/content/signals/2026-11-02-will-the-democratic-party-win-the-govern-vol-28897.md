---
signal_id: "CMSIG20261102VS06"
signal_slug: "will-the-democratic-party-win-the-govern-vol-28897"
headline: "Kansas Gov Dem: 34% on $29K surge"
semantic_title: "Democrats face uphill odds in the Kansas governor race"
telemetry: "34% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T07:49:23+00:00"
event_id: "CM-EVT-53XSJLYKW7"
event_slug: "govpartyks-27"
event_question: "Kansas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYKS-27-D"
  question_raw: "Will the Democratic party win the governorship in Kansas"
  current_price: 0.34
  volume_24h_usd: 28897.05
  volume_cumulative_usd: 66585.44
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 34%, an underdog position but above the 25% threshold, indicating a live contest."
  - "$28.9K in 24h is 43% of all-time volume, the race is attracting fresh attention close to election day."
  - "Kansas has historically elected Democratic governors despite Republican presidential dominance; market reflects that structural nuance."
  - "Resolves on Kansas governor election result."
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
      kalshi_vol_24h_usd: 28897.05
sources:
  - label: "ClearMarket market record: Kansas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyks-27"
    retrieved_at: "2026-11-02T07:49:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume arriving at a 34% Democratic price signals that the Kansas governor race is drawing renewed attention as a potential upset candidate, worth a desk watching on election night.
