---
signal_id: "CMSIG20260921VS02"
signal_slug: "will-the-democrats-win-the-kansas-senate-vol-26009"
headline: "Kansas Senate Dem win: 26% on $26K surge"
semantic_title: "Democrats bet on Kansas Senate stays alive below 25% threshold"
telemetry: "26% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T14:47:42+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x460d3942d385cdeda20519c0c5ad804ae48dc18efc9a82e1f1be87a29e69adb3"
  question_raw: "Will the Democrats win the Kansas Senate race in 2026?"
  current_price: 0.26
  volume_24h_usd: 26009.140624
  volume_cumulative_usd: 90830.69244099999
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 26% in Kansas, just above the 25% mark, a long shot but not negligible."
  - "24h volume of $26K is 29% of all-time, reflecting a sharp pickup in a contract that had been quiet."
  - "Kansas rarely sees competitive Senate races; fresh volume near the 25% threshold implies a catalyst, candidate news or polling, is drawing scrutiny."
  - "Resolves on the outcome of the 2026 Kansas U.S. Senate election."
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
      poly_vol_24h_usd: 26009.140624
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-21T14:47:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume surging to nearly 30% of all-time in a single session for a Kansas Democratic longshot tells desks that a catalyst may be imminent and the contract is being actively re-priced.
