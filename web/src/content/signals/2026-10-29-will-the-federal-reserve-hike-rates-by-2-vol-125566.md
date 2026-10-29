---
signal_id: "CMSIG20261029VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-125566"
headline: "Fed Dec +25bps: 77% on $125K volume spike"
semantic_title: "Odds hold at 77% for a Fed hike in December"
telemetry: "77% · $126K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T14:56:22+00:00"
event_id: "CM-EVT-FKPVVZFMR8"
event_slug: "kxfeddecision-26dec"
event_question: "Will the Federal Reserve make a decision in December 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26DEC-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their December 2026 meeting?"
  current_price: 0.77
  volume_24h_usd: 125566.09
  volume_cumulative_usd: 342473.1
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Market prices a December 2026 Fed hike as the strong base case at 77%."
  - "Kalshi sees $125.6K in 24h, 37% of all-time volume, signaling concentrated fresh flow."
  - "Spike likely tied to macro data or Fed-speaker remarks sharpening December expectations."
  - "Resolves on the FOMC December 2026 rate decision."
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
      kalshi_vol_24h_usd: 125566.09
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in December 20"
    url: "https://clearmarket.fyi/events/kxfeddecision-26dec"
    retrieved_at: "2026-10-29T14:56:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Pulling in 37% of all-time volume in one day on a rates contract suggests macro desks are actively hedging December Fed risk, consistent with a live repricing of the hike path.
