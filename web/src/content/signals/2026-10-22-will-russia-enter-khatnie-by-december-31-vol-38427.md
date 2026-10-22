---
signal_id: "CMSIG20261022VS06"
signal_slug: "will-russia-enter-khatnie-by-december-31-vol-38427"
headline: "Russia enters Khatnie by Dec 31: 25% on $38K"
semantic_title: "Russia reaching Khatnie by year-end priced at 25%"
telemetry: "25% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T13:25:36+00:00"
event_id: "CM-EVT-KR1P3ML5Y6"
event_slug: "will-russia-enter-khatnie-by"
event_question: "Will Russia enter Khatnie by June 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x41026240b7e9da9e447ba71d113c8e09dd0fff1bafa3a4a8ec38febe12d43f7a"
  question_raw: "Will Russia enter Khatnie by December 31, 2026?"
  current_price: 0.25
  volume_24h_usd: 38427.74
  volume_cumulative_usd: 146675.85976699996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Russian forces reaching Khatnie by December 31, 2026 at exactly 25%, a clear long-shot."
  - "$38K in 24h is 26% of all-time volume, a steady but meaningful one-day concentration."
  - "Fresh volume on a Ukraine front-line contract points to renewed attention on eastern sector military activity."
  - "Hard December 31 deadline makes this a clean near-term read on battlefield trajectory."
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
      poly_vol_24h_usd: 38427.74
sources:
  - label: "ClearMarket market record: Will Russia enter Khatnie by June 2026?"
    url: "https://clearmarket.fyi/events/will-russia-enter-khatnie-by"
    retrieved_at: "2026-10-22T13:25:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A quarter of lifetime volume in one day on a 25% Ukraine territorial contract suggests a desk is updating Ukraine battlefield models, likely after frontline reporting or Ukrainian military briefing changes the tempo assumption.
