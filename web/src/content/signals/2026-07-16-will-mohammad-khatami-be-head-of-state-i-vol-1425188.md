---
signal_id: "CMSIG20260716VS00"
signal_slug: "will-mohammad-khatami-be-head-of-state-i-vol-1425188"
headline: "Khatami Iran head of state: 0% on $1.4M surge"
semantic_title: "Capital writes off Khatami as Iran year-end head of state"
telemetry: "0% · $1.4M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-16T17:21:12+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4266ab921148974f104cbadd099e13bca989441bf58acfd2a08fc6cc7440e1a1"
  question_raw: "Will Mohammad Khatami be head of state in Iran end of 2026?"
  current_price: 0.001
  volume_24h_usd: 1425188.0009999983
  volume_cumulative_usd: 4996243.960269007
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices zero probability Khatami holds or gains head-of-state status by end of 2026."
  - "29% of all-time volume, $1.4M, flooded in over 24 hours, marking an extraordinary single-session conviction burst."
  - "Surge likely triggered by a definitive political development in Tehran cementing Khatami's exclusion from power."
  - "Contract resolves end of 2026; at 0% the crowd treats this as settled fact, not live risk."
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
      poly_vol_24h_usd: 1425188.0009999983
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-16T17:21:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 29%-of-all-time volume print at zero price signals desks treating an Iranian leadership question as conclusively resolved, warranting rapid reassessment of any Iran political-transition exposure.
