---
signal_id: "CMSIG20260728VS07"
signal_slug: "will-average-gas-prices-be-above-4-vol-23176"
headline: "US gas above $4.04: 98% on $23K surge"
semantic_title: "Average US gas prices staying above $4.04 prices near-certain"
telemetry: "98% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-28T10:31:13+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.04"
  question_raw: "Will average **gas prices** be above $4.04?"
  current_price: 0.98
  volume_24h_usd: 23176.47
  volume_cumulative_usd: 62317.51
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "Kalshi prices average US gas staying above $4.04 at 98%, the market has essentially resolved this affirmatively."
  - "$23K in 24h is 37% of all-time volume, a moderate share but notable given the extreme price level."
  - "Trading into a 98% contract suggests either a near-term resolution date or hedging against the residual 2% tail."
  - "Resolves on the EIA average retail price print; the 2% residual prices a sharp demand-shock or data anomaly."
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
      kalshi_vol_24h_usd: 23176.47
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-28T10:31:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain pricing with fresh volume likely reflects an upcoming EIA data release, a desk with energy exposure should confirm the resolution date and treat this as a near-settled macro input.
