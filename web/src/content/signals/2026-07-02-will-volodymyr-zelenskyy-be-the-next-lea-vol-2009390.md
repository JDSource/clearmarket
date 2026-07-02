---
signal_id: "CMSIG20260702VS00"
signal_slug: "will-volodymyr-zelenskyy-be-the-next-lea-vol-2009390"
headline: "Zelenskyy next out: 0% on $2M Polymarket surge"
semantic_title: "Traders write off Zelenskyy as the next leader out before 2027"
telemetry: "0% · $2M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-02T10:35:06+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will a current leader lose power before 2027, excluding Viktor Orbán?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa1b9197a70166b28f64766c468da80dbfced6e64efac9b80d87cac9c0e1540aa"
  question_raw: "Will Volodymyr Zelenskyy be the next leader out before 2027?"
  current_price: 0.001
  volume_24h_usd: 2009390.963507
  volume_cumulative_usd: 4729782.168000999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "0% price signals market sees zero credible path to Zelenskyy exit before 2027."
  - "$2.01M in 24h, 42% of all-time volume, marks an extraordinary single-session flush."
  - "Spike likely resolves positioning after a near-miss catalyst, ceasefire noise, or coordinated arb sweep."
  - "Resolves before 2027; current price leaves no residual tail risk priced in."
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
      poly_vol_24h_usd: 2009390.963507
sources:
  - label: "ClearMarket market record: Will a current leader lose power before 2027, excluding"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-02T10:35:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The combination of a zero price and a $2M volume surge suggests desks are closing out speculative longs or arbitraging a linked multi-leg leadership basket rather than expressing fresh directional conviction.
