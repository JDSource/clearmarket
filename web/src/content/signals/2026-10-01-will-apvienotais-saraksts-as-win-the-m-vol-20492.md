---
signal_id: "CMSIG20261001VS06"
signal_slug: "will-apvienotais-saraksts-as-win-the-m-vol-20492"
headline: "AS wins most Latvia seats 2026: 98% on $20K"
semantic_title: "Fresh volume backs AS to win most Latvian parliament seats"
telemetry: "98% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-01T15:04:01+00:00"
event_id: "CM-EVT-TPH1FR3YZ0"
event_slug: "latvian-parliamentary-election-winner"
event_question: "Will the Latvian parliamentary election result in a single party winning an outright majority by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0eac20f7ed673d0e99385158ea468f6540aa208abefb74613f8170c2f9909e53"
  question_raw: "Will Apvienotais Saraksts (AS) win the most seats in the 2026 Latvian parliamentary election?"
  current_price: 0.985
  volume_24h_usd: 20492.748284
  volume_cumulative_usd: 81136.74678499997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-03T00:00:00Z"
bullets:
  - "Polymarket prices Apvienotais Saraksts at 98% to win the most seats in the 2026 Latvian parliamentary election, near certainty."
  - "24h volume of $20K is 25% of all-time, suggesting a fresh wave of traders agreeing with the dominant consensus."
  - "The Baltic political context, AS as the established center-right bloc, supports a high-conviction single-party plurality."
  - "Resolves on official 2026 Latvian election results; the 2% residual reflects only black-swan coalition disruption risk."
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
      poly_vol_24h_usd: 20492.748284
sources:
  - label: "ClearMarket market record: Will the Latvian parliamentary election result in a sin"
    url: "https://clearmarket.fyi/events/latvian-parliamentary-election-winner"
    retrieved_at: "2026-10-01T15:04:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume arriving at 98% on a geopolitical contract signals market closure rather than debate, desks monitoring Baltic political risk can treat AS plurality as the base case and focus on coalition composition as the remaining variable.
