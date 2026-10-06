---
signal_id: "CMSIG20261006VS02"
signal_slug: "pedro-s-nchez-out-as-pm-of-spain-by-dece-vol-100752"
headline: "Sánchez out by Dec 31: 28% on $101K volume"
semantic_title: "Traders back Sánchez surviving as Spain's PM through year-end"
telemetry: "28% · $101K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-06T07:48:59+00:00"
event_id: "CM-EVT-1HSNRBYJ42"
event_slug: "pedro-snchez-out-as-pm-of-spain-by"
event_question: "Will Pedro Sánchez be out as Prime Minister of Spain by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x890f9b8de730479549e95027f26aad5ce89ecc4a42a6fd6316d0b0aec9a5aad1"
  question_raw: "Pedro Sánchez out as PM of Spain by December 31, 2026?"
  current_price: 0.28
  volume_24h_usd: 100752.56612700004
  volume_cumulative_usd: 369362.5680640001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Sánchez exit at 28%, the market leans toward him remaining PM through year-end."
  - "$101K in 24h volume equals 27% of all-time, pointing to a discrete political catalyst driving renewed interest."
  - "A 28% exit probability reflects live coalition fragility in Spain without the market calling an imminent collapse."
  - "Resolves if Sánchez leaves the PM role by December 31, 2026."
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
      poly_vol_24h_usd: 100752.56612700004
sources:
  - label: "ClearMarket market record: Will Pedro Sánchez be out as Prime Minister of Spain by"
    url: "https://clearmarket.fyi/events/pedro-snchez-out-as-pm-of-spain-by"
    retrieved_at: "2026-10-06T07:48:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $100K+ volume day on the Sánchez exit contract flags that a desk should monitor Spanish coalition news closely, the 28% price leaves meaningful tail risk on the table heading into year-end.
