---
signal_id: "CMSIG20260930VS03"
signal_slug: "will-the-republican-party-win-the-govern-vol-59110"
headline: "GOP Vermont governor: 83% on $59K surge"
semantic_title: "Traders back the GOP heavily in Vermont governor race"
telemetry: "83% · $59K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T14:33:50+00:00"
event_id: "CM-EVT-ZSNM57MQS0"
event_slug: "govpartyvt-26"
event_question: "Vermont Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYVT-26-R"
  question_raw: "Will the Republican party win the governorship in Vermont"
  current_price: 0.83
  volume_24h_usd: 59110.75
  volume_cumulative_usd: 172191.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-05T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Vermont governorship win at 83%, reflecting strong incumbent-party confidence."
  - "24h volume of $59K is 34% of all-time, notable for an historically low-liquidity state race."
  - "Vermont's Republican incumbent has unusual cross-party strength; volume may reflect late confirmatory polling."
  - "Resolves on the 2026 Vermont gubernatorial election result."
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
      kalshi_vol_24h_usd: 59110.75
sources:
  - label: "ClearMarket market record: Vermont Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyvt-26"
    retrieved_at: "2026-09-30T14:33:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A sharp liquidity event in a high-confidence race signals desks that position-taking is consolidating around the Republican outcome, with little evidence of a competitive challenge emerging.
