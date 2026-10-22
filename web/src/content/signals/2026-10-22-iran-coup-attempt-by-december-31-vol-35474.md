---
signal_id: "CMSIG20261022VS03"
signal_slug: "iran-coup-attempt-by-december-31-vol-35474"
headline: "Iran coup attempt by Dec 31: 12% on $35K surge"
semantic_title: "Betting picks up on an Iran coup attempt, odds stay at 12%"
telemetry: "12% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T07:48:28+00:00"
event_id: "CM-EVT-RD45F72C85"
event_slug: "iran-coup-attempt-by-june-30"
event_question: "Will there be a coup attempt in Iran by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x13faa876e0bc41ff44bd250ed3745bd62d33763e727f2193d3dfb5e789008fce"
  question_raw: "Iran coup attempt by December 31?"
  current_price: 0.12
  volume_24h_usd: 35474.111112
  volume_cumulative_usd: 140653.690888
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices an Iran coup attempt by December 31 at 12%, low probability but elevated for a regime-change event."
  - "25% of all-time volume cleared in 24h, hitting the all-time quarterly pace threshold in a single session."
  - "Coup-contract volume spikes often cluster around protest escalation, elite defection rumors, or cross-border pressure."
  - "Resolves December 31, 2026 on a defined coup attempt against the Iranian government."
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
      poly_vol_24h_usd: 35474.111112
sources:
  - label: "ClearMarket market record: Will there be a coup attempt in Iran by the end of 2026"
    url: "https://clearmarket.fyi/events/iran-coup-attempt-by-june-30"
    retrieved_at: "2026-10-22T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 25%-of-lifetime volume day on an Iran coup contract tells a desk that geopolitical desks are stress-testing regime-stability scenarios, likely in tandem with the concurrent IAEA and nuclear-deal flow.
