---
signal_id: "CMSIG20260930VS02"
signal_slug: "will-the-republican-party-win-the-govern-vol-59318"
headline: "Vermont GOP gov: 83% on $59K, 34% of all-time"
semantic_title: "Vermont governorship at 83% GOP as buying picks up sharply"
telemetry: "83% · $59K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T07:48:11+00:00"
event_id: "CM-EVT-ZSNM57MQS0"
event_slug: "govpartyvt-26"
event_question: "Vermont Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYVT-26-R"
  question_raw: "Will the Republican party win the governorship in Vermont"
  current_price: 0.83
  volume_24h_usd: 59318.25
  volume_cumulative_usd: 172191.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-05T15:00:00Z"
bullets:
  - "Kalshi prices the Republican candidate at 83% to win Vermont's governorship, a strong but not certain favorite."
  - "$59K traded in 24h, equal to 34% of all-time volume on this contract, a concentrated burst of activity."
  - "Vermont's GOP governor historically overperforms the national party; fresh volume may reflect a new poll or endorsement."
  - "Contract resolves on the November 2026 Vermont gubernatorial election."
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
      kalshi_vol_24h_usd: 59318.25
sources:
  - label: "ClearMarket market record: Vermont Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyvt-26"
    retrieved_at: "2026-09-30T07:48:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Vermont's unusual status as a Republican-held governorship in a deep-blue state makes an 83% print with a volume surge worth tracking, any catalyst narrowing the odds would be a notable political signal.
