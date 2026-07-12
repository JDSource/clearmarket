---
signal_id: "CMSIG20260712VS00"
signal_slug: "will-ali-motahari-be-head-of-state-in-ir-vol-571110"
headline: "Motahari Iran head of state: 0% on $571K surge"
semantic_title: "Motahari head-of-state bid written off by Iran watchers"
telemetry: "0% · $571K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-12T09:48:30+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x73d9b98f619d738cca001cfde25654d409a132f0eb565ae98972b62b123a4da0"
  question_raw: "Will Ali Motahari be head of state in Iran end of 2026?"
  current_price: 0.002
  volume_24h_usd: 571110.0699999993
  volume_cumulative_usd: 801561.4346059988
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Motahari at 0%, market treats his path to Iran's top post as closed by year-end."
  - "24h volume of $571K is 71% of all-time handle, signaling decisive late-stage capital settlement."
  - "Surge likely driven by post-succession clarity as Iran's political landscape consolidates around other figures."
  - "Resolves end of 2026; fresh flows confirm the zero, not challenge it."
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
      poly_vol_24h_usd: 571110.0699999993
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-12T09:48:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The concentrated volume at zero suggests a desk-level consensus trade closing out residual long exposure on Motahari amid Iran succession resolution.
