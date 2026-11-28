---
signal_id: "CMSIG20261128VS01"
signal_slug: "will-the-us-federal-government-take-a-st-vol-27867"
headline: "US govt NVIDIA stake: 26% on $28K surge"
semantic_title: "US government NVIDIA stake holds at 25% on a volume push"
telemetry: "26% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-28T07:48:37+00:00"
event_id: "CM-EVT-BDVS6ZB873"
event_slug: "which-companies-will-the-us-take-a-stake-in"
event_question: "Which companies will the US take a stake in by 2026-12-31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf86df821bd41f20c0b67674bfc03a7db9408bc336103ffdf9675cb8e313797f1"
  question_raw: "Will the US federal government take a stake in NVIDIA Corporation?"
  current_price: 0.257
  volume_24h_usd: 27867.805673
  volume_cumulative_usd: 75278.988423
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a federal equity stake in NVIDIA at 26%, just above the quarter-odds threshold, keeping the scenario live."
  - "24h volume of $28K is 37% of all-time, a concentrated burst suggesting this is not routine churn."
  - "Fresh attention likely tied to AI policy debate, export-control escalation, or strategic-asset rhetoric out of Washington."
  - "Contract resolves on a confirmed US government equity position in NVIDIA Corporation."
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
      poly_vol_24h_usd: 27867.805673
sources:
  - label: "ClearMarket market record: Which companies will the US take a stake in by 2026-12-"
    url: "https://clearmarket.fyi/events/which-companies-will-the-us-take-a-stake-in"
    retrieved_at: "2026-11-28T07:48:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume clustering at 37% of all-time on a 26% price signals desks are actively re-pricing regulatory tail risk around NVIDIA, any AI industrial-policy announcement or nationalization-adjacent language from the administration should be monitored closely.
