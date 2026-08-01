---
signal_id: "CMSIG20260801VS05"
signal_slug: "will-the-monthly-average-compute-price-o-vol-15740"
headline: "H200 avg above $2.00 in Aug: 99% on $16K Kalshi print"
semantic_title: "Fresh volume returns to H200 August average above $2.00 at 99%"
telemetry: "99% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-01T09:55:41+00:00"
event_id: "CM-EVT-0T7SDX2738"
event_slug: "kxh200ms-26aug"
event_question: "Will the NVIDIA H200 average hourly price in August reach a specified threshold?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200MS-26AUG-2.000"
  question_raw: "Will the monthly average compute price of NVIDIA's H200 be above $2.00 in August 2026?"
  current_price: 0.99
  volume_24h_usd: 15740.01
  volume_cumulative_usd: 18477.76
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices 99% odds the monthly average H200 compute price exceeds $2.00 in August."
  - "24h volume of $16K is 85% of all-time flow, a near-total single-day concentration."
  - "Volume surge alongside the $5.49 December contract spike suggests a coordinated repricing read across GPU compute tenors."
  - "Resolves end of August 2026 based on reported monthly average compute pricing."
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
      kalshi_vol_24h_usd: 15740.01
sources:
  - label: "ClearMarket market record: Will the NVIDIA H200 average hourly price in August rea"
    url: "https://clearmarket.fyi/events/kxh200ms-26aug"
    retrieved_at: "2026-08-01T09:55:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Paired with the December H200 contract spike, this tells a desk the market is building a consensus that NVIDIA H200 pricing floors are durable across both near- and long-dated tenors, relevant for any AI infrastructure cost modeling.
