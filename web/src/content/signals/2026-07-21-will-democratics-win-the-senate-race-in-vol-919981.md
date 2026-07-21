---
signal_id: "CMSIG20260721VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-919981"
headline: "NC Senate Dem win: 91% on $920K surge"
semantic_title: "Democrats defended as heavy NC Senate capital locks in"
telemetry: "91% · $920K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-21T10:22:52+00:00"
event_id: "CM-EVT-KX1QWP5LQ1"
event_slug: "senatenc-26"
event_question: "North Carolina Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATENC-26-D"
  question_raw: "Will Democratics win the Senate race in North Carolina?"
  current_price: 0.909
  volume_24h_usd: 919981.01
  volume_cumulative_usd: 1067713.06
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "91% implies near-certainty of a Democratic Senate pickup in North Carolina."
  - "Kalshi logs $920K in 24h, 86% of the contract's entire all-time volume."
  - "Extraordinary single-session concentration signals a terminal positioning event, not speculative probing."
  - "Contract resolves on North Carolina Senate race outcome."
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
      kalshi_vol_24h_usd: 919981.01
sources:
  - label: "ClearMarket market record: North Carolina Senate winner?"
    url: "https://clearmarket.fyi/events/senatenc-26"
    retrieved_at: "2026-07-21T10:22:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a near-closed-book position: late smart money piling onto a consensus outcome, with residual 9% offering asymmetric value if any late-breaking development disrupts the Democratic lock.
