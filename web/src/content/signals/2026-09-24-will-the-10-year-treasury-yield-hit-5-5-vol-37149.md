---
signal_id: "CMSIG20260924VS04"
signal_slug: "will-the-10-year-treasury-yield-hit-5-5-vol-37149"
headline: "10-yr yield 5.5% by 2027: 26% on $37K"
semantic_title: "Traders back a 10-year at 5.5% staying a long shot before 2027"
telemetry: "26% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T07:48:17+00:00"
event_id: "CM-EVT-4F238D6VR7"
event_slug: "how-high-will-10-year-treasury-yield-go-before-2027"
event_question: "What is the maximum 10-year Treasury yield before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1f10b1f557ab254487c22a6b7cd4b4a3b14e561c0017bc6fc58bb81f306ad558"
  question_raw: "Will the 10-year Treasury yield hit 5.5% before 2027?"
  current_price: 0.26
  volume_24h_usd: 37149.604156999994
  volume_cumulative_usd: 93122.425764
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the 10-year Treasury hitting 5.5% before 2027 at 26%, firmly in tail-risk territory."
  - "$37.2K in 24h represents 40% of all-time volume, the largest single-day share in this contract's life."
  - "A spike to 40% of lifetime volume on a rates-threshold contract points to fresh macro anxiety around the Fed hike narrative."
  - "Resolves if the 10-year yield closes at or above 5.5% at any point before January 1, 2027."
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
      poly_vol_24h_usd: 37149.604156999994
sources:
  - label: "ClearMarket market record: What is the maximum 10-year Treasury yield before 2027?"
    url: "https://clearmarket.fyi/events/how-high-will-10-year-treasury-yield-go-before-2027"
    retrieved_at: "2026-09-24T07:48:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty percent of lifetime volume in one session on a tail-risk rates contract is a meaningful flag, desks should note whether this is hedging activity linked to the elevated Fed hike odds in Spike 0.
