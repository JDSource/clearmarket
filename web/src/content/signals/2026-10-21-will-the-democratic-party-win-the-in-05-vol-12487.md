---
signal_id: "CMSIG20261021VS04"
signal_slug: "will-the-democratic-party-win-the-in-05-vol-12487"
headline: "IN-05 House seat: 16% on $12K Polymarket volume"
semantic_title: "Democrats remain heavy underdogs in IN-05 House race"
telemetry: "16% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T07:48:52+00:00"
event_id: "CM-EVT-2Y2596TYD9"
event_slug: "in-05-house-election-winner"
event_question: "Will the Republican Party win the Indiana 5th Congressional District House seat in the 2026 general election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x98f22f0ec396ec65364048a14c0b30f3a4f79065ab26581a516b5fa570253d51"
  question_raw: "Will the Democratic Party win the IN-05 House seat?"
  current_price: 0.16
  volume_24h_usd: 12487.665768
  volume_cumulative_usd: 30938.520937999994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "16% prices a Democratic win as a longshot, the contract implies an 84% Republican retention probability."
  - "40% of all-time volume arriving in 24h is a meaningful concentration suggesting a specific catalyst or late polling."
  - "Fresh capital entering at 16% could reflect either speculative upside hunting or a hedged position against a surprise."
  - "Resolves on certified Indiana 5th congressional district House race outcome."
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
      poly_vol_24h_usd: 12487.665768
sources:
  - label: "ClearMarket market record: Will the Republican Party win the Indiana 5th Congressi"
    url: "https://clearmarket.fyi/events/in-05-house-election-winner"
    retrieved_at: "2026-10-21T07:48:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume concentration at a low price in a red-leaning district warrants scrutiny, if no public catalyst explains the surge, desks should check for any private polling or candidate-event news circulating before the market moves further.
