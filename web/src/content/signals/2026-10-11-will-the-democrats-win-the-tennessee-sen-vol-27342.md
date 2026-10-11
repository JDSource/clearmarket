---
signal_id: "CMSIG20261011VS02"
signal_slug: "will-the-democrats-win-the-tennessee-sen-vol-27342"
headline: "TN Senate Dems: 5% on $27K volume spike"
semantic_title: "Democratic Tennessee Senate odds stay near zero"
telemetry: "5% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T07:48:50+00:00"
event_id: "CM-EVT-TGH45YCRW3"
event_slug: "tennessee-senate-election-winner"
event_question: "Will a Republican win the Tennessee Senate election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa0af1b2ca6a3251cad3845f8172febb2182cd7a60744cc9cb685c626e595d0da"
  question_raw: "Will the Democrats win the Tennessee Senate race in 2026?"
  current_price: 0.05
  volume_24h_usd: 27342.79384
  volume_cumulative_usd: 44740.770722000016
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket marks Democrats at 5% in Tennessee, effectively a long-shot price with little disagreement."
  - "61% of all-time contract volume hit in a single 24h window, the sharpest relative surge in this batch."
  - "Concentrated volume on a near-zero price may reflect arbitrage activity or contested positioning against the Kalshi mirror contract."
  - "Resolves on 2026 midterm election results."
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
      poly_vol_24h_usd: 27342.79384
sources:
  - label: "ClearMarket market record: Will a Republican win the Tennessee Senate election?"
    url: "https://clearmarket.fyi/events/tennessee-senate-election-winner"
    retrieved_at: "2026-10-11T07:48:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 61% all-time volume share in one day on a 5% contract is a cross-venue arbitrage flag, the desk should check spread against the Kalshi Tennessee GOP contract.
