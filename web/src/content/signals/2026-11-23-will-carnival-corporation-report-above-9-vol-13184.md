---
signal_id: "CMSIG20261123VS00"
signal_slug: "will-carnival-corporation-report-above-9-vol-13184"
headline: "Carnival 97M berth days: 99% on $13K surge"
semantic_title: "Carnival berth-day target above 97M looks like a lock"
telemetry: "99% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-23T07:48:00+00:00"
event_id: "CM-EVT-MS1NKLYT14"
event_slug: "kxccla-28janalbd"
event_question: "Carnival Corporation available lower berths, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCCLA-28JANALBD-97000000.0"
  question_raw: "Will Carnival Corporation report Above 97 million available lower berth days in 2026?"
  current_price: 0.99
  volume_24h_usd: 13184.82
  volume_cumulative_usd: 17878.43
  arbitration_model: "kalshi_staff"
  resolves_at: "2028-03-31T05:00:00Z"
bullets:
  - "Kalshi prices Carnival clearing 97M available lower berth days at 99%, near-certain resolution."
  - "24h volume of $13,185 is 74% of the contract's entire all-time handle, a sharp late concentration."
  - "Surge likely reflects traders closing residual short exposure ahead of Carnival's capacity reporting."
  - "Contract resolves on Carnival Corporation's official available lower berth day disclosure."
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
      kalshi_vol_24h_usd: 13184.82
sources:
  - label: "ClearMarket market record: Carnival Corporation available lower berths, 2026"
    url: "https://clearmarket.fyi/events/kxccla-28janalbd"
    retrieved_at: "2026-11-23T07:48:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as a near-resolved cleanup trade, the volume spike represents capital chasing the final 1% of residual risk off the book, not a directional view shift.
