---
signal_id: "CMSIG20260924VS06"
signal_slug: "will-the-republican-party-win-the-co-04-vol-10839"
headline: "CO-04 House GOP: 68% on $11K Polymarket burst"
semantic_title: "Republicans favored at 68% in CO-04 House race on volume push"
telemetry: "68% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T13:08:49+00:00"
event_id: "CM-EVT-7T2BJXLWQ5"
event_slug: "co-04-house-election-winner"
event_question: "CO-04 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x13d25ac2d08197538635b4879303c2e01e1e6f2250eaeca4cd2a81fbf864fb9d"
  question_raw: "Will the Republican Party win the CO-04 House seat?"
  current_price: 0.68
  volume_24h_usd: 10839.905544
  volume_cumulative_usd: 25123.117888999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "68% odds establish Republicans as solid favorites to hold Colorado's 4th Congressional District."
  - "43% of all-time Polymarket volume on this contract arrived in a single 24h window."
  - "A smaller contract seeing proportionally the largest all-time share suggests a specific local catalyst is in play."
  - "Resolves on the CO-04 House election result."
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
      poly_vol_24h_usd: 10839.905544
sources:
  - label: "ClearMarket market record: CO-04 House Election Winner"
    url: "https://clearmarket.fyi/events/co-04-house-election-winner"
    retrieved_at: "2026-09-24T13:08:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The highest all-time volume share in this batch, 43% in one day on a lower-dollar contract, flags a local news catalyst in CO-04 that political desks covering House control margins should investigate immediately.
