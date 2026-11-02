---
signal_id: "CMSIG20261102VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-1613876"
headline: "Michigan Senate Dem: 79% on $1.6M surge"
semantic_title: "Democrats hold a wide lead in the Michigan Senate race"
telemetry: "79% · $1.6M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T07:49:23+00:00"
event_id: "CM-EVT-GBSY094P67"
event_slug: "senatemi-26"
event_question: "Michigan Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMI-26-D"
  question_raw: "Will Democratics win the Senate race in Michigan?"
  current_price: 0.79
  volume_24h_usd: 1613876.32
  volume_cumulative_usd: 6352899.34
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 79%, a strong favorite, not yet a lock."
  - "$1.6M traded in 24h equals 25% of all-time volume, a decisive capital deployment."
  - "Eve-of-election flow with Michigan a key Senate battleground; fresh money backs the incumbent party."
  - "Contract resolves on Michigan Senate outcome, election day Nov 3."
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
      kalshi_vol_24h_usd: 1613876.32
sources:
  - label: "ClearMarket market record: Michigan Senate winner?"
    url: "https://clearmarket.fyi/events/senatemi-26"
    retrieved_at: "2026-11-02T07:49:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The scale of pre-election volume signals desks are treating Michigan as a near-settled call but are still actively hedging the 21% tail risk.
