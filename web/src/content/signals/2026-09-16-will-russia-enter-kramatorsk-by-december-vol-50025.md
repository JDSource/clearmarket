---
signal_id: "CMSIG20260916VS03"
signal_slug: "will-russia-enter-kramatorsk-by-december-vol-50025"
headline: "Russia enters Kramatorsk by Dec 31: 22% on $50K"
semantic_title: "Russia reaching Kramatorsk by year-end stays a long shot at 22%"
telemetry: "22% · $50K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-16T13:03:41+00:00"
event_id: "CM-EVT-7G3FWY0RL4"
event_slug: "which-cities-will-russia-enter-by-december-31"
event_question: "Will Russia enter any additional cities by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x357ee5e692658d4dae5b7fe59bae12cef029f2ebffb5452f4d439a1934d84211"
  question_raw: "Will Russia enter Kramatorsk by December 31, 2026?"
  current_price: 0.22
  volume_24h_usd: 50025.057259
  volume_cumulative_usd: 129697.265657
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Russian capture of Kramatorsk at 22%, reflecting low but non-trivial odds of a major eastern Ukraine shift."
  - "$50K in 24h accounts for 39% of all-time volume, pointing to renewed geopolitical attention on the Donetsk front."
  - "Kramatorsk is a key logistics hub; fresh trading may follow battlefield reporting or diplomatic developments."
  - "December 31 deadline is the resolution gate, roughly 15 weeks of conflict trajectory to monitor."
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
      poly_vol_24h_usd: 50025.057259
sources:
  - label: "ClearMarket market record: Will Russia enter any additional cities by December 31?"
    url: "https://clearmarket.fyi/events/which-cities-will-russia-enter-by-december-31"
    retrieved_at: "2026-09-16T13:03:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 22% price absorbing 39% of lifetime volume in one day signals desks are actively repricing Ukraine conflict tail risk, relevant for energy, defense, and Eastern European sovereign exposure.
