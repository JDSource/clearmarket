---
signal_id: "CMSIG20260627VS04"
signal_slug: "will-silver-si-settle-over-120-on-the-vol-25166"
headline: "Silver >$120 June final day: 0% on $25K"
semantic_title: "Silver $120 June expiry stacked firmly in the 'No' column"
telemetry: "0% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T01:36:27+00:00"
event_id: "CM-EVT-W6PTXB1828"
event_slug: "si-over-under-jun-2026"
event_question: "Will silver (SI) be above ___ by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe381e4050ad2c5c356b28ec5ba7fafae427dce1e37e56040689e0482d2de0556"
  question_raw: "Will Silver (SI) settle over $120 on the final trading day of June 2026?"
  current_price: 0.001
  volume_24h_usd: 25166.699999999997
  volume_cumulative_usd: 41123.094378000016
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T17:30:00Z"
bullets:
  - "Market prices zero probability of SI settling above $120 on the final June trading day."
  - "$25K in 24h equals 61% of the contract's all-time volume, dominant late-session activity."
  - "Silver spot is far below $120; the threshold is treated as an unreachable tail scenario."
  - "Resolves on the final June trading day, current flow is settlement, not a trend signal."
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
      poly_vol_24h_usd: 25166.699999999997
sources:
  - label: "ClearMarket market record: Will silver (SI) be above ___ by the end of June?"
    url: "https://clearmarket.fyi/events/si-over-under-jun-2026"
    retrieved_at: "2026-06-27T01:36:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Outsized share of lifetime volume in a single day confirms this is expiry-driven position close-out; silver desks should treat the $120 level as a purely notional reference for this cycle.
