---
signal_id: "CMSIG20261013VS07"
signal_slug: "will-the-republican-party-win-the-nc-08-vol-11056"
headline: "NC-08 Republican: 97% on $11K Polymarket flow"
semantic_title: "Republicans priced at 97% to hold NC-08 on fresh volume"
telemetry: "97% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T15:33:23+00:00"
event_id: "CM-EVT-M48NB8LSF4"
event_slug: "nc-08-house-election-winner"
event_question: "NC-08 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa4b1d5033cae899d9865ee6a50007ed9df1d5dcd5393ab6d44eeb61d30eaf5df"
  question_raw: "Will the Republican Party win the NC-08 House seat?"
  current_price: 0.974
  volume_24h_usd: 11056.343684000001
  volume_cumulative_usd: 27458.097113000003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans at 97% in NC-08, near-certain hold, with minimal priced risk."
  - "$11K in 24h is 40% of all-time contract volume; late-cycle flow into a decided race flags position cleanup."
  - "NC-08 has trended reliably Republican; volume at 97% mirrors the TX-04/GA-11 safe-seat pattern today."
  - "Resolves on the November 2026 House election result."
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
      poly_vol_24h_usd: 11056.343684000001
sources:
  - label: "ClearMarket market record: NC-08 House Election Winner"
    url: "https://clearmarket.fyi/events/nc-08-house-election-winner"
    retrieved_at: "2026-10-13T15:33:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The NC-08 spike fits today's broader pattern of traders consolidating positions in safe Republican seats, likely as part of House majority scenario modeling heading into the final weeks.
