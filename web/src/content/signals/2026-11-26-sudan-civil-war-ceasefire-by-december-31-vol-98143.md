---
signal_id: "CMSIG20261126VS01"
signal_slug: "sudan-civil-war-ceasefire-by-december-31-vol-98143"
headline: "Sudan ceasefire Dec 31: 11% on $98K surge"
semantic_title: "Sudan ceasefire by Dec 31 holds at long-shot odds on heavy trading"
telemetry: "11% · $98K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-26T07:47:57+00:00"
event_id: "CM-EVT-56LRJL3JK2"
event_slug: "sudan-civil-war-ceasefire-by"
event_question: "Will there be a ceasefire in the Sudan civil war by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2343926c89946f2e3abe1511dd38a026ca9176b96d6554ec6d7ae5b1a59a6ef9"
  question_raw: "Sudan civil war ceasefire by December 31, 2026?"
  current_price: 0.11
  volume_24h_usd: 98143.56999999999
  volume_cumulative_usd: 113270.32292800001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Sudan ceasefire by year-end at 11%, firmly in long-shot territory."
  - "24h volume of $98K is 87% of all-time, suggesting a near-debut-level rush of engagement."
  - "Fresh volume into a low-probability contract signals either a catalyst rumor or diplomatic back-channel noise drawing desk attention."
  - "Contract resolves on a confirmed, announced ceasefire between warring parties by December 31, 2026."
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
      poly_vol_24h_usd: 98143.56999999999
sources:
  - label: "ClearMarket market record: Will there be a ceasefire in the Sudan civil war by 202"
    url: "https://clearmarket.fyi/events/sudan-civil-war-ceasefire-by"
    retrieved_at: "2026-11-26T07:47:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 87% single-day share of all-time volume into an 11% contract is a flag for desks tracking Sudan exposure, the market is not moving the odds, but someone believes the question is suddenly worth pricing again.
