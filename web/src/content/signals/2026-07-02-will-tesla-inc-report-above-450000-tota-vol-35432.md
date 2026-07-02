---
signal_id: "CMSIG20260702VS07"
signal_slug: "will-tesla-inc-report-above-450000-tota-vol-35432"
headline: "Tesla Q2 deliveries >450K: 90% on $35K Kalshi flow"
semantic_title: "Tesla Q2 delivery beat above 450K sits deep in high-conviction territory"
telemetry: "90% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-02T10:35:06+00:00"
event_id: "CM-EVT-40YSQ5G480"
event_slug: "kxtsla-26juldeliv"
event_question: "Will Tesla deliver vehicles in Q2?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTSLA-26JULDELIV-450000.0"
  question_raw: "Will Tesla Inc. report above 450000 total deliveries in Q2 2026?"
  current_price: 0.9
  volume_24h_usd: 35432.24
  volume_cumulative_usd: 107787.06
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-21T20:00:00Z"
bullets:
  - "90% price reflects strong market confidence that Tesla will report above 450K total Q2 2026 deliveries."
  - "$35K in 24h, 33% of all-time Kalshi volume, marks a notable acceleration as delivery reporting nears."
  - "Tesla is expected to report Q2 deliveries in the first days of July; this surge is a pre-announcement positioning wave."
  - "10% residual risk covers supply chain disruptions, demand shortfalls, or a reporting methodology change."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 35432.24
sources:
  - label: "ClearMarket market record: Will Tesla deliver vehicles in Q2?"
    url: "https://clearmarket.fyi/events/kxtsla-26juldeliv"
    retrieved_at: "2026-07-02T10:35:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Pre-announcement volume clustering at 90% suggests informed participants with supply chain visibility are confident in the delivery number, desks should cross-reference against TSLA options positioning and analyst estimate revisions.
