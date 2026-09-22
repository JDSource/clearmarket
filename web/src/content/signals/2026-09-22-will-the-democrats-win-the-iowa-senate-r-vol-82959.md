---
signal_id: "CMSIG20260922VS01"
signal_slug: "will-the-democrats-win-the-iowa-senate-r-vol-82959"
headline: "Democrats Iowa Senate: 48% on $83K one-day volume"
semantic_title: "Iowa Senate odds slip below 50% as fresh volume hits"
telemetry: "48% · $83K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T13:04:04+00:00"
event_id: "CM-EVT-2X8487L8P4"
event_slug: "iowa-senate-election-winner"
event_question: "Will a Republican win the Iowa Senate seat in the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd50c016598c499fceea10a1a714e48d9b4953487fe215daeaf916068fae722f1"
  question_raw: "Will the Democrats win the Iowa Senate race in 2026?"
  current_price: 0.48
  volume_24h_usd: 82959.59605299997
  volume_cumulative_usd: 276943.64872600004
  arbitration_model: "uma_oracle"
bullets:
  - "At 48%, Polymarket has the Democratic candidate as a marginal underdog for Iowa's 2026 Senate seat."
  - "24h volume of $83K equals 30% of all-time, a meaningful capital inflow into an unresolved race."
  - "A sub-50% read on a Senate seat in a state Republicans have held suggests fresh money is betting on the lean."
  - "Resolves on 2026 general election certification."
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
      poly_vol_24h_usd: 82959.59605299997
sources:
  - label: "ClearMarket market record: Will a Republican win the Iowa Senate seat in the next "
    url: "https://clearmarket.fyi/events/iowa-senate-election-winner"
    retrieved_at: "2026-09-22T13:04:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 48% price drawing 30% of all-time volume in a single session tells a desk this race has moved onto the competitive-seat watchlist and warrants tracking alongside broader Senate control scenarios.
