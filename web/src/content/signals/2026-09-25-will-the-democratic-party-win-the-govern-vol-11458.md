---
signal_id: "CMSIG20260925VS05"
signal_slug: "will-the-democratic-party-win-the-govern-vol-11458"
headline: "Vermont Dem gov: 18% on $11K Kalshi volume"
semantic_title: "Democratic Vermont governor bid trades near 25% floor"
telemetry: "18% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T13:13:41+00:00"
event_id: "CM-EVT-ZSNM57MQS0"
event_slug: "govpartyvt-26"
event_question: "Vermont Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYVT-26-D"
  question_raw: "Will the Democratic party win the governorship in Vermont"
  current_price: 0.18
  volume_24h_usd: 11458.89
  volume_cumulative_usd: 19037.54
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-05T15:00:00Z"
bullets:
  - "Kalshi prices Democratic win at 18%, consistent with the mirror contract (GOP at 82%) and reflecting a heavy underdog position."
  - "24h volume is 60% of all-time handle, the second-highest all-time share in today's batch, suggesting coordinated activity on both sides of this contract."
  - "The Vermont Democratic and Republican governor contracts together show a synchronized volume surge, pointing to a single news catalyst driving both."
  - "Resolves on the 2026 Vermont gubernatorial election."
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
      kalshi_vol_24h_usd: 11458.89
sources:
  - label: "ClearMarket market record: Vermont Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyvt-26"
    retrieved_at: "2026-09-25T13:13:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Paired with the Republican Vermont governor spike, this mirror contract's 60% all-time session share confirms both sides of the race are attracting simultaneous capital, likely on a shared news event.
