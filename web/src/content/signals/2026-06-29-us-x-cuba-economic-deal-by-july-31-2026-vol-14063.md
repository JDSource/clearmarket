---
signal_id: "CMSIG20260629VS07"
signal_slug: "us-x-cuba-economic-deal-by-july-31-2026-vol-14063"
headline: "US-Cuba deal by Jul 31: 10% on $14K inflow"
semantic_title: "US-Cuba economic deal sits in deep skepticism territory"
telemetry: "10% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T01:47:13+00:00"
event_id: "CM-EVT-Y5QG71JGD0"
event_slug: "us-x-cuba-economic-deal-by"
event_question: "US x Cuba economic deal in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x789d388bafe08b6c17fefb96ec7ebadc6e997e0883eae5e4918354218e6dd52d"
  question_raw: "US x Cuba economic deal by July 31, 2026?"
  current_price: 0.1
  volume_24h_usd: 14063.861817
  volume_cumulative_usd: 38935.97322699993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "Polymarket prices 10%, market treats a bilateral economic agreement by July 31 as a low-probability tail."
  - "$14K in 24h is 36% of all-time volume; fresh attention likely driven by diplomatic back-channel speculation."
  - "Structural barriers, sanctions law, Congressional opposition, anchor the market firmly toward no-deal."
  - "Resolves July 31, 2026, a month of runway, but 10% implies capital sees no credible near-term pathway."
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
      poly_vol_24h_usd: 14063.861817
sources:
  - label: "ClearMarket market record: US x Cuba economic deal in 2026? (multi-deadline series"
    url: "https://clearmarket.fyi/events/us-x-cuba-economic-deal-by"
    retrieved_at: "2026-06-29T01:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A macro desk should read this as attention-driven flow on diplomatic noise rather than informed deal probability; 10% with 36% lifetime volume in one session suggests headline arbitrageurs rather than policy-informed positioning.
