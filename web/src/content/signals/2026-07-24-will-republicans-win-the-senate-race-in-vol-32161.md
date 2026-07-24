---
signal_id: "CMSIG20260724VS05"
signal_slug: "will-republicans-win-the-senate-race-in-vol-32161"
headline: "GOP Georgia Senate: 10% on $32K volume"
semantic_title: "Georgia Senate GOP odds stay low at 10% under volume"
telemetry: "10% · $32K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-24T10:14:05+00:00"
event_id: "CM-EVT-1S96Y2D1N4"
event_slug: "senatega-26"
event_question: "Will the Georgia Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEGA-26-R"
  question_raw: "Will Republicans win the Senate race in Georgia?"
  current_price: 0.099
  volume_24h_usd: 32161.27
  volume_cumulative_usd: 66623.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Market prices only a 10% chance Republicans win the Georgia Senate race, heavily Democratic-leaning at current odds."
  - "Kalshi records $32K in 24h, 48% of all-time volume, nearly half the contract's history traded in a single session."
  - "A near-half lifetime volume print at low odds may signal a catalyst, new polling, candidate news, or fundraising data."
  - "Resolves YES if the Republican candidate wins the Georgia Senate general election."
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
      kalshi_vol_24h_usd: 32161.27
sources:
  - label: "ClearMarket market record: Will the Georgia Senate race be decided by January 4, 2"
    url: "https://clearmarket.fyi/events/senatega-26"
    retrieved_at: "2026-07-24T10:14:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all-time Georgia Senate volume printing at 10% in one day suggests a fresh catalyst is circulating; desks should check for new polling or candidate developments driving the attention spike.
