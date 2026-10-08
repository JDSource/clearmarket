---
signal_id: "CMSIG20261008VS01"
signal_slug: "will-the-republican-party-win-the-nc-04-vol-33077"
headline: "NC-04 GOP win: 5% on $33K volume spike"
semantic_title: "Traders pile into NC-04 as a near-certain Democratic hold"
telemetry: "5% · $33K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T15:10:56+00:00"
event_id: "CM-EVT-NWW6JR41T9"
event_slug: "nc-04-house-election-winner"
event_question: "NC-04 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe29af21f8c8b4646f0d9b771193ab99a2a75a3ae8b360c138f8fad1acdd12cf2"
  question_raw: "Will the Republican Party win the NC-04 House seat?"
  current_price: 0.047
  volume_24h_usd: 33077.717623000004
  volume_cumulative_usd: 67451.159414
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Republicans priced at 5%, market treats this newly redrawn seat as safely Democratic."
  - "24h volume of $33K equals 49% of all-time, large single-session commitment relative to contract history."
  - "NC-04 redrawn post-redistricting; surge may reflect traders confirming Democratic baseline ahead of filing deadlines."
  - "Resolves on November 2026 general election result for NC-04."
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
      poly_vol_24h_usd: 33077.717623000004
sources:
  - label: "ClearMarket market record: NC-04 House Election Winner"
    url: "https://clearmarket.fyi/events/nc-04-house-election-winner"
    retrieved_at: "2026-10-08T15:10:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-half of all-time volume printing in one session at 5% suggests the desk community is settling on NC-04 as a low-risk Democratic certainty worth positioning against any residual tail.
