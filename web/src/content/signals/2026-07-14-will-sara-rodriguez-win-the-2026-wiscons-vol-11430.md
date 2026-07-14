---
signal_id: "CMSIG20260714VS04"
signal_slug: "will-sara-rodriguez-win-the-2026-wiscons-vol-11430"
headline: "Rodriguez WI Dem primary: 17% on $11K Polymarket surge"
semantic_title: "Rodriguez Wisconsin primary bid draws skeptical capital at 17%"
telemetry: "17% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-14T09:55:02+00:00"
event_id: "CM-EVT-CDL1PJHC16"
event_slug: "wisconsin-governor-democratic-primary-winner"
event_question: "Will a Democrat win the Wisconsin Governor Democratic Primary?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6bb7b47236aafe3cde3389214c31055abaa815b7170d9c12dcbea43b8a884925"
  question_raw: "Will Sara Rodriguez win the 2026 Wisconsin Governor Democratic primary election?"
  current_price: 0.17
  volume_24h_usd: 11430.116350999999
  volume_cumulative_usd: 41307.67458200002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-11T00:00:00Z"
bullets:
  - "17% price tags Sara Rodriguez as a clear underdog in the 2026 Wisconsin Democratic governor primary."
  - "$11,430 in 24h represents 28% of all-time volume, indicating a sharp burst of fresh market attention."
  - "Sudden attention on a low-probability candidate often precedes a news catalyst, endorsement, poll, or entry."
  - "Resolution tied to Wisconsin Democratic primary election date; field and frontrunner dynamics still fluid."
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
      poly_vol_24h_usd: 11430.116350999999
sources:
  - label: "ClearMarket market record: Will a Democrat win the Wisconsin Governor Democratic P"
    url: "https://clearmarket.fyi/events/wisconsin-governor-democratic-primary-winner"
    retrieved_at: "2026-07-14T09:55:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A volume burst on a low-priced underdog contract warrants monitoring for an imminent news catalyst, endorsement, fundraising disclosure, or a field change that could rapidly reprice Wisconsin primary odds.
