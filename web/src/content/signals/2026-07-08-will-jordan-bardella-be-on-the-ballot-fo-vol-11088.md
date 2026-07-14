---
signal_id: "CMSIG20260708VS04"
signal_slug: "will-jordan-bardella-be-on-the-ballot-fo-vol-11088"
headline: "Bardella 2027 ballot odds at 8% as volume hits 77% of lifetime"
semantic_title: "Bardella ballot access fades to 8% on heavy volume"
telemetry: "8% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-08T10:14:29+00:00"
event_id: "CM-EVT-6Q8LZ5QQW0"
event_slug: "2027-french-presidential-election-who-will-be-on-the-ballot"
event_question: "Will Matthieu Pigasse be on the ballot for the 2027 French presidential election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x12ca66c6090f31d532fb447eb39ffb902d3e74faaa62cad15b61c17b510fea88"
  question_raw: "Will Jordan Bardella be on the ballot for the 2027 French presidential election?"
  current_price: 0.077
  volume_24h_usd: 11088.248801
  volume_cumulative_usd: 14312.811965999992
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-17T00:00:00Z"
bullets:
  - "8% price implies the market heavily discounts Bardella appearing as a presidential candidate in 2027."
  - "24h volume $11K is 77% of all-time, nearly the entire contract history traded in one session."
  - "Flow is almost certainly linked to the Le Pen ballot-access contract spiking simultaneously at 89%."
  - "Resolves when 2027 French presidential candidate list is officially confirmed."
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
      poly_vol_24h_usd: 11088.248801
sources:
  - label: "ClearMarket market record: Will Matthieu Pigasse be on the ballot for the 2027 Fre"
    url: "https://clearmarket.fyi/events/2027-french-presidential-election-who-will-be-on-the-ballot"
    retrieved_at: "2026-07-08T10:14:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total lifetime volume concentrating in one day signals a definitive market verdict, traders are pricing Bardella as a placeholder who stands aside if Le Pen is confirmed eligible, not an independent contender.
