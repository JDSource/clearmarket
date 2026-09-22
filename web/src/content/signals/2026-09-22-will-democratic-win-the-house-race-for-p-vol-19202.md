---
signal_id: "CMSIG20260922VS06"
signal_slug: "will-democratic-win-the-house-race-for-p-vol-19202"
headline: "Democrat PA-1 House: 38% on $19K volume inflow"
semantic_title: "Buyers back Democrats in PA-1 at 38% with fresh volume"
telemetry: "38% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T07:48:31+00:00"
event_id: "CM-EVT-GWDTD01SV1"
event_slug: "housepa1-26"
event_question: "PA-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEPA1-26-D"
  question_raw: "Will Democratic win the House race for PA-1?"
  current_price: 0.38
  volume_24h_usd: 19202.1
  volume_cumulative_usd: 63787.04
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in PA-1 at 38%, competitive underdog territory in a closely watched suburban Pennsylvania seat."
  - "$19.2K in 24h represents 30% of all-time volume, a meaningful but not extreme concentration suggesting steady re-rating."
  - "PA-1 is a key midterm bellwether; fresh activity at 38% may reflect new polling, candidate fundraising disclosures, or voter registration data."
  - "Resolves on 2026 midterm election results for PA-1."
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
      kalshi_vol_24h_usd: 19202.1
sources:
  - label: "ClearMarket market record: PA-01 House winner?"
    url: "https://clearmarket.fyi/events/housepa1-26"
    retrieved_at: "2026-09-22T07:48:31+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Steady volume re-rating on a competitive House seat at 38% warrants a polling and fundraising check, this price is sensitive enough that a single credible data point could move it materially.
