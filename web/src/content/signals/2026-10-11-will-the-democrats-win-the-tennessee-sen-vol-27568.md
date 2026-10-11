---
signal_id: "CMSIG20261011VS02"
signal_slug: "will-the-democrats-win-the-tennessee-sen-vol-27568"
headline: "TN Senate Dem win: 7% on $28K surge"
semantic_title: "Democrats win Tennessee Senate stays a long shot at 7%"
telemetry: "7% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T14:36:40+00:00"
event_id: "CM-EVT-TGH45YCRW3"
event_slug: "tennessee-senate-election-winner"
event_question: "Will a Republican win the Tennessee Senate election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa0af1b2ca6a3251cad3845f8172febb2182cd7a60744cc9cb685c626e595d0da"
  question_raw: "Will the Democrats win the Tennessee Senate race in 2026?"
  current_price: 0.069
  volume_24h_usd: 27568.763537
  volume_cumulative_usd: 45116.74041900001
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices a Democratic Tennessee Senate win at 7%, deep underdog territory."
  - "61% of all-time volume hit in 24 hours, the sharpest lifetime-share surge in this batch."
  - "Paired with Spike 0 and Spike 5, the activity suggests traders are cross-checking Tennessee contracts across venues."
  - "Resolves after 2026 Tennessee Senate race outcome is certified."
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
      poly_vol_24h_usd: 27568.763537
sources:
  - label: "ClearMarket market record: Will a Republican win the Tennessee Senate election?"
    url: "https://clearmarket.fyi/events/tennessee-senate-election-winner"
    retrieved_at: "2026-10-11T14:36:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 61% of lifetime volume arriving in one session, a desk should note cross-venue arbitrage activity between Kalshi and Polymarket Tennessee contracts is likely driving the flow.
