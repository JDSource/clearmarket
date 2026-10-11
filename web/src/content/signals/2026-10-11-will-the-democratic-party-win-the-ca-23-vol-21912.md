---
signal_id: "CMSIG20261011VS07"
signal_slug: "will-the-democratic-party-win-the-ca-23-vol-21912"
headline: "CA-23 Dem House win: 3% on $22K surge"
semantic_title: "Democrats win CA-23 House seat priced at a long shot, 3%"
telemetry: "3% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T14:36:40+00:00"
event_id: "CM-EVT-X824QSSRY4"
event_slug: "ca-23-house-election-winner"
event_question: "Who will win the California 23rd congressional district House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc9e72c14f5ca7fceddcb619aefdd779bd54960acb6b416c426dc11b99c206565"
  question_raw: "Will the Democratic Party win the CA-23 House seat?"
  current_price: 0.029
  volume_24h_usd: 21912.487740000004
  volume_cumulative_usd: 55159.03322699999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic win in CA-23 at 3%, an extreme underdog line in a Republican-leaning district."
  - "40% of all-time volume arrived in 24 hours, bringing fresh attention to an otherwise quiet House contract."
  - "Volume into a 3% line suggests traders may be using it as a cheap tail-risk hedge on House composition models."
  - "Resolves after CA-23 2026 House race results are certified."
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
      poly_vol_24h_usd: 21912.487740000004
sources:
  - label: "ClearMarket market record: Who will win the California 23rd congressional district"
    url: "https://clearmarket.fyi/events/ca-23-house-election-winner"
    retrieved_at: "2026-10-11T14:36:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Significant volume at 3% on a House seat implies a desk is treating CA-23 as a low-cost option on an unlikely Democratic pick-up, relevant to modelling Republican House margin scenarios.
