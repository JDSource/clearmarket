---
signal_id: "CMSIG20260630VS04"
signal_slug: "tesla-and-spacex-merger-officially-annou-vol-76061"
headline: "Tesla-SpaceX merger by Sept 30: 11% on $76K inflow"
semantic_title: "Traders stack modest conviction on a Tesla-SpaceX merger announcement"
telemetry: "11% · $76K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-30T10:55:12+00:00"
event_id: "CM-EVT-2CLPLTTYR2"
event_slug: "tesla-and-spacex-merger-officially-announced-by-june-30"
event_question: "Tesla and SpaceX merger officially announced in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9e7056c4004056441b57f960460c5e4f6d3e6ab9e1633b15538eb909d0f34466"
  question_raw: "Tesla and SpaceX merger officially announced by September 30?"
  current_price: 0.11
  volume_24h_usd: 76061.227604
  volume_cumulative_usd: 120368.98667700005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket at 11%, a low but non-trivial probability with three months remaining."
  - "24h volume $76K is 63% of all-time, suggesting the contract is newly in focus."
  - "Renewed attention may follow Musk corporate restructuring commentary or board signaling."
  - "Resolution deadline is September 30; elevated fresh-volume share flags institutional curiosity."
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
      poly_vol_24h_usd: 76061.227604
sources:
  - label: "ClearMarket market record: Tesla and SpaceX merger officially announced in 2026? ("
    url: "https://clearmarket.fyi/events/tesla-and-spacex-merger-officially-announced-by-june-30"
    retrieved_at: "2026-06-30T10:55:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 63% all-time volume share in one session on a low-liquidity corporate event contract tells a desk that fresh attention is flooding a thin book, worth monitoring for an underlying news catalyst.
