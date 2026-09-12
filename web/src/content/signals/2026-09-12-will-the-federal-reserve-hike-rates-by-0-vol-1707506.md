---
signal_id: "CMSIG20260912VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-1707506"
headline: "Fed Sept hold: 21% on $1.7M fresh inflow"
semantic_title: "No-hike odds hold at 21% through a volume surge"
telemetry: "21% · $1.7M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-12T11:56:57+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their September 2026 meeting?"
  current_price: 0.21
  volume_24h_usd: 1707506.21
  volume_cumulative_usd: 5667042.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi prices the Fed standing pat in September at just 21%, a clear minority view."
  - "$1.71M in 24h volume is 30% of the contract's entire all-time volume, flagging sharp two-sided interest."
  - "Paired surge with the 25bps contract suggests traders are actively hedging both sides of the FOMC decision."
  - "Resolves on the September 2026 Federal Reserve rate decision."
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
      kalshi_vol_24h_usd: 1707506.21
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-09-12T11:56:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous spike in both the hike and hold contracts tells a desk that rate uncertainty is live enough that real money is covering the tail, watch for a data print or Fed communication catalyst.
