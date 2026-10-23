---
signal_id: "CMSIG20261023VS00"
signal_slug: "will-marion-mar-chal-win-the-2027-french-vol-371000"
headline: "Maréchal France 2027: 0% on $371K volume spike"
semantic_title: "Maréchal 2027 presidential odds stay at zero on a surge"
telemetry: "0% · $371K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T13:04:13+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf9f40504425133cce159883ca3eaf376a815ab1ae763086ae8e4a3f5eacea479"
  question_raw: "Will Marion Maréchal win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 371000.0
  volume_cumulative_usd: 872673.103
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Kalshi prices Maréchal at 0%, market reads her as a non-viable presidential contender for 2027."
  - "24h volume of $371K is 43% of all-time on Polymarket, a sharp burst of fresh attention on a near-zero contract."
  - "Surge likely reflects political news flow around the French right; attention precedes developments in candidate positioning."
  - "Resolves on 2027 French presidential election outcome."
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
      poly_vol_24h_usd: 371000.0
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-10-23T13:04:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume against a 0% price signals desks are actively confirming, not reconsidering, Maréchal's elimination from viable 2027 contention, possibly hedging RN scenario risk.
