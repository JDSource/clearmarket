---
signal_id: "CMSIG20260616VS03"
signal_slug: "spacex-ipo-closing-market-cap-above-2t-vol-926218"
headline: "SpaceX IPO >$2T: 93% on $926K volume"
semantic_title: "Heavy flows defend SpaceX IPO above $2T at 93%"
telemetry: "93% · $926K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-16T12:50:46+00:00"
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
  - "Polymarket prices 93%, strong consensus that SpaceX IPO closes above the $2T threshold."
  - "24h volume $926K is 43% of all-time; largest single-day flow in the IPO valuation ladder."
  - "High conviction here anchors the strip: $2T treated as near-floor, $2.2T as the live debate."
  - "Resolution on IPO closing day; any delay or valuation revision is the primary tail risk."
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
    retrieved_at: "2026-06-16T12:50:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $2T contract commands the heaviest flow in the SpaceX strip, desks should use its 93% read as the implied valuation floor when sizing positions across the ladder.
