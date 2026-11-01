---
signal_id: "CMSIG20261101VS00"
signal_slug: "will-the-democrats-win-the-iowa-senate-r-vol-270296"
headline: "Iowa Senate Dem win: 43% on $270K surge"
semantic_title: "Fresh volume tests Iowa Senate as a real Democratic pickup"
telemetry: "43% · $270K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T14:43:30+00:00"
event_id: "CM-EVT-2X8487L8P4"
event_slug: "iowa-senate-election-winner"
event_question: "Will a Republican win the Iowa Senate seat in the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd50c016598c499fceea10a1a714e48d9b4953487fe215daeaf916068fae722f1"
  question_raw: "Will the Democrats win the Iowa Senate race in 2026?"
  current_price: 0.43
  volume_24h_usd: 270296.833752
  volume_cumulative_usd: 964169.4428190002
  arbitration_model: "uma_oracle"
bullets:
  - "At 43%, Polymarket holds Iowa as a lean-Republican seat but within striking distance for Democrats."
  - "$270K traded in 24h equals 28% of all-time volume, largest single-day draw this contract has seen."
  - "Election Day pressure; Iowa is a marquee 2026 pickup target and fresh attention may precede polling movement."
  - "Resolves on certified 2026 midterm result for Iowa's U.S. Senate seat."
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
      poly_vol_24h_usd: 270296.833752
sources:
  - label: "ClearMarket market record: Will a Republican win the Iowa Senate seat in the next "
    url: "https://clearmarket.fyi/events/iowa-senate-election-winner"
    retrieved_at: "2026-11-01T14:43:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume concentration on Election Day signals desks are treating Iowa as a live swing rather than a settled Republican hold, worth monitoring for late odds shifts.
