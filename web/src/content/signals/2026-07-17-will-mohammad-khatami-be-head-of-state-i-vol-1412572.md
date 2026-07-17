---
signal_id: "CMSIG20260717VS00"
signal_slug: "will-mohammad-khatami-be-head-of-state-i-vol-1412572"
headline: "Khatami Iran head of state: 0% on $1.4M surge"
semantic_title: "Capital writes off Khatami as Iran head of state by year-end"
telemetry: "0% · $1.4M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-17T09:53:28+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4266ab921148974f104cbadd099e13bca989441bf58acfd2a08fc6cc7440e1a1"
  question_raw: "Will Mohammad Khatami be head of state in Iran end of 2026?"
  current_price: 0.001
  volume_24h_usd: 1412572.1149999981
  volume_cumulative_usd: 5000419.275269006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Khatami at 0%, market treats outcome as resolved impossibility."
  - "24h volume of $1.4M is 28% of all-time $5M, signaling a decisive, concentrated flush."
  - "Fresh attention likely driven by Iran leadership news cycle; flows confirm no credible path."
  - "Contract resolves end-2026; zero price leaves no residual risk premium to fade."
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
      poly_vol_24h_usd: 1412572.1149999981
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-17T09:53:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume surge at a zero price indicates desks are closing positions or arbitraging residual liquidity out of the contract, treating any Khatami leadership scenario in Iran by year-end as fully extinguished.
