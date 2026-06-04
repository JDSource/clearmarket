---
signal_id: "CMSIG20260603VS06"
signal_slug: "israel-x-iran-permanent-peace-deal-by-ju-vol-202502"
headline: "Israel-Iran permanent peace by June 30: 19% on $202K"
semantic_title: "Traders fade an Israel-Iran peace deal by June 30"
telemetry: "19% · $203K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-03T01:46:55+00:00"
event_id: "CM-EVT-6BZBWX4DV3"
event_slug: "israel-x-iran-permanent-peace-deal-by"
event_question: "Israel x Iran permanent peace deal by May 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5efa976ebe94080bbda7e45605333ff8f30156cc91604d66c41eb52fd3e25f3e"
  question_raw: "Israel x Iran permanent peace deal by June 30, 2026?"
  current_price: 0.19
  volume_24h_usd: 202502.16006700005
  volume_cumulative_usd: 760455.0397569994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket at 19%, one-in-five odds of formal Israel-Iran peace deal by month-end."
  - "$202K in 24h is 27% of all-time volume; flows correlated with US-Iran deal contract (Spike 2)."
  - "Likely moving in tandem with broader Gulf diplomacy narrative; bilateral deal seen as harder than US track."
  - "Resolves June 30; discount to US-Iran contract reflects additional bilateral complexity."
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
      poly_vol_24h_usd: 202502.16006700005
sources:
  - label: "ClearMarket market record: Israel x Iran permanent peace deal by May 31, 2026?"
    url: "https://clearmarket.fyi/events/israel-x-iran-permanent-peace-deal-by"
    retrieved_at: "2026-06-03T01:46:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 10-point discount to the US-Iran contract price reflects market judgment that a direct Israel-Iran deal faces higher hurdles, geopolitical desks should monitor whether the gap narrows as diplomacy progresses.
