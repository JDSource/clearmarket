---
signal_id: "CMSIG20261029VS04"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-47893"
headline: "Fed Dec hold: 22% on $47K Kalshi volume"
semantic_title: "A Fed pause in December stays a long shot at 22%"
telemetry: "22% · $48K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T14:56:22+00:00"
event_id: "CM-EVT-FKPVVZFMR8"
event_slug: "kxfeddecision-26dec"
event_question: "Will the Federal Reserve make a decision in December 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26DEC-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their December 2026 meeting?"
  current_price: 0.22
  volume_24h_usd: 47893.65
  volume_cumulative_usd: 157947.42
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Market places only 22% odds on the Fed leaving rates unchanged in December 2026."
  - "Kalshi sees $47.9K in 24h, 30% of all-time volume, moving in tandem with the hike contract."
  - "Flow here is the mirror of Spike 1, traders actively arbitraging the hike vs. hold split."
  - "Resolves on the FOMC December 2026 decision."
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
      kalshi_vol_24h_usd: 47893.65
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in December 20"
    url: "https://clearmarket.fyi/events/kxfeddecision-26dec"
    retrieved_at: "2026-10-29T14:56:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Correlated volume on both the hike and hold legs of the December FOMC contract points to active spread trading; desks should treat this alongside Spike 1 as a single macro rates repricing event.
