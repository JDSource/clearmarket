---
signal_id: "CMSIG20261103VS01"
signal_slug: "will-the-republican-party-win-the-govern-vol-3154697"
headline: "Florida GOP governor: 68% on $3.2M volume burst"
semantic_title: "Buyers back Florida GOP governor odds at 68%"
telemetry: "68% · $3.2M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T15:46:45+00:00"
event_id: "CM-EVT-4HX1NKV2L1"
event_slug: "govpartyfl-26"
event_question: "Florida Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYFL-26-R"
  question_raw: "Will the Republican party win the governorship in Florida"
  current_price: 0.68
  volume_24h_usd: 3154697.14
  volume_cumulative_usd: 7367398.2
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "At 68%, Kalshi traders price a clear Republican favorite in the 2026 Florida gubernatorial race."
  - "$3.2M in 24h trading equals 43% of all-time contract volume, an outsized single-day commitment."
  - "Florida governorship has trended Republican for two cycles; heavy volume here reinforces, not challenges, that baseline."
  - "Resolves on the 2026 Florida gubernatorial election result."
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
      kalshi_vol_24h_usd: 3154697.14
sources:
  - label: "ClearMarket market record: Florida Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyfl-26"
    retrieved_at: "2026-11-03T15:46:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume-to-all-time ratio of 43% signals a positioning surge, likely tied to candidate or polling developments; a desk should monitor for news that prompted fresh directional conviction at the 68% level.
