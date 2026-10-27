---
signal_id: "CMSIG20261027VS02"
signal_slug: "will-together-win-the-most-seats-in-the-vol-397689"
headline: "Together most seats: 0% on $398K inflow"
semantic_title: "Together party all but ruled out for most seats by traders"
telemetry: "0% · $398K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T07:49:11+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4e9cff8a3aeac036225fedcc98af9b0d55284b3f430b599e7f61b059c1e177af"
  question_raw: "Will Together win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.004
  volume_24h_usd: 397689.747112
  volume_cumulative_usd: 1189532.2450970002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Price at 0%, Polymarket traders have effectively closed the book on Together winning a plurality of Knesset seats."
  - "$398K in 24h is 33% of all-time volume, an unusually large surge into a contract priced at the floor."
  - "Volume into a zero-priced contract indicates confirmation trading or position liquidation, not genuine two-sided discovery."
  - "Resolves on official Knesset seat distribution after the 2026 Israeli election."
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
      poly_vol_24h_usd: 397689.747112
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-27T07:49:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $398K surge into a 0%-priced contract is a strong signal that traders are closing out residual long exposure on Together, desks should treat this as a definitive market consensus call, not a live race.
