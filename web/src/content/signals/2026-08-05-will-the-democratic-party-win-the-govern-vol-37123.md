---
signal_id: "CMSIG20260805VS06"
signal_slug: "will-the-democratic-party-win-the-govern-vol-37123"
headline: "Democrats win TX governor: 12% on $37K in 24h"
semantic_title: "Democrats winning Texas governor stays under 25%"
telemetry: "12% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-05T10:31:36+00:00"
event_id: "CM-EVT-B8XSR8GJT6"
event_slug: "govpartytx-26"
event_question: "Texas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYTX-26-D"
  question_raw: "Will the Democratic party win the governorship in Texas"
  current_price: 0.12
  volume_24h_usd: 37123.41
  volume_cumulative_usd: 54739.56
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-20T15:00:00Z"
bullets:
  - "Kalshi prices a Texas Democratic gubernatorial win at 12%, long shot, but not negligible."
  - "68% of all-time volume in 24h suggests a specific catalyst refreshed attention on this race."
  - "Could reflect a candidate filing, polling release, or national environment shift tied to today's news cycle."
  - "Resolves on the 2026 Texas gubernatorial general election result."
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
      kalshi_vol_24h_usd: 37123.41
sources:
  - label: "ClearMarket market record: Texas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartytx-26"
    retrieved_at: "2026-08-05T10:31:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

12% with a volume surge on a historically deep-red state contest is worth flagging, a desk tracking the 2026 cycle should investigate what catalyst prompted fresh positioning before dismissing it.
