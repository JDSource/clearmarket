---
signal_id: "CMSIG20260926VS05"
signal_slug: "will-kostadin-kostadinov-win-the-next-b-vol-14410"
headline: "Kostadinov Bulgaria president: 2% on $14K volume"
semantic_title: "Kostadinov trails badly in Bulgarian presidential market"
telemetry: "2% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T12:40:21+00:00"
event_id: "CM-EVT-C541X65QT7"
event_slug: "bulgaria-presidential-election"
event_question: "Will Bulgaria hold a presidential election by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa9e24f23e61265a798a2e484c0ead96255e6cd94034dfc0ab58343aa907cc390"
  question_raw: "Will Kostadin Kostadinov win the next  Bulgarian presidential election?"
  current_price: 0.015
  volume_24h_usd: 14410.174281999998
  volume_cumulative_usd: 52269.557077
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "Polymarket prices Kostadin Kostadinov at 2%, the market sees his path to the Bulgarian presidency as highly unlikely."
  - "$14.4K in 24h represents 28% of all-time volume, mirroring the activity pattern on the concurrent Gyurov contract."
  - "Simultaneous surges on multiple Bulgarian presidential candidates suggest a single information event is driving re-pricing across the field."
  - "Contract resolves on the official Bulgarian presidential election outcome."
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
      poly_vol_24h_usd: 14410.174281999998
sources:
  - label: "ClearMarket market record: Will Bulgaria hold a presidential election by 2026?"
    url: "https://clearmarket.fyi/events/bulgaria-presidential-election"
    retrieved_at: "2026-09-26T12:40:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Coordinated volume across Bulgarian presidential candidates in one session points to a field-wide repricing event, desks should identify the common catalyst, likely a debate, poll, or candidate development.
