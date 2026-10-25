---
signal_id: "CMSIG20261025VS02"
signal_slug: "will-together-win-the-most-seats-in-the-vol-183786"
headline: "Together most seats: 0% on $184K volume"
semantic_title: "Together party effectively ruled out for first place at 0%"
telemetry: "0% · $184K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-25T12:57:02+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4e9cff8a3aeac036225fedcc98af9b0d55284b3f430b599e7f61b059c1e177af"
  question_raw: "Will Together win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.003
  volume_24h_usd: 183786.37615700002
  volume_cumulative_usd: 549329.063039
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "0% price is a near-total dismissal, the market treats a Together plurality finish as essentially impossible."
  - "Polymarket saw $184K in 24h, 33% of all-time volume, a decisive crowd piling in to confirm a verdict."
  - "Volume at zero-priced contracts typically marks settlement positioning or arbitrage cleanup, not genuine speculation."
  - "Resolves on official 2026 Israeli legislative election seat tallies."
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
      poly_vol_24h_usd: 183786.37615700002
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-25T12:57:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Six-figure volume on a zero-priced contract tells a desk that traders are closing positions or arbitraging residual liquidity, the Israeli center-left slate has been functionally eliminated by market consensus.
