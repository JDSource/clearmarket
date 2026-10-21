---
signal_id: "CMSIG20261021VS02"
signal_slug: "will-russia-enter-khatnie-by-december-31-vol-38438"
headline: "Russia takes Khatnie by Dec 31: 27% on $38K"
semantic_title: "Russia entering Khatnie by year-end stays a low-odds bet"
telemetry: "27% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T13:25:08+00:00"
event_id: "CM-EVT-KR1P3ML5Y6"
event_slug: "will-russia-enter-khatnie-by"
event_question: "Will Russia enter Khatnie by June 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x41026240b7e9da9e447ba71d113c8e09dd0fff1bafa3a4a8ec38febe12d43f7a"
  question_raw: "Will Russia enter Khatnie by December 31, 2026?"
  current_price: 0.27
  volume_24h_usd: 38438.951052
  volume_cumulative_usd: 108248.119767
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 27% chance Russia enters Khatnie before December 31, odds lean against the scenario."
  - "36% of all-time volume, $38K, arrived in 24 hours, pointing to a ground-condition or front-line update driving fresh bets."
  - "At 27%, traders are pricing meaningful but minority-case risk; the contract is live to battlefield reporting."
  - "Resolves YES on credible confirmation of Russian forces entering Khatnie by December 31, 2026."
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
      poly_vol_24h_usd: 38438.951052
sources:
  - label: "ClearMarket market record: Will Russia enter Khatnie by June 2026?"
    url: "https://clearmarket.fyi/events/will-russia-enter-khatnie-by"
    retrieved_at: "2026-10-21T13:25:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 36% all-time volume spike on a specific territorial milestone tells a desk that front-line movement or intelligence reporting has sharpened near-term event risk, 27% is not negligible for a geopolitical desk running Ukraine exposure.
