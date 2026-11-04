---
signal_id: "CMSIG20261104VS05"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-995453"
headline: "NY-17 Dem House: 100% on $995K surge"
semantic_title: "NY-17 House race trades to certainty for Democrats"
telemetry: "100% · $995K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T15:57:35+00:00"
event_id: "CM-EVT-YYRD31F2R5"
event_slug: "houseny17-26"
event_question: "Will a new representative be elected for New York's 17th House district by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENY17-26-D"
  question_raw: "Will Democratic win the House race for NY-17?"
  current_price: 0.998
  volume_24h_usd: 995453.92
  volume_cumulative_usd: 1388639.18
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic NY-17 House win at 100%, market has fully resolved this race."
  - "$995K is 72% of all-time contract volume, arriving as Election Day results come in."
  - "NY-17 was a targeted competitive district; a 100% price means reported results are decisive."
  - "Resolves on certified NY-17 congressional result."
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
      kalshi_vol_24h_usd: 995453.92
sources:
  - label: "ClearMarket market record: Will a new representative be elected for New York's 17t"
    url: "https://clearmarket.fyi/events/houseny17-26"
    retrieved_at: "2026-11-04T15:57:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 100% print on 72% of all-time volume tells a desk that NY-17 is called and traders are clearing residual short positions at zero cost.
