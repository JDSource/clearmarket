---
signal_id: "CMSIG20260823VS00"
signal_slug: "will-ukraine-re-enter-myrnohrad-by-decem-vol-35916"
headline: "Ukraine Myrnohrad reentry: 6% on $35K surge"
semantic_title: "Traders back long odds on Ukraine retaking Myrnohrad"
telemetry: "6% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-23T08:24:40+00:00"
event_id: "CM-EVT-G8QGG1QZ27"
event_slug: "will-ukraine-re-enter-myrnohrad-by-may-31"
event_question: "Will Ukraine re-enter Myrnohrad in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x578cfae7575d7d072fc67f12b4920a1aca31050a45f15344674fd37f16f52d42"
  question_raw: "Will Ukraine re-enter Myrnohrad by December 31?"
  current_price: 0.06
  volume_24h_usd: 35916.95
  volume_cumulative_usd: 106433.99087600001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Ukrainian return to Myrnohrad by Dec 31 at just 6%, deep skepticism of near-term offensive success."
  - "24h volume of $35K is 34% of all-time handle, a sharp single-day concentration on a low-liquidity front-line contract."
  - "Surge likely reflects battlefield news flow or Ukrainian operational signals drawing fresh attention to this specific city."
  - "Resolves Dec 31, 2026; at 6%, the market is pricing this as a tail scenario, not a base case."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 35916.95
sources:
  - label: "ClearMarket market record: Will Ukraine re-enter Myrnohrad in 2026? (multi-deadlin"
    url: "https://clearmarket.fyi/events/will-ukraine-re-enter-myrnohrad-by-may-31"
    retrieved_at: "2026-08-23T08:24:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 34% all-time volume day on a 6% contract signals a news catalyst is driving speculative positioning, not a consensus view shift, desks should watch for Ukrainian military communiqués or Russian defensive line reporting around Myrnohrad.
