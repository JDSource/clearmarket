---
signal_id: "CMSIG20261017VS03"
signal_slug: "will-the-democratic-party-win-the-ca-06-vol-26002"
headline: "CA-06 Dem House: 97% on $26K Polymarket surge"
semantic_title: "CA-06 Democratic hold trades near certainty on fresh volume"
telemetry: "97% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T07:48:43+00:00"
event_id: "CM-EVT-BM3S3MCMH3"
event_slug: "ca-06-house-election-winner"
event_question: "Will the winner of the CA-06 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x903cbd11469e0948360f745ccbbaa9325bad2927c40f65a0f1796dd9fc54aec2"
  question_raw: "Will the Democratic Party win the CA-06 House seat?"
  current_price: 0.968
  volume_24h_usd: 26002.801753
  volume_cumulative_usd: 63281.797884
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices the Democratic candidate at 97%, effectively a resolution preview, not a contested market."
  - "$26K in 24h is 41% of all-time volume, notable for a market priced this close to certainty."
  - "Volume at near-100% odds typically reflects either arbitrage harvesting or a last-minute hedge against a tail risk."
  - "Resolves on 2026 California general election results."
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
      poly_vol_24h_usd: 26002.801753
sources:
  - label: "ClearMarket market record: Will the winner of the CA-06 House election be determin"
    url: "https://clearmarket.fyi/events/ca-06-house-election-winner"
    retrieved_at: "2026-10-17T07:48:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a 97% market is a yield-capture or tail-hedge signal rather than a directional bet, desks should note this as a liquidity housekeeping print, not a fundamental re-rating.
