---
signal_id: "CMSIG20260912VS04"
signal_slug: "will-democratic-win-the-house-race-for-p-vol-20918"
headline: "Dems PA-1 House: 41% on $20.9K volume spike"
semantic_title: "PA-1 House odds slip below 50% on heavy trading"
telemetry: "41% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-12T11:56:57+00:00"
event_id: "CM-EVT-GWDTD01SV1"
event_slug: "housepa1-26"
event_question: "PA-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEPA1-26-D"
  question_raw: "Will Democratic win the House race for PA-1?"
  current_price: 0.41
  volume_24h_usd: 20918.33
  volume_cumulative_usd: 26867.03
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in PA-1 at 41%, the market leans Republican in this competitive seat."
  - "$20.9K in 24h volume is 78% of the contract's total all-time volume, an extraordinary one-day concentration."
  - "A near-total lifetime-volume flush in a single day points to a specific local catalyst, polling, candidate news, or redistricting update."
  - "Resolves on the PA-1 House election result."
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
      kalshi_vol_24h_usd: 20918.33
sources:
  - label: "ClearMarket market record: PA-01 House winner?"
    url: "https://clearmarket.fyi/events/housepa1-26"
    retrieved_at: "2026-09-12T11:56:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When 78% of a contract's lifetime volume prints in one session, a desk modeling House majority probabilities should treat PA-1 as newly contested and investigate the triggering catalyst immediately.
