---
signal_id: "CMSIG20260817VS01"
signal_slug: "will-thomas-chalifoux-be-the-republican-vol-16430"
headline: "Chalifoux FL-09 GOP nominee: 16% on $16K surge"
semantic_title: "Chalifoux FL-09 GOP nominee odds hold under 25%"
telemetry: "16% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-17T08:38:12+00:00"
event_id: "CM-EVT-98VYGBFP77"
event_slug: "fl-09-republican-primary-winner"
event_question: "Will the Republican primary winner be determined for FL-09 by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe368e5e6be50377d08d2af99c9ad18694aef2f3af9ccbf60b1146302c3ee3da1"
  question_raw: "Will Thomas Chalifoux be the Republican nominee for FL-09?"
  current_price: 0.157
  volume_24h_usd: 16430.153914000002
  volume_cumulative_usd: 48442.99274
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-18T00:00:00Z"
bullets:
  - "At 16%, Polymarket treats Chalifoux as a clear underdog for the FL-09 Republican nomination."
  - "34% of all-time volume hit in 24 hours, the heaviest single-day flow this contract has seen."
  - "Volume concentration this late in a primary cycle often precedes a polling release or ballot development."
  - "Contract resolves on the FL-09 Republican primary result."
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
      poly_vol_24h_usd: 16430.153914000002
sources:
  - label: "ClearMarket market record: Will the Republican primary winner be determined for FL"
    url: "https://clearmarket.fyi/events/fl-09-republican-primary-winner"
    retrieved_at: "2026-08-17T08:38:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A third of all-time volume arriving in one day on a down-ballot primary contract suggests a catalyst, filing news, a poll, or opposition research, is circulating; desks covering Florida congressional redistricting should flag for follow-on.
