---
signal_id: "CMSIG20261106VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-334516"
headline: "Fed Dec 25bp hike: 78% on $335K inflow"
semantic_title: "Traders back a Fed December hike at 78% with heavy fresh volume"
telemetry: "78% · $335K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T15:37:54+00:00"
event_id: "CM-EVT-FKPVVZFMR8"
event_slug: "kxfeddecision-26dec"
event_question: "Will the Federal Reserve make a decision in December 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26DEC-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their December 2026 meeting?"
  current_price: 0.78
  volume_24h_usd: 334516.75
  volume_cumulative_usd: 931385.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "At 78%, Kalshi pricing treats a December 25bp hike as the strong-probability outcome, not a coin flip."
  - "$334K in 24h represents 36% of all-time volume, a significant single-session commitment."
  - "Fresh money arriving here likely reflects a macro data print or Fed communication sharpening conviction."
  - "Contract resolves at the December 2026 FOMC meeting decision."
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
      kalshi_vol_24h_usd: 334516.75
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in December 20"
    url: "https://clearmarket.fyi/events/kxfeddecision-26dec"
    retrieved_at: "2026-11-06T15:37:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 78% handle with one-third of all-time volume in a single session tells rates desks that the market is treating December hike risk as effectively locked in, worth cross-checking against OIS pricing and Fed funds futures for basis.
