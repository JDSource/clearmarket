---
signal_id: "CMSIG20260912VS03"
signal_slug: "will-democratic-win-the-house-race-for-f-vol-35785"
headline: "Dems FL-25 House: 71% on $35.8K volume spike"
semantic_title: "Buyers back Democrats in FL-25 at 71%"
telemetry: "71% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-12T11:56:57+00:00"
event_id: "CM-EVT-Q8F4815M66"
event_slug: "kxhouserace-fl25-26"
event_question: "Will the Florida 25th House seat be won in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL25-26-D"
  question_raw: "Will Democratic win the House race for FL-25?"
  current_price: 0.71
  volume_24h_usd: 35785.69
  volume_cumulative_usd: 57143.76
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in FL-25 at 71%, a strong favorite read in this House race."
  - "$35.8K in 24h volume accounts for 63% of the contract's all-time volume, marking a decisive surge."
  - "Heavy fresh volume in a district race at this late stage implies new local polling or candidate news is driving attention."
  - "Resolves on the FL-25 House election result."
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
      kalshi_vol_24h_usd: 35785.69
sources:
  - label: "ClearMarket market record: Will the Florida 25th House seat be won in the next ele"
    url: "https://clearmarket.fyi/events/kxhouserace-fl25-26"
    retrieved_at: "2026-09-12T11:56:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 63% of lifetime volume hitting in one day, a desk tracking House control scenarios should flag FL-25 as a newly active seat, check for fresh district polling or a candidate development.
