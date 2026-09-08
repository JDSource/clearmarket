---
signal_id: "CMSIG20260908VS05"
signal_slug: "will-boeing-company-the-report-above-5-vol-10402"
headline: "Boeing 2026 deliveries above 560: 95% on $10K surge"
semantic_title: "Buyers back Boeing crossing 560 commercial deliveries in 2026"
telemetry: "95% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-08T12:34:41+00:00"
event_id: "CM-EVT-XC5LD6MTP5"
event_slug: "kxbaa-28jandeliv"
event_question: "Boeing commercial airplane deliveries, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBAA-28JANDELIV-560"
  question_raw: "Will Boeing Company (The) report Above 560 commercial airplane deliveries in 2026?"
  current_price: 0.95
  volume_24h_usd: 10402.37
  volume_cumulative_usd: 32818.3
  arbitration_model: "kalshi_staff"
  resolves_at: "2028-03-31T05:00:00Z"
bullets:
  - "Kalshi prices the above-560 threshold at 95%, the market treats this production target as effectively achieved."
  - "$10.4K in 24h is 32% of all-time volume, a meaningful late-stage activity burst for an industrial output contract."
  - "Volume at 95% pricing points to settlement-stage positioning as Boeing's 2026 delivery pace becomes trackable from reported data."
  - "Contract resolves on Boeing's official 2026 full-year commercial airplane delivery count."
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
      kalshi_vol_24h_usd: 10402.37
sources:
  - label: "ClearMarket market record: Boeing commercial airplane deliveries, 2026"
    url: "https://clearmarket.fyi/events/kxbaa-28jandeliv"
    retrieved_at: "2026-09-08T12:34:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain pricing with a volume spike suggests the market has incorporated recent Boeing delivery data, a desk tracking aerospace supply-chain risk should treat the 560+ target as consensus and monitor for any production disruption that could challenge it.
