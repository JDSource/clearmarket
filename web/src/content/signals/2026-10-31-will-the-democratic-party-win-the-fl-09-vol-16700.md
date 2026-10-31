---
signal_id: "CMSIG20261031VS07"
signal_slug: "will-the-democratic-party-win-the-fl-09-vol-16700"
headline: "FL-09 Dem seat (PM): 40% on 59% all-time share"
semantic_title: "Fresh volume returns to FL-09 Democratic odds at 40%"
telemetry: "40% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T07:49:19+00:00"
event_id: "CM-EVT-3ZLX48RMQ5"
event_slug: "fl-09-house-election-winner"
event_question: "Will the winner of the FL-09 House election be determined by November 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd0f009dd6d9c8b46db418c5b44af2566cdb7de8274685ca4f8dea3231b75900f"
  question_raw: "Will the Democratic Party win the FL-09 House seat?"
  current_price: 0.4
  volume_24h_usd: 16700.647455000002
  volume_cumulative_usd: 28454.683029000003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices FL-09 Democratic win at 40%, closely mirroring Kalshi's 38%, confirming cross-venue consensus."
  - "59% of all-time Polymarket volume on this contract landed in 24h, the sharpest single-day concentration of the two FL-09 venues."
  - "Tight spread between Polymarket (40%) and Kalshi (38%) leaves minimal arbitrage; both point to a Republican-leaning district."
  - "Resolves on FL-09 2026 House election result."
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
      poly_vol_24h_usd: 16700.647455000002
sources:
  - label: "ClearMarket market record: Will the winner of the FL-09 House election be determin"
    url: "https://clearmarket.fyi/events/fl-09-house-election-winner"
    retrieved_at: "2026-10-31T07:49:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Cross-venue price convergence at 38, 40% with majority all-time volume printing today confirms FL-09 is a live contested race, the near-zero arbitrage gap signals well-informed capital on both platforms.
