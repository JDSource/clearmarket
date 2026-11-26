---
signal_id: "CMSIG20261126VS00"
signal_slug: "will-miguel-tellado-be-the-next-prime-mi-vol-139553"
headline: "Tellado Spain PM: 0% on $139K inflow"
semantic_title: "Tellado Spain PM odds stay at zero through volume surge"
telemetry: "0% · $140K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-26T07:47:57+00:00"
event_id: "CM-EVT-D9KHM803Y2"
event_slug: "next-prime-minister-of-spain-20260625005215443"
event_question: "Who will be the next Prime Minister of Spain?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd3b68cd44f465f6c4090950f247368148292a6cedea926032c846f952015a4b9"
  question_raw: "Will Miguel Tellado be the next Prime Minister of Spain?"
  current_price: 0.001
  volume_24h_usd: 139553.85
  volume_cumulative_usd: 173599.72600000002
  arbitration_model: "uma_oracle"
  resolves_at: "2028-03-31T23:59:00Z"
bullets:
  - "Polymarket prices Tellado at 0%, a near-total rejection of his path to PM."
  - "24h volume of $139K is 80% of all-time, signaling a sharp burst of fresh attention."
  - "Volume without price movement implies the market is re-testing a verdict, not revising it."
  - "Contract resolves on confirmation of a next Spanish Prime Minister."
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
      poly_vol_24h_usd: 139553.85
sources:
  - label: "ClearMarket market record: Who will be the next Prime Minister of Spain?"
    url: "https://clearmarket.fyi/events/next-prime-minister-of-spain-20260625005215443"
    retrieved_at: "2026-11-26T07:47:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as a crowd-sourced reaffirmation: despite a surge of fresh capital engaging the question, consensus finds no viable route for Tellado to the premiership under current political conditions.
