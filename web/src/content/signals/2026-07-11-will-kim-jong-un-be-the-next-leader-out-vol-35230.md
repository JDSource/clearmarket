---
signal_id: "CMSIG20260711VS03"
signal_slug: "will-kim-jong-un-be-the-next-leader-out-vol-35230"
headline: "Kim Jong Un out before 2027: 0% on $35K"
semantic_title: "Heavy flows defend the Kim Jong Un leadership status quo"
telemetry: "0% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-11T09:24:55+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will the next leader out of power before 2027 be someone other than Orban?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa8e9566651e959f6b5807a45d8e89f2eb1238be4fe9ee63100f9be29a326d56a"
  question_raw: "Will Kim Jong Un be the next leader out before 2027?"
  current_price: 0.001
  volume_24h_usd: 35230.0
  volume_cumulative_usd: 135347.113176
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket holds Kim Jong Un leadership departure at 0%, reflecting market consensus of near-zero near-term regime change."
  - "26% of all-time volume in 24h, $35K, is a modest but notable acceleration for a geopolitical tail-risk contract."
  - "North Korea health speculation or a state-media appearance cycle may have drawn fresh attention to the contract."
  - "Resolves before end of 2026; 0% price implies no credible intelligence leak or succession signal in current market."
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
      poly_vol_24h_usd: 35230.0
sources:
  - label: "ClearMarket market record: Will the next leader out of power before 2027 be someon"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-11T09:24:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume uptick on a 0%-priced leadership-change contract is a low-signal noise event for most desks, but geopolitical analysts should cross-reference against any recent DPRK state-media gaps or South Korean intelligence commentary that may have triggered the brief attention surge.
