---
signal_id: "CMSIG20261021VS05"
signal_slug: "state-of-the-economy-at-the-end-of-2026-vol-17596"
headline: "Economy stable end-2026: 69% on $18K volume"
semantic_title: "Traders back a recession-free U.S. economy at end of 2026"
telemetry: "69% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T13:25:08+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXECONPATH-26-OHEAT"
  question_raw: "State of the economy at the end of 2026?"
  current_price: 0.692
  volume_24h_usd: 17596.13
  volume_cumulative_usd: 55958.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T14:55:00Z"
bullets:
  - "Kalshi prices a 69% chance the U.S. economy avoids recession or significant downturn by end of 2026."
  - "31% of all-time volume, $18K, cleared in 24 hours, reflecting fresh macro-data sensitivity."
  - "At 69%, the market leans toward stability but leaves meaningful downside probability as rate and growth data evolve."
  - "Resolves based on defined economic-condition criteria at December 31, 2026."
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
      kalshi_vol_24h_usd: 17596.13
sources:
  - label: "ClearMarket market record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/events/kxeconpath-26"
    retrieved_at: "2026-10-21T13:25:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 31% all-time volume burst on a broad macro-state contract tells a desk that incoming economic data, GDP, jobs, or Fed signaling, is actively repricing the soft-landing probability and warrants cross-asset monitoring.
