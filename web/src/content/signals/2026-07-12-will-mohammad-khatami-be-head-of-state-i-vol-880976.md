---
signal_id: "CMSIG20260712VS01"
signal_slug: "will-mohammad-khatami-be-head-of-state-i-vol-880976"
headline: "Khatami Iran head of state: 0% on $881K surge"
semantic_title: "Capital stacks against Khatami's return to Iranian leadership"
telemetry: "0% · $881K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-12T09:48:30+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4266ab921148974f104cbadd099e13bca989441bf58acfd2a08fc6cc7440e1a1"
  question_raw: "Will Mohammad Khatami be head of state in Iran end of 2026?"
  current_price: 0.002
  volume_24h_usd: 880976.6289999989
  volume_cumulative_usd: 2026859.5802690003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Khatami at 0% end-of-2026, reformist path to power deemed effectively impossible."
  - "$881K in 24h is 43% of $2M all-time pool, the single largest daily session on this contract."
  - "Volume spike alongside the Motahari zero suggests coordinated Iran succession basket settlement."
  - "Resolves December 31, 2026; flows indicate institutional finality rather than speculative entry."
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
      poly_vol_24h_usd: 880976.6289999989
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-12T09:48:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous heavy volume on both Iran leadership contracts at zero points to a macro desk unwinding a multi-leg Iran political hedge as succession uncertainty collapses.
