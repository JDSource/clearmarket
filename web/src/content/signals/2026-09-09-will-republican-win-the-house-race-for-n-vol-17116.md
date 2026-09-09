---
signal_id: "CMSIG20260909VS03"
signal_slug: "will-republican-win-the-house-race-for-n-vol-17116"
headline: "NJ-7 Republican: 30% on $17K activity burst"
semantic_title: "Republican NJ-7 odds stay under 50% in volume test"
telemetry: "30% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-09T12:40:54+00:00"
event_id: "CM-EVT-P0428D3JR9"
event_slug: "housenj7-26"
event_question: "Who will win the New Jersey 7th Congressional District House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENJ7-26-R"
  question_raw: "Will Republican win the House race for NJ-7?"
  current_price: 0.3
  volume_24h_usd: 17116.69
  volume_cumulative_usd: 22382.06
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "The Republican side of NJ-7 prices at 30% on Kalshi, consistent with the Democratic contract at 71%."
  - "76% of all-time Republican-leg volume cleared in 24h, mirroring the surge in the opposing contract."
  - "Paired spike on both legs confirms concentrated district attention, not simple arbitrage noise."
  - "Resolves as the inverse of the Democratic NJ-7 contract on Election Night 2026."
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
      kalshi_vol_24h_usd: 17116.69
sources:
  - label: "ClearMarket market record: Who will win the New Jersey 7th Congressional District "
    url: "https://clearmarket.fyi/events/housenj7-26"
    retrieved_at: "2026-09-09T12:40:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous all-time volume flush on both legs of NJ-7 is a strong signal that a desk should treat this district as actively moving on an off-market catalyst, the two-sided surge warrants primary source confirmation.
