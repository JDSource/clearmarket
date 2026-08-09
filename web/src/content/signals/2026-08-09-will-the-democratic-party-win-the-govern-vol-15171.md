---
signal_id: "CMSIG20260809VS05"
signal_slug: "will-the-democratic-party-win-the-govern-vol-15171"
headline: "Illinois governor Dem: 94% on $15K spike"
semantic_title: "Democrats hold Illinois governorship at 94% odds"
telemetry: "94% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-09T08:37:25+00:00"
event_id: "CM-EVT-Z8JF0KZ5G3"
event_slug: "govpartyil-26"
event_question: "Illinois Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYIL-26-D"
  question_raw: "Will the Democratic party win the governorship in Illinois"
  current_price: 0.94
  volume_24h_usd: 15171.43
  volume_cumulative_usd: 33234.51
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices the Democratic party winning the Illinois governorship at 94%, a strong structural lean with limited priced-in risk."
  - "24h volume of $15K is 46% of all-time handle, suggesting a catalyst has re-engaged traders on a seemingly settled race."
  - "Fresh volume at a high-probability level may reflect a specific candidate entry, polling drop, or donor development prompting a re-check."
  - "Contract resolves on the Illinois gubernatorial general election result."
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
      kalshi_vol_24h_usd: 15171.43
sources:
  - label: "ClearMarket market record: Illinois Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyil-26"
    retrieved_at: "2026-08-09T08:37:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 94% contract drawing nearly half its lifetime volume in one session tells a desk that something has briefly reopened the Illinois governor question, monitor for a Republican field development or incumbent news.
