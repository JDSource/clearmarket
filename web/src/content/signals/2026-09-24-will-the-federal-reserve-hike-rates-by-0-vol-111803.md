---
signal_id: "CMSIG20260924VS03"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-111803"
headline: "Fed Oct hold: 37% on $112K Kalshi volume"
semantic_title: "A Fed October pause sits at 37% as traders push back"
telemetry: "37% · $112K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T13:08:49+00:00"
event_id: "CM-EVT-FPF77GZ320"
event_slug: "kxfeddecision-26oct"
event_question: "Will the Federal Reserve make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26OCT-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their October 2026 meeting?"
  current_price: 0.37
  volume_24h_usd: 111803.2
  volume_cumulative_usd: 374483.61
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T18:05:00Z"
bullets:
  - "37% odds on a 0bps October outcome put a pause firmly in minority territory versus a hike."
  - "$112K in 24h covers 30% of all-time volume on this contract in a single session."
  - "Paired with Spike 0's 63% hike odds, the two contracts reveal a market leaning decisively toward action."
  - "Resolves on the FOMC October 2026 rate decision."
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
      kalshi_vol_24h_usd: 111803.2
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in October 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-26oct"
    retrieved_at: "2026-09-24T13:08:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous volume surge on both the hike and hold contracts reflects active two-sided positioning, desks are not just picking a side but hedging the distribution of October outcomes.
