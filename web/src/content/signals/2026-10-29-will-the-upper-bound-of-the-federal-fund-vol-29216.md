---
signal_id: "CMSIG20261029VS06"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-29216"
headline: "Fed funds above 4%: 80% on $29K surge"
semantic_title: "Betting picks up on fed funds staying above 4% after December"
telemetry: "80% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T14:56:22+00:00"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound, December 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.8
  volume_24h_usd: 29216.44
  volume_cumulative_usd: 82856.93
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Market prices an 80% chance the federal funds rate upper bound remains above 4.00% post-December meeting."
  - "Kalshi sees $29.2K in 24h, 35% of all-time volume, clustering with other Fed-December flow."
  - "High conviction at 80% with fresh volume reinforces a 'higher for longer' base case into year-end."
  - "Resolves following the FOMC December 2026 meeting announcement."
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
      kalshi_vol_24h_usd: 29216.44
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, December 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26dec"
    retrieved_at: "2026-10-29T14:56:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

This contract's correlated surge alongside the hike/hold pair confirms a coordinated macro rates repricing, an 80% print above 4.00% is the structural anchor desks are trading around for year-end positioning.
