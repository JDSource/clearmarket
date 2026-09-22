---
signal_id: "CMSIG20260922VS06"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-18545"
headline: "Democrat MT-1 House: 29% on $19K Kalshi surge"
semantic_title: "Democrats win MT-1 stays a long shot at 29%"
telemetry: "29% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T13:04:04+00:00"
event_id: "CM-EVT-QWGZDJ1DQ6"
event_slug: "housemt1-26"
event_question: "MT-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEMT1-26-D"
  question_raw: "Will Democratic win the House race for MT-1?"
  current_price: 0.29
  volume_24h_usd: 18545.22
  volume_cumulative_usd: 31052.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 29%, Kalshi prices a Democratic upset in MT-1 as a meaningful but unlikely outcome."
  - "60% of all-time volume arrived in 24 hours, the highest all-time share concentration across today's batch."
  - "Paired with Spike 3's 70% GOP read, capital is actively pricing both sides of MT-1 in the same session."
  - "Resolves on 2026 general election result."
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
      kalshi_vol_24h_usd: 18545.22
sources:
  - label: "ClearMarket market record: MT-01 House winner?"
    url: "https://clearmarket.fyi/events/housemt1-26"
    retrieved_at: "2026-09-22T13:04:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 60% of lifetime volume printing in one day, MT-1 is live on both sides simultaneously, a desk building House-control scenarios should treat this as one of the most actively contested district contracts today.
