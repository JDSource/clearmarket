---
signal_id: "CMSIG20260728VS05"
signal_slug: "will-lydie-massard-be-the-joint-left-nom-vol-19465"
headline: "Massard French left nominee 2027: 0% on $19K"
semantic_title: "Lydie Massard as French left nominee prices at zero"
telemetry: "0% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-28T10:31:13+00:00"
event_id: "CM-EVT-WGPTXTJYH0"
event_slug: "france-united-left-primary-winner"
event_question: "Will the France United Left Primary produce a winner by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21b6425a17c08cd0591b06aa70557091efbe42a3a4ee419ee397518db9de3af1"
  question_raw: "Will Lydie Massard be the joint left nominee for the 2027 French presidential election?"
  current_price: 0.003
  volume_24h_usd: 19465.500000000004
  volume_cumulative_usd: 35633.55873300001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-11T00:00:00Z"
bullets:
  - "Polymarket prices Massard as the joint left nominee for 2027 at 0%, the market has fully ruled this out."
  - "$19K in 24h is 55% of all-time volume, a sharp spike on a contract the market treats as already settled."
  - "Volume at zero likely reflects a definitive disqualifying event, a withdrawal, endorsement of a rival, or official announcement."
  - "Resolves on formal nomination; no realistic path remains per current pricing."
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
      poly_vol_24h_usd: 19465.500000000004
sources:
  - label: "ClearMarket market record: Will the France United Left Primary produce a winner by"
    url: "https://clearmarket.fyi/events/france-united-left-primary-winner"
    retrieved_at: "2026-07-28T10:31:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 55% all-time volume day printing at 0% is a termination signal, a desk covering French political risk should confirm the specific catalyst (withdrawal or rival consolidation) and update 2027 election positioning accordingly.
