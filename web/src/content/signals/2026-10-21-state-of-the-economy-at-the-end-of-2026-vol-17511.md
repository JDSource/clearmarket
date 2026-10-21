---
signal_id: "CMSIG20261021VS02"
signal_slug: "state-of-the-economy-at-the-end-of-2026-vol-17511"
headline: "US economy end-2026: 69% on $17K Kalshi inflow"
semantic_title: "Odds favor a healthy economy reading at end of 2026"
telemetry: "69% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T07:48:52+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXECONPATH-26-OHEAT"
  question_raw: "State of the economy at the end of 2026?"
  current_price: 0.693
  volume_24h_usd: 17511.94
  volume_cumulative_usd: 55969.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T14:55:00Z"
bullets:
  - "69% prices a 'healthy' or above-baseline economic state as the modal outcome through year-end."
  - "31% of all-time volume in 24h suggests a macro event, jobs data, Fed guidance, triggered fresh positioning."
  - "Odds staying near 70% through a volume surge implies the crowd is reaffirming, not revising, the base case."
  - "Resolves against Kalshi's defined economic-condition criteria at December 31, 2026."
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
      kalshi_vol_24h_usd: 17511.94
sources:
  - label: "ClearMarket market record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/events/kxeconpath-26"
    retrieved_at: "2026-10-21T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A macro contract drawing a third of its lifetime volume in one session is a useful sentiment barometer, the 69% hold through the surge tells desks that the fresh capital endorsed the prevailing growth narrative rather than hedging against deterioration.
