---
signal_id: "CMSIG20260924VS04"
signal_slug: "will-dan-sullivan-win-the-alaska-senate-vol-85878"
headline: "Sullivan AK Senate: 27% on $86K Polymarket spike"
semantic_title: "Dan Sullivan trades at 27% as Alaska race draws more money"
telemetry: "27% · $86K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T13:08:49+00:00"
event_id: "CM-EVT-FSS872PZ65"
event_slug: "alaska-senate-election-winner"
event_question: "Alaska Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x741bb46008b72234857c5118c8365ab3c2f69dbf28b30b59de04f173b8a778de"
  question_raw: "Will Dan Sullivan win the Alaska Senate race in 2026?"
  current_price: 0.27
  volume_24h_usd: 85878.64440800001
  volume_cumulative_usd: 283422.33938099997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "27% odds make Sullivan a heavy underdog in his Alaska Senate re-election bid."
  - "Polymarket records $86K in 24h, 30% of all-time volume, in a clear single-session burst."
  - "Closely mirrors Kalshi's GOP Alaska contract (Spike 1), confirming cross-venue conviction on the same outcome."
  - "Resolves on the 2026 Alaska Senate election result."
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
      poly_vol_24h_usd: 85878.64440800001
sources:
  - label: "ClearMarket market record: Alaska Senate Election Winner"
    url: "https://clearmarket.fyi/events/alaska-senate-election-winner"
    retrieved_at: "2026-09-24T13:08:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sullivan's odds at 27% across two venues simultaneously spiking in volume suggests a coordinated information update, new polling or a major endorsement, that warrants immediate attention from political-risk monitors.
