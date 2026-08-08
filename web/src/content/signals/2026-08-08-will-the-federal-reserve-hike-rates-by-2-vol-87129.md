---
signal_id: "CMSIG20260808VS02"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-87129"
headline: "Fed 25bps Sept hike: 36% on $87K volume"
semantic_title: "A 25bps Fed hike in September draws fresh attention at 36%"
telemetry: "36% · $87K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-08T08:36:03+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their September 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 87129.83
  volume_cumulative_usd: 341985.87
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi prices a 25bps September hike at 36%, a meaningful minority scenario, not dismissed."
  - "24h volume of $87K hits exactly 25% of all-time, a clean liquidity milestone for this contract."
  - "Activity likely mirrors the Spike 1 hold contract, as traders hedge across both outcomes."
  - "Resolves at the September 2026 Federal Reserve meeting announcement."
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
      kalshi_vol_24h_usd: 87129.83
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-08-08T08:36:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 36% pricing and a 25% all-time volume share in one session, a desk should treat a September 25bps hike as a live tail risk worth hedging, not a rounding error.
