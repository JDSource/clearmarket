---
signal_id: "CMSIG20261104VS04"
signal_slug: "will-the-democratic-party-win-the-govern-vol-1273551"
headline: "KS governor Dem: 98% on $1.3M surge"
semantic_title: "Betting piles into Kansas governor going Democratic"
telemetry: "98% · $1.3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T15:57:35+00:00"
event_id: "CM-EVT-53XSJLYKW7"
event_slug: "govpartyks-27"
event_question: "Kansas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYKS-27-D"
  question_raw: "Will the Democratic party win the governorship in Kansas"
  current_price: 0.982
  volume_24h_usd: 1273551.29
  volume_cumulative_usd: 1946089.61
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic Kansas governorship win at 98%, essentially settled."
  - "$1.3M represents 65% of all-time handle arriving on Election Day."
  - "Kansas governorship flipping Democratic would be a major upset; a 98% price implies results are already in view."
  - "Resolves on certified Kansas gubernatorial result."
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
      kalshi_vol_24h_usd: 1273551.29
sources:
  - label: "ClearMarket market record: Kansas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyks-27"
    retrieved_at: "2026-11-04T15:57:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 65% all-time volume share printing at 98% on Election Day signals traders believe Kansas returns have made this outcome clear and are rushing to capture residual premium.
