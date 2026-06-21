---
signal_id: "CMSIG20260621VS03"
signal_slug: "spacex-ipo-closing-market-cap-above-2t-vol-926218"
headline: "SpaceX IPO above $2T: 93% on $926K volume"
semantic_title: "Heavy flows defend SpaceX IPO above the $2T threshold"
telemetry: "93% · $926K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-21T11:14:34+00:00"
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
  - "Polymarket at 93%, strong consensus that IPO closing cap clears $2T comfortably."
  - "24h volume $926K is the largest single-session dollar sum across all SpaceX strikes today."
  - "High price with high volume suggests institutional hedgers locking in the floor valuation."
  - "Resolves at IPO close; 7% residual risk priced in covers deal delay or macro dislocation."
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
    retrieved_at: "2026-06-21T11:14:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $2T strike is where the largest capital is deployed at near-certainty pricing, a desk should treat $2T as the market-consensus IPO floor and size risk accordingly above that level.
