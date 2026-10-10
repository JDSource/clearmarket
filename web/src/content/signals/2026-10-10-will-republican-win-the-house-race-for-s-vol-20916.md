---
signal_id: "CMSIG20261010VS02"
signal_slug: "will-republican-win-the-house-race-for-s-vol-20916"
headline: "SC-01 GOP House: 72% on $21K surge"
semantic_title: "Heavy trading tests the GOP's 72% edge in SC-01"
telemetry: "72% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T07:48:40+00:00"
event_id: "CM-EVT-1VRNWSCZT7"
event_slug: "kxhouserace-sc01-26"
event_question: "SC-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-SC01-26-R"
  question_raw: "Will Republican win the House race for SC-01?"
  current_price: 0.72
  volume_24h_usd: 20916.07
  volume_cumulative_usd: 33286.56
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi marks Republicans at 72% to win SC-01, a moderate-to-strong favorite read."
  - "63% of the contract's all-time volume, $21K, cleared in the last 24 hours."
  - "Parallel surge in the Democratic SC-01 contract (spike 3) suggests two-sided attention, not one-directional pressure."
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
      kalshi_vol_24h_usd: 20916.07
sources:
  - label: "ClearMarket market record: SC-01 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-sc01-26"
    retrieved_at: "2026-10-10T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes on both the Republican and Democratic SC-01 contracts signal active two-sided market engagement; a desk should watch for a polling release or candidate event driving re-pricing in the district.
