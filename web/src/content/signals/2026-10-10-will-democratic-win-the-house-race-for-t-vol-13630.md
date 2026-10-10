---
signal_id: "CMSIG20261010VS06"
signal_slug: "will-democratic-win-the-house-race-for-t-vol-13630"
headline: "TX-35 Dem House: 63% on $14K Kalshi volume"
semantic_title: "Buyers back Democratic TX-35 as odds hold above 50%"
telemetry: "63% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T14:12:44+00:00"
event_id: "CM-EVT-30RGTM2V02"
event_slug: "kxhousetx35-26"
event_question: "Will there be a winner determined in the TX-35 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSETX35-26-D"
  question_raw: "Will Democratic win the House race for TX-35?"
  current_price: 0.63
  volume_24h_usd: 13630.39
  volume_cumulative_usd: 52858.42
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic candidate at 63%, market gives a clear but not commanding edge in this Texas seat."
  - "$14K in 24h is 26% of all-time volume, a moderate but notable acceleration for a high-liquidity contract."
  - "TX-35 drawing fresh attention at 63% suggests a competitive dynamic is keeping traders engaged late in the cycle."
  - "Resolves on TX-35 general election outcome."
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
      kalshi_vol_24h_usd: 13630.39
sources:
  - label: "ClearMarket market record: Will there be a winner determined in the TX-35 House ra"
    url: "https://clearmarket.fyi/events/kxhousetx35-26"
    retrieved_at: "2026-10-10T14:12:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 63% Democratic price in a Texas House race drawing a fresh volume pulse tells a desk this seat is being watched as a bellwether for Hispanic-district dynamics, any polling or early-vote data could move the price.
