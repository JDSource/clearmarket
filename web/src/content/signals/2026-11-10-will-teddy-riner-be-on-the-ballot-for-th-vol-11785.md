---
signal_id: "CMSIG20261110VS01"
signal_slug: "will-teddy-riner-be-on-the-ballot-for-th-vol-11785"
headline: "Riner 2027 French ballot: 28% on $11K volume"
semantic_title: "Teddy Riner on the 2027 French ballot stays a long shot"
telemetry: "28% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-10T07:48:26+00:00"
event_id: "CM-EVT-6Q8LZ5QQW0"
event_slug: "2027-french-presidential-election-who-will-be-on-the-ballot"
event_question: "Will Marine Le Pen be on the ballot for the 2027 French presidential election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4a467cd0e45358dfc86a1be7e9a7ecf1c0a563e3535f8cf6690bfa358a1cbf6f"
  question_raw: "Will Teddy Riner be on the ballot for the 2027 French presidential election?"
  current_price: 0.282
  volume_24h_usd: 11785.157644
  volume_cumulative_usd: 36698.110961
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-17T00:00:00Z"
bullets:
  - "28% on Polymarket prices Riner's presidential candidacy as unlikely but not negligible."
  - "24h volume of $11.8K is 32% of all-time, a meaningful spike for a niche political contract."
  - "Renewed attention may track a public statement or media speculation about Riner's political ambitions."
  - "Contract resolves on whether Riner formally appears on the 2027 French presidential ballot."
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
      poly_vol_24h_usd: 11785.157644
sources:
  - label: "ClearMarket market record: Will Marine Le Pen be on the ballot for the 2027 French"
    url: "https://clearmarket.fyi/events/2027-french-presidential-election-who-will-be-on-the-ballot"
    retrieved_at: "2026-11-10T07:48:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-third all-time volume burst on a sub-$40K contract suggests a specific news trigger around Riner's political intentions, worth monitoring French political press for a candidacy signal before 2027 filing deadlines.
