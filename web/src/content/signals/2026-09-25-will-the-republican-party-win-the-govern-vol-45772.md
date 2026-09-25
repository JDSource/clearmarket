---
signal_id: "CMSIG20260925VS02"
signal_slug: "will-the-republican-party-win-the-govern-vol-45772"
headline: "Vermont GOP governor: 84% on $45K surge"
semantic_title: "Heavy trading backs Republican Vermont governor at 84%"
telemetry: "84% · $46K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T07:48:30+00:00"
event_id: "CM-EVT-ZSNM57MQS0"
event_slug: "govpartyvt-26"
event_question: "Vermont Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYVT-26-R"
  question_raw: "Will the Republican party win the governorship in Vermont"
  current_price: 0.84
  volume_24h_usd: 45772.31
  volume_cumulative_usd: 93853.29
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-05T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 84% to hold the Vermont governorship, an unusually strong GOP read in a blue state."
  - "$45K in 24h equals 49% of all-time volume, nearly doubling the contract's prior activity in one session."
  - "Vermont's Republican governor has historically outrun the party brand; fresh volume suggests bettors are pricing that dynamic as durable."
  - "Resolves on the Vermont gubernatorial election in November 2026."
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
      kalshi_vol_24h_usd: 45772.31
sources:
  - label: "ClearMarket market record: Vermont Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyvt-26"
    retrieved_at: "2026-09-25T07:48:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-half of lifetime volume in one day on an 84% Republican price in Vermont signals the market is treating this as a near-settled outcome, relevant for anyone modeling split-ticket gubernatorial patterns.
