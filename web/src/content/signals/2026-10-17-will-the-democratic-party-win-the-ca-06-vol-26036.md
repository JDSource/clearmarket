---
signal_id: "CMSIG20261017VS03"
signal_slug: "will-the-democratic-party-win-the-ca-06-vol-26036"
headline: "CA-06 Democrat: 97% on $26K Polymarket surge"
semantic_title: "CA-06 Democratic hold near certainty; volume backs the 97%"
telemetry: "97% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T11:58:01+00:00"
event_id: "CM-EVT-BM3S3MCMH3"
event_slug: "ca-06-house-election-winner"
event_question: "Will the winner of the CA-06 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x903cbd11469e0948360f745ccbbaa9325bad2927c40f65a0f1796dd9fc54aec2"
  question_raw: "Will the Democratic Party win the CA-06 House seat?"
  current_price: 0.968
  volume_24h_usd: 26036.181752999997
  volume_cumulative_usd: 63315.177884000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats at 97%, effectively treating this seat as resolved before election day."
  - "24h volume of $26K is 41% of all-time, a notable surge into a near-certain outcome."
  - "Yield-seeking flow into settled contracts often reflects broader portfolio hedging or arbitrage against correlated markets."
  - "Resolves on November 2026 election night."
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
      poly_vol_24h_usd: 26036.181752999997
sources:
  - label: "ClearMarket market record: Will the winner of the CA-06 House election be determin"
    url: "https://clearmarket.fyi/events/ca-06-house-election-winner"
    retrieved_at: "2026-10-17T11:58:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy flow into a 97% contract signals arbitrage or hedge activity rather than directional uncertainty, desks should check correlated California downballot contracts for mispricing.
