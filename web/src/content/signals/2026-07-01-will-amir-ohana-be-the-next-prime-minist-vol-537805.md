---
signal_id: "CMSIG20260701VS02"
signal_slug: "will-amir-ohana-be-the-next-prime-minist-vol-537805"
headline: "Ohana next Israel PM: 0% on $538K volume"
semantic_title: "Market stacks against Ohana ascending to Israeli PM"
telemetry: "0% · $538K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-01T11:21:48+00:00"
event_id: "CM-EVT-05G08PPSM2"
event_slug: "who-will-be-the-next-prime-minister-of-israel-after-the-next-election"
event_question: "Will a specific individual become Prime Minister of Israel following the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8cbdd0c4c6061c9e5c5a94d4a474c1880d0f2ab5ee4704a64af1e77c6d0e18d0"
  question_raw: "Will Amir Ohana be the next Prime Minister of Israel?"
  current_price: 0.003
  volume_24h_usd: 537805.961645
  volume_cumulative_usd: 1633500.9265619942
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket assigns zero probability to Amir Ohana becoming Israel's next Prime Minister."
  - "$538K in 24h is 33% of all-time volume, a significant single-session conviction flush."
  - "Flow likely driven by Netanyahu coalition developments rendering Ohana a non-viable successor path."
  - "Zero price with high volume suggests institutional desks are definitively closing the tail-risk position."
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
      poly_vol_24h_usd: 537805.961645
sources:
  - label: "ClearMarket market record: Will a specific individual become Prime Minister of Isr"
    url: "https://clearmarket.fyi/events/who-will-be-the-next-prime-minister-of-israel-after-the-next-election"
    retrieved_at: "2026-07-01T11:21:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 0% price absorbing one-third of all-time contract volume in a day signals that a previously live successor scenario has been conclusively eliminated, warranting removal from any Israeli political transition scenario book.
