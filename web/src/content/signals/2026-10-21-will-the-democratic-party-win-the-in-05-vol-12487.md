---
signal_id: "CMSIG20261021VS06"
signal_slug: "will-the-democratic-party-win-the-in-05-vol-12487"
headline: "Dem wins IN-05 House: 16% on $12K spike"
semantic_title: "Democrats face long odds winning Indiana's IN-05 House seat"
telemetry: "16% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T13:25:08+00:00"
event_id: "CM-EVT-2Y2596TYD9"
event_slug: "in-05-house-election-winner"
event_question: "Will the Republican Party win the Indiana 5th Congressional District House seat in the 2026 general election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x98f22f0ec396ec65364048a14c0b30f3a4f79065ab26581a516b5fa570253d51"
  question_raw: "Will the Democratic Party win the IN-05 House seat?"
  current_price: 0.16
  volume_24h_usd: 12487.665767999999
  volume_cumulative_usd: 30938.520938
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democratic chances in Indiana's 5th at just 16%, the seat is treated as a heavy Republican hold."
  - "40% of all-time volume, $12K, hit in 24 hours, a sharp concentration for a low-odds contract."
  - "Fresh volume into a 16% longshot often precedes a news event that traders think could shift the competitive landscape."
  - "Resolves on certified 2026 midterm results for Indiana's 5th congressional district."
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
      poly_vol_24h_usd: 12487.665767999999
sources:
  - label: "ClearMarket market record: Will the Republican Party win the Indiana 5th Congressi"
    url: "https://clearmarket.fyi/events/in-05-house-election-winner"
    retrieved_at: "2026-10-21T13:25:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy all-time volume share on a 16% contract is a classic news-anticipation signal, a desk should watch for candidate controversy, a polling outlier, or district-level demographic news that could be moving the longshot price.
