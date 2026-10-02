---
signal_id: "CMSIG20261002VS02"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-11356"
headline: "Democrats NC-11 House: 65% on $11K Kalshi inflow"
semantic_title: "Buyers back Democrats in NC-11 as odds hold at 65%"
telemetry: "65% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T14:26:08+00:00"
event_id: "CM-EVT-0N8GC3M3K5"
event_slug: "kxhousenc11-26"
event_question: "Who will win the North Carolina 11th congressional district House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSENC11-26-DEM"
  question_raw: "Will Democratic win the House race for NC-11?"
  current_price: 0.65
  volume_24h_usd: 11356.07
  volume_cumulative_usd: 35416.84
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "65% price on Kalshi makes NC-11 a clear Democratic lean, pricing out roughly one-in-three Republican scenarios."
  - "24h volume of $11.4K is 32% of all-time handle, meaningful but contract still has room to build further."
  - "NC-11 is a historically Republican-leaning mountain district; 65% Democratic odds represent a notable political shift drawing scrutiny."
  - "Resolves on certified North Carolina 11th District House race result."
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
      kalshi_vol_24h_usd: 11356.07
sources:
  - label: "ClearMarket market record: Who will win the North Carolina 11th congressional dist"
    url: "https://clearmarket.fyi/events/kxhousenc11-26"
    retrieved_at: "2026-10-02T14:26:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh capital sustaining a 65% Democratic price in a traditionally red district warrants attention, volume here likely reflects new polling or candidate-specific news moving through political desks.
