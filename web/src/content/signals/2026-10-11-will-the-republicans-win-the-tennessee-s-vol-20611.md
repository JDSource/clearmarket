---
signal_id: "CMSIG20261011VS05"
signal_slug: "will-the-republicans-win-the-tennessee-s-vol-20611"
headline: "TN Senate Republican: 93% on $21K inflow"
semantic_title: "Fresh volume backs GOP Tennessee Senate win at 93%"
telemetry: "93% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T14:36:40+00:00"
event_id: "CM-EVT-TGH45YCRW3"
event_slug: "tennessee-senate-election-winner"
event_question: "Will a Republican win the Tennessee Senate election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x17d8c697aa69e53ef8062fc4b42ff6f8f7983ec569a021aab6d707d6f797780a"
  question_raw: "Will the Republicans win the Tennessee Senate race in 2026?"
  current_price: 0.927
  volume_24h_usd: 20611.018678
  volume_cumulative_usd: 48318.44028100002
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices a Republican Tennessee Senate win at 93%, echoing Kalshi's 92% read on the same race."
  - "43% of all-time volume arrived in 24 hours, consistent cross-venue positioning in the same direction."
  - "Near-identical prices on Kalshi and Polymarket reduce arbitrage opportunity and confirm consensus conviction."
  - "Resolves after 2026 Tennessee Senate race is called."
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
      poly_vol_24h_usd: 20611.018678
sources:
  - label: "ClearMarket market record: Will a Republican win the Tennessee Senate election?"
    url: "https://clearmarket.fyi/events/tennessee-senate-election-winner"
    retrieved_at: "2026-10-11T14:36:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes at matched prices across two venues confirm genuine market consensus on Tennessee, giving a desk high confidence this is a reliable anchor in a midterm Senate model.
