---
signal_id: "CMSIG20261107VS01"
signal_slug: "will-national-party-win-the-most-seats-i-vol-285804"
headline: "NZ National most seats: 99% on $286K volume"
semantic_title: "Traders pile into National Party winning NZ seats at 99%"
telemetry: "99% · $286K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T14:39:51+00:00"
event_id: "CM-EVT-DB92W53ZH3"
event_slug: "new-zealand-legislative-election-winner"
event_question: "Will the New Zealand Labour Party win the most seats in the next legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xba155b6be6cabf93bf31dfcc56fe2f4e3e88d16b0d490319c635930f2d9fbd04"
  question_raw: "Will National Party win the most seats in the New Zealand House of Representatives in the 2026 New Zealand legislative election?"
  current_price: 0.988
  volume_24h_usd: 285804.546751
  volume_cumulative_usd: 389042.07704700006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-07T00:00:00Z"
bullets:
  - "Polymarket prices National Party winning the most House seats at 99%, effectively a settled outcome."
  - "$286K in 24h represents 73% of all-time contract volume, flagging a sharp burst of late attention."
  - "Fresh volume into an already-consensus market suggests either arbitrage closing or hedging against the 1% tail."
  - "Contract resolves on official NZ election seat count."
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
      poly_vol_24h_usd: 285804.546751
sources:
  - label: "ClearMarket market record: Will the New Zealand Labour Party win the most seats in"
    url: "https://clearmarket.fyi/events/new-zealand-legislative-election-winner"
    retrieved_at: "2026-11-07T14:39:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The spike into a 99% contract points to late-stage liquidity cleanup or tail-risk hedging; a desk should note the complementary Labour contract (Spike 2) trading simultaneously as the two-sided read.
