---
signal_id: "CMSIG20260725VS05"
signal_slug: "krg-declares-independence-from-iraq-by-d-vol-69599"
headline: "KRG independence by Dec 31: 8% on $70K"
semantic_title: "KRG independence by year-end stays a long shot at 8%"
telemetry: "8% · $70K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-25T09:43:16+00:00"
event_id: "CM-EVT-SPXZBC4MN7"
event_slug: "who-will-trump-talk-to"
event_question: "Will the KRG declare independence from Iraq by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x19e4c19193bb06609b83267b5d06fbd4c45d8848ff532a66ace9e8e77e3c991d"
  question_raw: "KRG declares independence from Iraq by December 31?"
  current_price: 0.077
  volume_24h_usd: 69599.63999999998
  volume_cumulative_usd: 267245.36046300014
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Kurdish Regional Government independence from Iraq at 8%, a tail risk, not a base case."
  - "$70K in 24h represents 26% of all-time volume, the second-largest single-day draw on this contract."
  - "Fresh attention at 8% suggests geopolitical developments, regional diplomacy, Baghdad tensions, or U.S. posture, are prompting reassessment."
  - "Contract resolves if KRG formally declares independence before December 31, 2026."
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
      poly_vol_24h_usd: 69599.63999999998
sources:
  - label: "ClearMarket market record: Will the KRG declare independence from Iraq by December"
    url: "https://clearmarket.fyi/events/who-will-trump-talk-to"
    retrieved_at: "2026-07-25T09:43:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 8% price drawing a quarter of lifetime volume in one day signals a geopolitical development worth investigating, tail-risk desks should identify the specific regional catalyst driving re-engagement.
