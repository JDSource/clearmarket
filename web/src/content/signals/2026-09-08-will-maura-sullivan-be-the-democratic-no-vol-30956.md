---
signal_id: "CMSIG20260908VS01"
signal_slug: "will-maura-sullivan-be-the-democratic-no-vol-30956"
headline: "Sullivan NH-01 Dem primary: 83% on $31K volume"
semantic_title: "Traders pile into Sullivan as the NH-01 Dem primary front-runner"
telemetry: "83% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-08T12:34:41+00:00"
event_id: "CM-EVT-BHSCBSRT91"
event_slug: "nh-01-democratic-primary-winner"
event_question: "Will a Democrat win the NH-01 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8e0c12663aac3ff057b2b3954864e2370ec1a9c94992104996f79f7da097cda1"
  question_raw: "Will Maura Sullivan be the Democratic nominee for NH-01?"
  current_price: 0.83
  volume_24h_usd: 30956.510423
  volume_cumulative_usd: 99069.001719
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "Polymarket prices Sullivan at 83%, a strong but not locked-in lead with real tail risk remaining."
  - "$31K in 24h represents 31% of all-time volume, confirming a sharp burst of fresh attention."
  - "Elevated volume alongside an 83% price suggests late money is backing the front-runner ahead of a catalyst, likely a poll, endorsement, or filing deadline."
  - "Contract resolves on the Democratic primary winner for New Hampshire's 1st Congressional District."
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
      poly_vol_24h_usd: 30956.510423
sources:
  - label: "ClearMarket market record: Will a Democrat win the NH-01 primary election?"
    url: "https://clearmarket.fyi/events/nh-01-democratic-primary-winner"
    retrieved_at: "2026-09-08T12:34:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as event-driven positioning ahead of a near-term NH-01 primary catalyst, the 83% handle still offers enough uncertainty to attract both sides of the trade.
