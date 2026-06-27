---
signal_id: "CMSIG20260627VS06"
signal_slug: "will-the-h200-compute-per-hour-price-be-vol-10818"
headline: "H200 compute >$4.99/hr by Jun 30: 90% on $11K"
semantic_title: "H200 compute pricing above $4.99 by June 30 defended near consensus"
telemetry: "90% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T10:03:08+00:00"
event_id: "CM-EVT-XQHHCRQHC2"
event_slug: "kxh200q-26jun30"
event_question: "Will the price of NVIDIA H200 compute decrease by June 30, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200Q-26JUN30-4.990"
  question_raw: "Will the H200 compute per hour price be above $4.99 by Jun 30?"
  current_price: 0.9
  volume_24h_usd: 10818.02
  volume_cumulative_usd: 37332.52
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi at 90%, market prices sustained GPU compute premium as near-certain through end of June."
  - "$11K in 24h is 29% of all-time volume; institutional attention intensifying at contract expiry."
  - "H200 spot rates have remained elevated on persistent AI inference demand; 90% reflects supply constraint conviction."
  - "Resolves June 30, residual 10% discount may reflect thin liquidity risk or last-hour rate compression."
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
      kalshi_vol_24h_usd: 10818.02
sources:
  - label: "ClearMarket market record: Will the price of NVIDIA H200 compute decrease by June "
    url: "https://clearmarket.fyi/events/kxh200q-26jun30"
    retrieved_at: "2026-06-27T10:03:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-unanimous pricing with fresh volume at expiry tells a desk that the AI compute premium trade remains crowded and largely uncontested, any softening in the 90% would be an early signal of supply relief.
