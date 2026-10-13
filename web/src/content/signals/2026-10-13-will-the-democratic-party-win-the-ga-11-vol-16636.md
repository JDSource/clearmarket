---
signal_id: "CMSIG20261013VS05"
signal_slug: "will-the-democratic-party-win-the-ga-11-vol-16636"
headline: "GA-11 Democrat: 1% on $17K Polymarket burst"
semantic_title: "Odds hold Democrats out of GA-11 at 1% on fresh volume"
telemetry: "1% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T15:33:23+00:00"
event_id: "CM-EVT-Q69VMQDDC9"
event_slug: "ga-11-house-election-winner"
event_question: "Will the GA-11 House election be won by a Republican candidate in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc04a813ce0d0160a94dafaab3f3f018d99e7d6e4f36806bc3b548b2de3f8e280"
  question_raw: "Will the Democratic Party win the GA-11 House seat?"
  current_price: 0.014
  volume_24h_usd: 16636.268197
  volume_cumulative_usd: 33853.794751
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats at 1% in GA-11, market treats this as a safe Republican seat."
  - "$16.6K in 24h is 49% of all-time flow, nearly half the contract's history in a single session."
  - "GA-11 is a reliably red suburban-rural district; volume at minimal odds fits a sweep-scenario hedge pattern."
  - "Resolves on November 2026 House election result."
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
      poly_vol_24h_usd: 16636.268197
sources:
  - label: "ClearMarket market record: Will the GA-11 House election be won by a Republican ca"
    url: "https://clearmarket.fyi/events/ga-11-house-election-winner"
    retrieved_at: "2026-10-13T15:33:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Clustered with similar 1% GA and TX contract spikes today, GA-11 volume is best read as part of a coordinated House-map position rather than district-specific news.
