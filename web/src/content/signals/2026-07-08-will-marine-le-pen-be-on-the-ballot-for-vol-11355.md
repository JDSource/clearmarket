---
signal_id: "CMSIG20260708VS05"
signal_slug: "will-marine-le-pen-be-on-the-ballot-for-vol-11355"
headline: "Le Pen 2027 on ballot: 89% on $11K Polymarket flow"
semantic_title: "Le Pen ballot eligibility defended at 89% conviction"
telemetry: "89% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-08T10:14:29+00:00"
event_id: "CM-EVT-6Q8LZ5QQW0"
event_slug: "2027-french-presidential-election-who-will-be-on-the-ballot"
event_question: "Will Matthieu Pigasse be on the ballot for the 2027 French presidential election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa4a28a02e05eae793b93bd30cc7eb203525804435d5bcfe4889ffce8d94adcff"
  question_raw: "Will Marine Le Pen be on the ballot for the 2027 French presidential election?"
  current_price: 0.89
  volume_24h_usd: 11355.875476999998
  volume_cumulative_usd: 17606.957300999995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-17T00:00:00Z"
bullets:
  - "89% price reflects strong market confidence that Le Pen's legal situation will not bar her candidacy."
  - "24h volume $11K is 64% of all-time, dominant single-session activity for this contract."
  - "Concurrent Bardella (8%) and Le Pen win (27%) spikes suggest a coordinated French political repricing."
  - "Resolves when official 2027 presidential candidate list is published."
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
      poly_vol_24h_usd: 11355.875476999998
sources:
  - label: "ClearMarket market record: Will Matthieu Pigasse be on the ballot for the 2027 Fre"
    url: "https://clearmarket.fyi/events/2027-french-presidential-election-who-will-be-on-the-ballot"
    retrieved_at: "2026-07-08T10:14:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The cluster of French election contract volume in a single session indicates a catalyst, likely a court ruling or legal development, that traders are using to lock in Le Pen eligibility at high confidence while repricing Bardella out.
