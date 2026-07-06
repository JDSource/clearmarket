---
signal_id: "CMSIG20260706VS01"
signal_slug: "will-seyed-hossein-mousavian-be-head-of-vol-200333"
headline: "Mousavian Iran head of state EOY: 0% on $200K"
semantic_title: "Mousavian head-of-state odds sit at zero amid Iran succession flows"
telemetry: "0% · $200K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-06T12:00:42+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x821f357da390a32347e4df0c3fb0aa4a8eadf4af72730c8dc7a7f1ab58798a02"
  question_raw: "Will Seyed Hossein Mousavian be head of state in Iran end of 2026?"
  current_price: 0.002
  volume_24h_usd: 200333.95
  volume_cumulative_usd: 388435.96538199997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket assigns zero probability to Mousavian leading Iran by end of 2026, a near-impossibility verdict."
  - "$200K in 24h represents 52% of all-time volume, flagging a sharp burst of fresh attention on Iran leadership contracts."
  - "Simultaneous volume across multiple Iran succession contracts suggests coordinated positioning around a shared macro catalyst."
  - "Contract resolves on Mousavian holding head-of-state title on December 31, 2026."
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
      poly_vol_24h_usd: 200333.95
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-06T12:00:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 52% all-time volume in a single session, concurrent with parallel Iran leadership spikes, signals that a desk is stress-testing the full slate of Iranian succession candidates against a specific news catalyst, the zero price reflects no credible path for Mousavian.
