---
signal_id: "CMSIG20261104VS06"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-965498"
headline: "NY-17 House Dem: 99% on $965K Kalshi surge"
semantic_title: "NY-17 Democratic House odds hold firm at 99%"
telemetry: "99% · $965K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T07:48:42+00:00"
event_id: "CM-EVT-YYRD31F2R5"
event_slug: "houseny17-26"
event_question: "Will a new representative be elected for New York's 17th House district by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENY17-26-D"
  question_raw: "Will Democratic win the House race for NY-17?"
  current_price: 0.992
  volume_24h_usd: 965498.45
  volume_cumulative_usd: 1340880.09
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic win in NY-17 at 99%, a toss-up district priced as nearly decided."
  - "72% of all-time volume cleared in 24h, an outsized single-session concentration."
  - "NY-17 is a targeted competitive seat; heavy late volume confirms Democratic lean has held through counting."
  - "Resolves on certified NY-17 2026 House result."
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
      kalshi_vol_24h_usd: 965498.45
sources:
  - label: "ClearMarket market record: Will a new representative be elected for New York's 17t"
    url: "https://clearmarket.fyi/events/houseny17-26"
    retrieved_at: "2026-11-04T07:48:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 72% all-time volume rate on NY-17 at 99% tells desks this closely-watched swing district is being written off by any remaining Republican holders, a meaningful signal for House majority math.
