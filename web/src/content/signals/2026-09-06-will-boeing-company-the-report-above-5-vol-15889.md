---
signal_id: "CMSIG20260906VS02"
signal_slug: "will-boeing-company-the-report-above-5-vol-15889"
headline: "Boeing 560+ deliveries 2026: 96% on $16K surge"
semantic_title: "Heavy trading backs Boeing topping 560 deliveries in 2026"
telemetry: "96% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-06T11:54:44+00:00"
event_id: "CM-EVT-XC5LD6MTP5"
event_slug: "kxbaa-28jandeliv"
event_question: "Boeing commercial airplane deliveries, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBAA-28JANDELIV-560"
  question_raw: "Will Boeing Company (The) report Above 560 commercial airplane deliveries in 2026?"
  current_price: 0.96
  volume_24h_usd: 15889.8
  volume_cumulative_usd: 22613.49
  arbitration_model: "kalshi_staff"
  resolves_at: "2028-03-31T05:00:00Z"
bullets:
  - "96% pricing reflects strong market conviction that Boeing crosses 560 commercial deliveries in 2026."
  - "70% of all-time contract volume traded in 24 hours, the deepest single-day concentration in this market's history."
  - "Boeing's production ramp and recent delivery data likely triggered a final-leg repricing toward near-certainty."
  - "Resolution tied to full-year 2026 delivery count; at 96%, the market leaves little room for a supply-chain shock."
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
      kalshi_vol_24h_usd: 15889.8
sources:
  - label: "ClearMarket market record: Boeing commercial airplane deliveries, 2026"
    url: "https://clearmarket.fyi/events/kxbaa-28jandeliv"
    retrieved_at: "2026-09-06T11:54:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-exhaustion of all-time volume in one session suggests traders are closing out residual short positions; a desk covering aerospace should note the market is treating Boeing's delivery recovery as essentially confirmed.
