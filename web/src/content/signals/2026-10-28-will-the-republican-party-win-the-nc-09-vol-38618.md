---
signal_id: "CMSIG20261028VS06"
signal_slug: "will-the-republican-party-win-the-nc-09-vol-38618"
headline: "GOP NC-09 House seat: 67% on $39K surge"
semantic_title: "Republicans hold 67% in NC-09 through active trading"
telemetry: "67% · $39K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T14:50:28+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x31727e0e298757e552661f62733cc401c6066b80a7d2607d2ac56b729eb15a00"
  question_raw: "Will the Republican Party win the NC-09 House seat?"
  current_price: 0.67
  volume_24h_usd: 38618.409276
  volume_cumulative_usd: 101037.794293
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans at 67% in NC-09, a solid but soft favorite, far from certain."
  - "38% of all-time volume cleared in 24 hours, consistent with the parallel Democratic-side contract activity."
  - "The paired volume across both NC-09 contracts points to a contested-district repricing event, not one-sided flow."
  - "Resolves on the certified NC-09 House election result."
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
      poly_vol_24h_usd: 38618.409276
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-28T14:50:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Trading both sides of NC-09 simultaneously at near-complementary prices suggests desks are stress-testing the district model rather than expressing a clean directional view.
