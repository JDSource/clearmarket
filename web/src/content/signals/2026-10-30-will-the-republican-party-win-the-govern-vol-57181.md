---
signal_id: "CMSIG20261030VS07"
signal_slug: "will-the-republican-party-win-the-govern-vol-57181"
headline: "Tennessee GOP governor: 93% on $57K flow"
semantic_title: "Tennessee governor race draws pre-election volume at 93%"
telemetry: "93% · $57K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T07:48:50+00:00"
event_id: "CM-EVT-S594KBZJM4"
event_slug: "govpartytn-26"
event_question: "Will there be a new Tennessee Governor by 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYTN-26-R"
  question_raw: "Will the Republican party win the governorship in Tennessee"
  current_price: 0.931
  volume_24h_usd: 57181.1
  volume_cumulative_usd: 166084.57
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-19T15:00:00Z"
bullets:
  - "Kalshi prices Republicans winning the Tennessee governorship at 93%, a strong favourite stance."
  - "24h volume of $57K is 34% of all-time $166K, elevated but not a lifetime-dominant spike."
  - "Election-eve flow on a 93% contract suggests portfolio completion rather than new conviction."
  - "Contract resolves on the Tennessee gubernatorial election outcome."
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
      kalshi_vol_24h_usd: 57181.1
sources:
  - label: "ClearMarket market record: Will there be a new Tennessee Governor by 2027?"
    url: "https://clearmarket.fyi/events/govpartytn-26"
    retrieved_at: "2026-10-30T07:48:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Pre-election volume on a high-confidence Tennessee governor contract suggests desks are rounding out state-level political books before results roll in rather than expressing fresh directional views.
