---
signal_id: "CMSIG20260909VS01"
signal_slug: "will-democratic-win-the-house-race-for-t-vol-39718"
headline: "TX-28 Democrat: 75% on $40K volume burst"
semantic_title: "Traders back Democrats to hold TX-28 at 75%"
telemetry: "75% · $40K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-09T12:40:54+00:00"
event_id: "CM-EVT-BJ7C9T9VL1"
event_slug: "housetx28-26"
event_question: "TX-28 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSETX28-26-D"
  question_raw: "Will Democratic win the House race for TX-28?"
  current_price: 0.75
  volume_24h_usd: 39718.7
  volume_cumulative_usd: 63849.1
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi contract sits at 75% for a Democratic hold in TX-28, priced as a lean, not a lock."
  - "62% of all-time volume arrived in 24h, signaling a sharp step-up in market attention."
  - "TX-28 has been a contested South Texas seat; fresh volume likely tracks candidate or polling developments."
  - "Contract resolves on certified 2026 midterm results for Texas's 28th Congressional District."
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
      kalshi_vol_24h_usd: 39718.7
sources:
  - label: "ClearMarket market record: TX-28 House winner?"
    url: "https://clearmarket.fyi/events/housetx28-26"
    retrieved_at: "2026-09-09T12:40:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume concentration in a nominally Democratic-leaning but genuinely competitive seat suggests desks should monitor for a new challenger emergence or internal poll leak driving repricing risk.
