---
signal_id: "CMSIG20260814VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-166196"
headline: "Fed Sep hike 25bps: 28% on $166K surge"
semantic_title: "Fed September hike stays a long shot at 28%"
telemetry: "28% · $166K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-14T09:04:43+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their September 2026 meeting?"
  current_price: 0.28
  volume_24h_usd: 166196.23
  volume_cumulative_usd: 597100.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "28% prices a September hike as an unlikely but non-trivial tail risk."
  - "$166K hit in 24h, 28% of all-time contract volume, the largest single-day share."
  - "Fresh macro data or Fed communication likely driving reassessment of the hiking path."
  - "Resolves on FOMC September 2026 rate decision."
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
      kalshi_vol_24h_usd: 166196.23
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-08-14T09:04:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy one-day volume into a 28% hike contract tells a macro desk that traders are actively hedging a non-consensus Fed move rather than dismissing it.
