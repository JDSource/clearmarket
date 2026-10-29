---
signal_id: "CMSIG20261029VS05"
signal_slug: "will-democratic-win-the-house-race-for-v-vol-40222"
headline: "VA-05 Dem House: 43% on $40K Kalshi flow"
semantic_title: "Fresh volume returns to the VA-05 House race near 50%"
telemetry: "43% · $40K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T14:56:22+00:00"
event_id: "CM-EVT-J5Q1GQ0MF2"
event_slug: "kxhouserace-va05-26"
event_question: "Will a winner be determined in the Virginia 5th Congressional District House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-VA05-26-D"
  question_raw: "Will Democratic win the House race for VA-05?"
  current_price: 0.43
  volume_24h_usd: 40222.16
  volume_cumulative_usd: 153244.69
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Market gives Democrats a 43% chance, just below even, in Virginia's 5th congressional district."
  - "Kalshi records $40.2K in 24h, 26% of all-time volume, a notable late-October burst."
  - "Near-50% pricing with rising volume marks VA-05 as a live competitive race drawing fresh attention."
  - "Resolves on the 2026 VA-05 general election result."
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
      kalshi_vol_24h_usd: 40222.16
sources:
  - label: "ClearMarket market record: Will a winner be determined in the Virginia 5th Congres"
    url: "https://clearmarket.fyi/events/kxhouserace-va05-26"
    retrieved_at: "2026-10-29T14:56:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-even price with a fresh volume surge in late October flags VA-05 as a genuine toss-up that desks may be trading as a bellwether for broader House control scenarios.
