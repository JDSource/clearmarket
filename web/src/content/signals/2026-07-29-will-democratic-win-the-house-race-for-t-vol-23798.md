---
signal_id: "CMSIG20260729VS04"
signal_slug: "will-democratic-win-the-house-race-for-t-vol-23798"
headline: "Democrat TX-15 House: 58% on $24K surge"
semantic_title: "Democrats lead in TX-15 House race with odds above 50%"
telemetry: "58% · $24K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-29T10:36:04+00:00"
event_id: "CM-EVT-F1CD0HM6W4"
event_slug: "housetx15-26"
event_question: "TX-15 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSETX15-26-D"
  question_raw: "Will Democratic win the House race for TX-15?"
  current_price: 0.58
  volume_24h_usd: 23798.87
  volume_cumulative_usd: 37826.87
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in Texas's 15th congressional district at 58%, a narrow lean."
  - "63% of all-time volume arrived in 24h, compressing the contract's trading history into one session."
  - "TX-15 is a competitive Rio Grande Valley seat; fresh polling or candidate news likely drove the inflow."
  - "Resolves on the official TX-15 election result; race remains inside the margin of conviction."
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
      kalshi_vol_24h_usd: 23798.87
sources:
  - label: "ClearMarket market record: TX-15 House winner?"
    url: "https://clearmarket.fyi/events/housetx15-26"
    retrieved_at: "2026-07-29T10:36:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly two-thirds of all lifetime volume in a single day on a competitive Texas House seat signals that new campaign intelligence, polling, fundraising, or endorsements, is moving congressional race odds.
