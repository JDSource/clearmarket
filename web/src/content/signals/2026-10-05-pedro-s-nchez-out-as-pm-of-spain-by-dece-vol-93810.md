---
signal_id: "CMSIG20261005VS02"
signal_slug: "pedro-s-nchez-out-as-pm-of-spain-by-dece-vol-93810"
headline: "Sánchez out by Dec 31: 27% on $94K"
semantic_title: "Traders back Sánchez exit odds at 27% by year-end"
telemetry: "27% · $94K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T16:45:18+00:00"
event_id: "CM-EVT-1HSNRBYJ42"
event_slug: "pedro-snchez-out-as-pm-of-spain-by"
event_question: "Will Pedro Sánchez be out as Prime Minister of Spain by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x890f9b8de730479549e95027f26aad5ce89ecc4a42a6fd6316d0b0aec9a5aad1"
  question_raw: "Pedro Sánchez out as PM of Spain by December 31, 2026?"
  current_price: 0.27
  volume_24h_usd: 93810.857139
  volume_cumulative_usd: 330732.60380599997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Sánchez departure by December 31, 2026 at 27%, meaningful but not the base case."
  - "$94K in 24h represents 28% of all-time volume, pointing to a discrete catalyst driving attention."
  - "Spanish coalition fragility and budget deadlines in Q4 are the nearest pressure points."
  - "Contract resolves December 31, 2026."
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
      poly_vol_24h_usd: 93810.857139
sources:
  - label: "ClearMarket market record: Will Pedro Sánchez be out as Prime Minister of Spain by"
    url: "https://clearmarket.fyi/events/pedro-snchez-out-as-pm-of-spain-by"
    retrieved_at: "2026-10-05T16:45:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A concentrated surge to 28% of all-time volume on a year-end political-exit contract signals traders believe near-term Spanish parliamentary risk is underpriced at current odds.
