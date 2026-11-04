---
signal_id: "CMSIG20261104VS07"
signal_slug: "will-the-democratic-party-win-the-govern-vol-1077393"
headline: "KS governor Dem: 92% on $1.1M Kalshi inflow"
semantic_title: "Buyers back Democrats in a rare Kansas governor race"
telemetry: "92% · $1.1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T07:48:42+00:00"
event_id: "CM-EVT-53XSJLYKW7"
event_slug: "govpartyks-27"
event_question: "Kansas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYKS-27-D"
  question_raw: "Will the Democratic party win the governorship in Kansas"
  current_price: 0.921
  volume_24h_usd: 1077393.54
  volume_cumulative_usd: 1691896.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Democratic Kansas governor win at 92%, a striking result in a traditionally red state."
  - "64% of all-time volume in 24h signals a sharp increase in market attention near resolution."
  - "Kansas governorship has history of Democratic wins; 92% odds confirm the pattern is holding in 2026."
  - "Resolves on certified Kansas 2026 gubernatorial outcome."
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
      kalshi_vol_24h_usd: 1077393.54
sources:
  - label: "ClearMarket market record: Kansas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyks-27"
    retrieved_at: "2026-11-04T07:48:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 92% price with 64% of lifetime volume concentrating in one day tells desks that Kansas governor is being treated as a Democratic hold, with capital flowing in to confirm rather than contest the result.
