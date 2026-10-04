---
signal_id: "CMSIG20261004VS06"
signal_slug: "will-fl-vio-bolsonaro-win-the-first-roun-vol-42788"
headline: "Flávio Bolsonaro 1st round win: 35% on $43K"
semantic_title: "Flávio Bolsonaro first-round win at 35%"
telemetry: "35% · $43K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T07:48:35+00:00"
event_id: "CM-EVT-2NF81BZ4K5"
event_slug: "brazil-presidential-election-first-round-margin-of-victory"
event_question: "Will the margin of victory in Brazil's presidential election first round be less than 5 percentage points?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x25966b196ffc1682fc77df0298784831a60aea8abe03b9aa4fc219d1422feb9f"
  question_raw: "Will Flávio Bolsonaro win the first round of the 2026 Brazilian presidential election by less than 5%?"
  current_price: 0.35
  volume_24h_usd: 42788.191628
  volume_cumulative_usd: 137092.59627099996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices Flávio Bolsonaro winning the first round outright at 35%, possible but not expected."
  - "31% of all-time volume cleared in 24h, reflecting active repricing of the outright win scenario."
  - "Outright win requires clearing 50% in round one; the market views a runoff as far more likely."
  - "Resolves on Brazil's 2026 first-round result."
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
      poly_vol_24h_usd: 42788.191628
sources:
  - label: "ClearMarket market record: Will the margin of victory in Brazil's presidential ele"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-margin-of-victory"
    retrieved_at: "2026-10-04T07:48:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 35% first-round win price alongside near-certainty on runoff qualification tells a desk the market's base case is a Bolsonaro-Lula runoff, fresh volume here likely reflects traders calibrating across multiple Brazil contracts.
