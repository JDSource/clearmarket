---
signal_id: "CMSIG20261010VS03"
signal_slug: "will-democratic-win-the-house-race-for-s-vol-16259"
headline: "SC-01 Dem House: 28% on $16K volume"
semantic_title: "Democrats stay a long shot in SC-01 near 28%"
telemetry: "28% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T07:48:40+00:00"
event_id: "CM-EVT-1VRNWSCZT7"
event_slug: "kxhouserace-sc01-26"
event_question: "SC-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-SC01-26-D"
  question_raw: "Will Democratic win the House race for SC-01?"
  current_price: 0.28
  volume_24h_usd: 16259.05
  volume_cumulative_usd: 36302.2
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Democratic SC-01 win at 28%, market treats this as the underdog side."
  - "45% of all-time volume, $16K, arrived in 24 hours, matching the Republican SC-01 spike timing."
  - "Coordinated two-sided activity in SC-01 is consistent with fresh district-level polling or an opposition research release."
  - "Resolves on 2026 SC-01 House election result."
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
      kalshi_vol_24h_usd: 16259.05
sources:
  - label: "ClearMarket market record: SC-01 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-sc01-26"
    retrieved_at: "2026-10-10T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The Democratic SC-01 contract drawing 45% of its lifetime volume on the same day as the Republican contract suggests market participants are reassessing the district competitiveness rather than simply chasing a narrative.
