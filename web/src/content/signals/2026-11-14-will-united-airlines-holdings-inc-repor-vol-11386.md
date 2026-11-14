---
signal_id: "CMSIG20261114VS04"
signal_slug: "will-united-airlines-holdings-inc-repor-vol-11386"
headline: "UAL >182M passengers: 98% on $11K volume"
semantic_title: "United above 182M passengers holds at 98% through a volume push"
telemetry: "98% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-14T07:48:40+00:00"
event_id: "CM-EVT-XL3H4QDNB2"
event_slug: "kxuala-28janpax"
event_question: "United Airlines passenger count, January 2028"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUALA-28JANPAX-182000000"
  question_raw: "Will United Airlines Holdings Inc. report Above 182 million passengers flown in 2026?"
  current_price: 0.98
  volume_24h_usd: 11386.13
  volume_cumulative_usd: 15137.29
  arbitration_model: "kalshi_staff"
  resolves_at: "2028-03-31T05:00:00Z"
bullets:
  - "Kalshi prices United Airlines above 182 million passengers at 98%, an adjacent, slightly easier threshold to the 184M contract."
  - "24h volume of $11K is 75% of all-time, same session dominance pattern as the 184M contract."
  - "Paired trading across both thresholds indicates structured positioning around United's upcoming traffic disclosure."
  - "Resolves on United's official annual passenger count."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 11386.13
sources:
  - label: "ClearMarket market record: United Airlines passenger count, January 2028"
    url: "https://clearmarket.fyi/events/kxuala-28janpax"
    retrieved_at: "2026-11-14T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous 75%-of-all-time volume on adjacent passenger-count contracts points to a coordinated desk position ahead of United's data release, treating both bars as near-certain clears.
