---
signal_id: "CMSIG20261023VS04"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-50754"
headline: "NC-1 House Dem: 80% on $51K Kalshi surge"
semantic_title: "Democrats lead NC-1 with 80% odds drawing heavy money"
telemetry: "80% · $51K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T07:49:03+00:00"
event_id: "CM-EVT-22K74MYTV1"
event_slug: "housenc1-26"
event_question: "Will the winner of the North Carolina 1st Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENC1-26-D"
  question_raw: "Will Democratic win the House race for NC-1?"
  current_price: 0.8
  volume_24h_usd: 50754.58
  volume_cumulative_usd: 149527.25
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "80% price on Kalshi puts Democrats as a solid favorite to hold or flip NC-1 in the 2026 cycle."
  - "$50,755 in 24h volume equals 34% of all-time, meaningful single-session commitment on a competitive district."
  - "NC-1 is a targeted competitive seat; fresh volume at 80% suggests recent polling or candidate news moved conviction."
  - "Resolves on 2026 NC-1 House general election result."
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
      kalshi_vol_24h_usd: 50754.58
sources:
  - label: "ClearMarket market record: Will the winner of the North Carolina 1st Congressional"
    url: "https://clearmarket.fyi/events/housenc1-26"
    retrieved_at: "2026-10-23T07:49:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained 80% Democratic pricing with a 34% all-time daily volume spike on a competitive North Carolina district is actionable for any desk tracking House majority scenarios, the market is expressing genuine directional conviction, not just noise.
