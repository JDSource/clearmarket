---
signal_id: "CMSIG20261013VS03"
signal_slug: "will-the-democratic-party-win-the-ga-11-vol-16180"
headline: "GA-11 Democrat: 2% on $16K Polymarket volume"
semantic_title: "GA-11 Democratic chances stay near zero despite fresh bets"
telemetry: "2% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T07:49:07+00:00"
event_id: "CM-EVT-Q69VMQDDC9"
event_slug: "ga-11-house-election-winner"
event_question: "Will the GA-11 House election be won by a Republican candidate in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc04a813ce0d0160a94dafaab3f3f018d99e7d6e4f36806bc3b548b2de3f8e280"
  question_raw: "Will the Democratic Party win the GA-11 House seat?"
  current_price: 0.019
  volume_24h_usd: 16180.544387
  volume_cumulative_usd: 33398.070941
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket holds Democratic win probability at 2% in GA-11, a Republican-leaning Georgia district."
  - "48% of all-time volume arrived in 24 hours, pulling lifetime activity forward sharply."
  - "Paired spike with NY-23 suggests systematic down-ballot Republican-seat positioning rather than district-specific news."
  - "Resolves on the GA-11 general election outcome."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 16180.544387
sources:
  - label: "ClearMarket market record: Will the GA-11 House election be won by a Republican ca"
    url: "https://clearmarket.fyi/events/ga-11-house-election-winner"
    retrieved_at: "2026-10-13T07:49:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous GA-11 and NY-23 spikes at near-zero Democratic prices point to a coordinated sweep of Republican-leaning seats, likely House-control hedging rather than idiosyncratic district flow.
