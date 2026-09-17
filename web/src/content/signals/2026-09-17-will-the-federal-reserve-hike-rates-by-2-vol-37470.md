---
signal_id: "CMSIG20260917VS05"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-37470"
headline: "Fed Dec. 25bps hike: 69% on $37K volume"
semantic_title: "December 25bps hike holds above 50% as traders pile in"
telemetry: "69% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-17T13:05:20+00:00"
event_id: "CM-EVT-FKPVVZFMR8"
event_slug: "kxfeddecision-26dec"
event_question: "Will the Federal Reserve make a decision in December 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26DEC-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their December 2026 meeting?"
  current_price: 0.69
  volume_24h_usd: 37470.05
  volume_cumulative_usd: 66108.3
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Kalshi prices a 69% chance of a 25bps Fed hike at the December 2026 meeting, a clear lean."
  - "$37K in 24h is 57% of all-time volume, showing sustained rate-path interest extending to year-end."
  - "December pricing at 69% for a hike contrasts with October near-toss-up, implying a delayed move view."
  - "Resolves on the December 2026 FOMC decision."
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
      kalshi_vol_24h_usd: 37470.05
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in December 20"
    url: "https://clearmarket.fyi/events/kxfeddecision-26dec"
    retrieved_at: "2026-09-17T13:05:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The December hike contract pricing well above October suggests desks are building a 'skip-then-hike' scenario, a tradeable Fed path view worth flagging for rates strategy.
