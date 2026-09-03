---
signal_id: "CMSIG20260903VS07"
signal_slug: "will-christine-fr-chette-be-the-next-pre-vol-12033"
headline: "Fréchette Quebec Premier: 32% on $12K surge"
semantic_title: "Fréchette Quebec premier odds sit at 32% on fresh bets"
telemetry: "32% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-03T12:31:50+00:00"
event_id: "CM-EVT-X4XRMN8RJ9"
event_slug: "next-premier-of-quebec-594"
event_question: "Will a new Premier of Quebec be elected by the next Quebec general election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa43974113a83acd2f2477e9561bc4a18baac2a3ff6afb087cd2e5662e19f9231"
  question_raw: "Will Christine Fréchette be the next Premier of Quebec following the 2026 Quebec general election?"
  current_price: 0.319
  volume_24h_usd: 12033.428537
  volume_cumulative_usd: 42464.906803
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-05T00:00:00Z"
bullets:
  - "Polymarket prices Fréchette at 32%, market assigns her roughly one-in-three odds of becoming Quebec's next premier."
  - "24h volume of $12K is 28% of all-time flow, a moderate but notable single-session pickup."
  - "Quebec provincial polling or party developments ahead of the 2026 election appear to be drawing capital."
  - "Resolves on the premier following the 2026 Quebec provincial election."
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
      poly_vol_24h_usd: 12033.428537
sources:
  - label: "ClearMarket market record: Will a new Premier of Quebec be elected by the next Que"
    url: "https://clearmarket.fyi/events/next-premier-of-quebec-594"
    retrieved_at: "2026-09-03T12:31:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume at one-in-three odds on a provincial leadership contract suggests new polling or a party-internal development has shifted the calculus, worth monitoring for Quebec political risk exposure.
