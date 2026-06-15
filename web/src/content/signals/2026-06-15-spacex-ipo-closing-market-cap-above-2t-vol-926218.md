---
signal_id: "CMSIG20260615VS03"
signal_slug: "spacex-ipo-closing-market-cap-above-2t-vol-926218"
headline: "SpaceX IPO above $2T: 93% on $926K inflow"
semantic_title: "Heavy flows stack conviction behind a $2T SpaceX floor"
telemetry: "93% · $926K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-15T13:52:22+00:00"
event_id: "CM-EVT-FDQNXYNKT6"
event_slug: "spacex-ipo-closing-market-cap-above"
event_question: "SpaceX IPO closing market cap, 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6619036865c2d27f1b1c00cd565ce74f6aa72ef93be29c315be36941d3559c59"
  question_raw: "SpaceX IPO closing market cap above $2T?"
  current_price: 0.93
  volume_24h_usd: 926218.8570059997
  volume_cumulative_usd: 2157189.453323009
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 93%, near-consensus that SpaceX IPO closes above $2T."
  - "24h volume $926K is 43% of all-time, the largest single-session dollar flow across the SpaceX strip."
  - "The $2T level functions as the market's baseline valuation anchor for the IPO."
  - "Spread to $2.2T (67%) marks the zone where real valuation disagreement begins."
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
      poly_vol_24h_usd: 926218.8570059997
sources:
  - label: "ClearMarket market record: SpaceX IPO closing market cap, 2027"
    url: "https://clearmarket.fyi/events/spacex-ipo-closing-market-cap-above"
    retrieved_at: "2026-06-15T13:52:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $2T contract drawing the strip's highest nominal 24h volume at near-certainty pricing confirms it as the reference floor, desks pricing SpaceX private shares or derivatives should anchor base-case models at or above this level.
