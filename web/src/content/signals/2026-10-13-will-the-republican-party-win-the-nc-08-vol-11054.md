---
signal_id: "CMSIG20261013VS05"
signal_slug: "will-the-republican-party-win-the-nc-08-vol-11054"
headline: "NC-08 Republican: 96% on $11K Polymarket inflow"
semantic_title: "NC-08 Republican hold near certain as volume builds late"
telemetry: "96% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T07:49:07+00:00"
event_id: "CM-EVT-M48NB8LSF4"
event_slug: "nc-08-house-election-winner"
event_question: "NC-08 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa4b1d5033cae899d9865ee6a50007ed9df1d5dcd5393ab6d44eeb61d30eaf5df"
  question_raw: "Will the Republican Party win the NC-08 House seat?"
  current_price: 0.962
  volume_24h_usd: 11054.303684
  volume_cumulative_usd: 27456.057113
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republican retention of NC-08 at 96%, leaving almost no room for a Democratic upset."
  - "40% of all-time volume cleared in 24 hours, compressing meaningful lifetime activity into one session."
  - "Late money at near-certainty odds typically reflects closing out opposing positions rather than new directional conviction."
  - "Resolves on the NC-08 general election result."
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
      poly_vol_24h_usd: 11054.303684
sources:
  - label: "ClearMarket market record: NC-08 House Election Winner"
    url: "https://clearmarket.fyi/events/nc-08-house-election-winner"
    retrieved_at: "2026-10-13T07:49:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume piling into a 96% contract in the final pre-election window suggests desks are liquidating residual Democratic exposure rather than opening fresh Republican bets.
