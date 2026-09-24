---
signal_id: "CMSIG20260924VS05"
signal_slug: "will-the-10-year-treasury-yield-hit-5-5-vol-36295"
headline: "10Y yield 5.5% by 2027: 30% on $36K surge"
semantic_title: "Traders back 10-year yield hitting 5.5% before 2027 at 30%"
telemetry: "30% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T13:08:49+00:00"
event_id: "CM-EVT-4F238D6VR7"
event_slug: "how-high-will-10-year-treasury-yield-go-before-2027"
event_question: "What is the maximum 10-year Treasury yield before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1f10b1f557ab254487c22a6b7cd4b4a3b14e561c0017bc6fc58bb81f306ad558"
  question_raw: "Will the 10-year Treasury yield hit 5.5% before 2027?"
  current_price: 0.296
  volume_24h_usd: 36295.396251
  volume_cumulative_usd: 94484.00247499999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "30% odds on a 5.5% 10-year yield before year-end reflect meaningful but minority-view tail risk."
  - "Polymarket logs $36K in 24h, 38% of all-time contract volume, a sharp single-session concentration."
  - "Fresh volume alongside active Fed hike contracts (Spikes 0 and 3) shows rates anxiety spreading across tenors."
  - "Resolves if the 10-year Treasury yield touches 5.5% before January 1, 2027."
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
      poly_vol_24h_usd: 36295.396251
sources:
  - label: "ClearMarket market record: What is the maximum 10-year Treasury yield before 2027?"
    url: "https://clearmarket.fyi/events/how-high-will-10-year-treasury-yield-go-before-2027"
    retrieved_at: "2026-09-24T13:08:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly 40% of all-time volume in one session on the 5.5% yield contract tells fixed-income desks the market is seriously stress-testing upside rate scenarios concurrent with repricing short-end Fed expectations.
