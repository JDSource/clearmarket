---
signal_id: "CMSIG20261028VS06"
signal_slug: "will-the-republican-party-win-the-nc-09-vol-42064"
headline: "GOP NC-09 House seat: 68% on $42K"
semantic_title: "Republicans stay favored in NC-09 as volume tests 68%"
telemetry: "68% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T15:35:02+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x31727e0e298757e552661f62733cc401c6066b80a7d2607d2ac56b729eb15a00"
  question_raw: "Will the Republican Party win the NC-09 House seat?"
  current_price: 0.68
  volume_24h_usd: 42064.133147
  volume_cumulative_usd: 104583.518164
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans winning NC-09 at 68%, a comfortable but not decisive lead for the GOP."
  - "40% of all-time volume in 24h pairs with the Democratic NC-09 contract spike, reflecting two-sided action on the same race."
  - "Combined volume across both NC-09 contracts signals this district is drawing serious late-cycle attention."
  - "Resolves on the certified winner of the NC-09 House general election."
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
      poly_vol_24h_usd: 42064.133147
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-28T15:35:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous volume spike on both the GOP and Democratic NC-09 contracts points to active two-sided trading, likely driven by fresh district-level data, making NC-09 a live watch for House control scenario analysis.
