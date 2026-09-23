---
signal_id: "CMSIG20260923VS05"
signal_slug: "will-kostadin-kostadinov-win-the-next-b-vol-12989"
headline: "Kostadinov Bulgaria president: 1% on $13K"
semantic_title: "Kostadinov Bulgarian presidential odds sit at 1%"
telemetry: "1% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T13:18:01+00:00"
event_id: "CM-EVT-C541X65QT7"
event_slug: "bulgaria-presidential-election"
event_question: "Will Bulgaria hold a presidential election by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa9e24f23e61265a798a2e484c0ead96255e6cd94034dfc0ab58343aa907cc390"
  question_raw: "Will Kostadin Kostadinov win the next  Bulgarian presidential election?"
  current_price: 0.006
  volume_24h_usd: 12989.656719000002
  volume_cumulative_usd: 37368.012795
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "Polymarket prices Kostadinov at 1%, effectively ruling out his presidential win in the current contract window."
  - "24h volume of $13K is 35% of all-time handle, a disproportionate single-day surge for a near-zero outcome."
  - "The far-right Bulgarian politician's contract drawing fresh volume at 1% may reflect geopolitical monitoring tied to Bulgaria's NATO/EU positioning."
  - "Resolves on the next Bulgarian presidential election result."
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
      poly_vol_24h_usd: 12989.656719000002
sources:
  - label: "ClearMarket market record: Will Bulgaria hold a presidential election by 2026?"
    url: "https://clearmarket.fyi/events/bulgaria-presidential-election"
    retrieved_at: "2026-09-23T13:18:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 35% all-time volume session on a 1% contract in a Central European election suggests geopolitically motivated monitoring, desks tracking Balkans stability or EU cohesion should note the attention even if the price signal is negligible.
