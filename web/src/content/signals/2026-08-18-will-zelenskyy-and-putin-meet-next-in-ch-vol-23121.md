---
signal_id: "CMSIG20260818VS05"
signal_slug: "will-zelenskyy-and-putin-meet-next-in-ch-vol-23121"
headline: "Zelenskyy-Putin China meet: 0% on $23K surge"
semantic_title: "A Zelenskyy-Putin China meeting before 2027 stays at 0%"
telemetry: "0% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-18T08:31:22+00:00"
event_id: "CM-EVT-RRTJG4DGV7"
event_slug: "where-will-zelenskyy-and-putin-meet-next"
event_question: "Will Zelenskyy and Putin meet before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1219cce4580ec8af8b9e927915de1f46daf8109d88696f3b6295f45384f714a4"
  question_raw: "Will Zelenskyy and Putin meet next in China before 2027?"
  current_price: 0.004
  volume_24h_usd: 23121.526
  volume_cumulative_usd: 85606.028762
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the meeting at 0%, traders see no credible path to a China-hosted summit before year-end."
  - "27% of all-time volume in 24h ($23K), a meaningful activity spike for a contract already at the floor."
  - "Volume at a 0% price typically reflects either settlement anticipation or a news item that killed residual hope."
  - "Resolves if Zelenskyy and Putin hold a face-to-face meeting on Chinese soil before January 1, 2027."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 23121.526
sources:
  - label: "ClearMarket market record: Will Zelenskyy and Putin meet before 2027?"
    url: "https://clearmarket.fyi/events/where-will-zelenskyy-and-putin-meet-next"
    retrieved_at: "2026-08-18T08:31:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume piling into a 0% contract signals the market is actively closing out any remaining long positions, a desk covering geopolitical tail risk on a China-brokered peace track should treat this scenario as expired.
