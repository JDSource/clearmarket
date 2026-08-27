---
signal_id: "CMSIG20260827VS03"
signal_slug: "will-the-democratic-party-win-the-govern-vol-29048"
headline: "PA Dem governor: 95% on $29K inflow"
semantic_title: "Pennsylvania governor odds hold for Democrats on fresh volume"
telemetry: "95% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-27T18:47:16+00:00"
event_id: "CM-EVT-05XLLSTC09"
event_slug: "govpartypa-26"
event_question: "Pennsylvania Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYPA-26-D"
  question_raw: "Will the Democratic party win the governorship in Pennsylvania"
  current_price: 0.952
  volume_24h_usd: 29048.6
  volume_cumulative_usd: 94303.19
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-17T15:00:00Z"
bullets:
  - "Kalshi prices 95%, market strongly favors Democrats retaining the Pennsylvania governorship in 2026."
  - "24h volume of $29K represents 31% of all-time, a notable single-day acceleration."
  - "Fresh activity likely tied to candidate field developments or early polling out of Pennsylvania."
  - "Race resolves on 2026 Pennsylvania gubernatorial election result."
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
      kalshi_vol_24h_usd: 29048.6
sources:
  - label: "ClearMarket market record: Pennsylvania Governor winner?"
    url: "https://clearmarket.fyi/events/govpartypa-26"
    retrieved_at: "2026-08-27T18:47:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 31% all-time share in one session on an already deep market suggests renewed macro-political attention to Pennsylvania ahead of the 2026 cycle, worth cross-referencing against Senate and House contract flows.
