---
signal_id: "CMSIG20261005VS02"
signal_slug: "will-republican-win-the-house-race-for-c-vol-34528"
headline: "CO-04 GOP win: 69% as two-thirds of all-time vol clears"
semantic_title: "Heavy trading backs Republican hold in Colorado CO-04"
telemetry: "69% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T07:48:02+00:00"
event_id: "CM-EVT-GZL5K2GKF0"
event_slug: "kxhouserace-co04-26"
event_question: "CO-04 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-CO04-26-R"
  question_raw: "Will Republican win the House race for CO-04?"
  current_price: 0.69
  volume_24h_usd: 34528.92
  volume_cumulative_usd: 52083.49
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in CO-04 at 69%, moderate favorite, not a lock, retaining real Democratic upset risk."
  - "66% of all-time contract volume traded in 24 hours, the dominant single session by a wide margin."
  - "CO-04 was redrawn after 2022; fresh attention may reflect new polling or a candidate development in the district."
  - "Resolves on the November 2026 general election result for Colorado's 4th congressional district."
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
      kalshi_vol_24h_usd: 34528.92
sources:
  - label: "ClearMarket market record: CO-04 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-co04-26"
    retrieved_at: "2026-10-05T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two-thirds of all-time volume in one session on a House district race is an outsized signal, a desk watching House majority math should flag CO-04 as a newly contested seat where market participants see information worth pricing.
