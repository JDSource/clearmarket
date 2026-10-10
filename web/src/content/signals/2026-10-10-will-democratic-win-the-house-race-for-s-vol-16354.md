---
signal_id: "CMSIG20261010VS04"
signal_slug: "will-democratic-win-the-house-race-for-s-vol-16354"
headline: "SC-01 Dem House: 28% on $16K volume burst"
semantic_title: "Democratic SC-01 long shot stays under 30% in active trade"
telemetry: "28% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T14:12:44+00:00"
event_id: "CM-EVT-1VRNWSCZT7"
event_slug: "kxhouserace-sc01-26"
event_question: "SC-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-SC01-26-D"
  question_raw: "Will Democratic win the House race for SC-01?"
  current_price: 0.28
  volume_24h_usd: 16354.25
  volume_cumulative_usd: 36397.4
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Democratic candidate at 28%, the contract is live but the market stays skeptical."
  - "$16K in 24h covers 45% of all-time volume, moving in tandem with the Republican SC-01 spike."
  - "The paired surge on both sides of this seat points to a competitive-race reassessment rather than noise."
  - "Resolves on SC-01 general election outcome."
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
      kalshi_vol_24h_usd: 16354.25
sources:
  - label: "ClearMarket market record: SC-01 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-sc01-26"
    retrieved_at: "2026-10-10T14:12:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The Democratic side of SC-01 drawing 45% of its lifetime volume alongside the Republican contract confirms a desk should flag this district as freshly contested, the 28% price may be the key level to watch.
