---
signal_id: "CMSIG20260727VS06"
signal_slug: "will-lydie-massard-be-the-joint-left-nom-vol-12037"
headline: "Massard 2027 French left pick: 0% on $12K"
semantic_title: "Odds on Massard as French left nominee in 2027 sit at zero"
telemetry: "0% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-27T11:16:33+00:00"
event_id: "CM-EVT-WGPTXTJYH0"
event_slug: "france-united-left-primary-winner"
event_question: "Will the France United Left Primary produce a winner by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21b6425a17c08cd0591b06aa70557091efbe42a3a4ee419ee397518db9de3af1"
  question_raw: "Will Lydie Massard be the joint left nominee for the 2027 French presidential election?"
  current_price: 0.005
  volume_24h_usd: 12037.400000000001
  volume_cumulative_usd: 18968.058733000013
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-11T00:00:00Z"
bullets:
  - "Polymarket prices Lydie Massard as the joint left nominee for the 2027 French presidential race at 0%."
  - "24h volume $12K is 63% of the contract's all-time total, the market is reaching a definitive verdict."
  - "Zero probability reflects the crowded and more prominent French left field; Massard carries negligible public profile."
  - "2027 French presidential election remains over a year away; this contract is effectively closed."
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
      poly_vol_24h_usd: 12037.400000000001
sources:
  - label: "ClearMarket market record: Will the France United Left Primary produce a winner by"
    url: "https://clearmarket.fyi/events/france-united-left-primary-winner"
    retrieved_at: "2026-07-27T11:16:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 0% price absorbing 63% of all-time volume is a market closing the door, desks tracking French political risk should focus capital on higher-probability left-flank candidates rather than this name.
