---
signal_id: "CMSIG20261103VS04"
signal_slug: "will-the-democratic-party-win-the-govern-vol-163585"
headline: "Kansas Dem governor: 36% on $164K surge"
semantic_title: "Democratic Kansas governor bid draws buyers at 36%"
telemetry: "36% · $164K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T07:49:22+00:00"
event_id: "CM-EVT-53XSJLYKW7"
event_slug: "govpartyks-27"
event_question: "Kansas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYKS-27-D"
  question_raw: "Will the Democratic party win the governorship in Kansas"
  current_price: 0.36
  volume_24h_usd: 163585.08
  volume_cumulative_usd: 234076.97
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic Kansas governorship win at 36%, an underdog but not a long shot."
  - "70% of all-time volume arrived in 24 hours, the highest all-time share of any spike in this batch."
  - "Kansas has trended competitive in statewide races; 36% on Election Day implies live contest status."
  - "Resolves on certified Kansas gubernatorial results."
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
      kalshi_vol_24h_usd: 163585.08
sources:
  - label: "ClearMarket market record: Kansas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyks-27"
    retrieved_at: "2026-11-03T07:49:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Seventy percent of all-time contract volume landing in a single session on a 36% Democratic outcome tells a desk this race is being treated as a genuine swing result to watch tonight.
