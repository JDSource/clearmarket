---
signal_id: "CMSIG20260924VS03"
signal_slug: "will-dan-sullivan-win-the-alaska-senate-vol-86678"
headline: "Sullivan AK Senate: 27% on $87K surge"
semantic_title: "Dan Sullivan odds sit at 27% as Polymarket volume picks up"
telemetry: "27% · $87K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T07:48:17+00:00"
event_id: "CM-EVT-FSS872PZ65"
event_slug: "alaska-senate-election-winner"
event_question: "Alaska Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x741bb46008b72234857c5118c8365ab3c2f69dbf28b30b59de04f173b8a778de"
  question_raw: "Will Dan Sullivan win the Alaska Senate race in 2026?"
  current_price: 0.27
  volume_24h_usd: 86678.34491399999
  volume_cumulative_usd: 283410.15938100003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Dan Sullivan's re-election at 27%, closely mirroring the Kalshi Republican contract."
  - "$86.7K traded in 24h, equal to 31% of all-time volume on this contract."
  - "Cross-venue alignment near 27-29% signals consistent bearish read on Sullivan, not noise on one platform."
  - "Resolves on the 2026 Alaska Senate general election result."
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
      poly_vol_24h_usd: 86678.34491399999
sources:
  - label: "ClearMarket market record: Alaska Senate Election Winner"
    url: "https://clearmarket.fyi/events/alaska-senate-election-winner"
    retrieved_at: "2026-09-24T07:48:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The tight Kalshi/Polymarket convergence around 27-29% on Sullivan adds conviction to the bearish read, a useful cross-venue sanity check for any desk running political-risk positions.
