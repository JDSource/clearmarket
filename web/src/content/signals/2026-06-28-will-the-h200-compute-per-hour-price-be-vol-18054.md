---
signal_id: "CMSIG20260628VS06"
signal_slug: "will-the-h200-compute-per-hour-price-be-vol-18054"
headline: "H200 above $4.19/hr: 96% on $18K inflow"
semantic_title: "H200 at $4.19 floor absorbs final-day selling at near-certain levels"
telemetry: "96% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:25:52+00:00"
event_id: "CM-EVT-XQHHCRQHC2"
event_slug: "kxh200q-26jun30"
event_question: "Will the price of NVIDIA H200 compute decrease by June 30, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200Q-26JUN30-4.190"
  question_raw: "Will the H200 compute per hour price be above $4.19 by Jun 30?"
  current_price: 0.96
  volume_24h_usd: 18054.8
  volume_cumulative_usd: 22929.7
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi prices the $4.19 H200 compute floor at 96%, deepest in-the-money of the three GPU contracts."
  - "$18K in 24h is 79% of all-time volume; late sellers absorbing any residual NO bids."
  - "The $4.19 level sits well below prevailing spot, making this a near-mechanical resolution barring market disruption."
  - "Resolves June 30; the 4% NO tail is institutional insurance against data-source or settlement anomalies."
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
      kalshi_vol_24h_usd: 18054.8
sources:
  - label: "ClearMarket market record: Will the price of NVIDIA H200 compute decrease by June "
    url: "https://clearmarket.fyi/events/kxh200q-26jun30"
    retrieved_at: "2026-06-28T10:25:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High all-time volume concentration at a deep in-the-money level reflects end-of-contract settlement activity, desks should treat the $4.19 floor as a confirmed baseline and focus analytical energy on the $4.99 band for forward rate signaling.
