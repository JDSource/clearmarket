---
signal_id: "CMSIG20260821VS04"
signal_slug: "will-the-democrats-win-the-wisconsin-gov-vol-69118"
headline: "Dems win WI governor 2026: 81% on $69K surge"
semantic_title: "Democrats favored to hold Wisconsin governor at 81%"
telemetry: "81% · $69K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-21T08:35:56+00:00"
event_id: "CM-EVT-QYSXP23XP8"
event_slug: "wisconsin-governor-winner-2026"
event_question: "Will the Wisconsin gubernatorial election be won by the incumbent or a challenger?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfbd0a65112e26d9a2a68dc47f8a95c6c14d22650cb4837c5429b546726661b71"
  question_raw: "Will the Democrats win the Wisconsin governor race in 2026?"
  current_price: 0.81
  volume_24h_usd: 69118.87022399998
  volume_cumulative_usd: 183049.24106699994
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democratic retention of Wisconsin's governorship at 81%, a strong lean, not a lock."
  - "24h volume of $69K is 38% of all-time, suggesting renewed attention rather than an inaugural discovery of this contract."
  - "Fresh volume may track a new poll, candidate development, or shifting national environment for 2026 midterm governors."
  - "Wisconsin is a key swing-state bellwether; governor race outcomes carry downstream implications for 2028 electoral infrastructure."
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
      poly_vol_24h_usd: 69118.87022399998
sources:
  - label: "ClearMarket market record: Will the Wisconsin gubernatorial election be won by the"
    url: "https://clearmarket.fyi/events/wisconsin-governor-winner-2026"
    retrieved_at: "2026-08-21T08:35:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A fresh $69K inflow sustaining 81% odds signals the market is confirming, not discovering, Democratic favoritism in Wisconsin, likely in response to new polling or candidate news worth tracking.
