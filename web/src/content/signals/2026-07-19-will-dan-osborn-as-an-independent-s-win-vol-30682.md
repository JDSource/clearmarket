---
signal_id: "CMSIG20260719VS04"
signal_slug: "will-dan-osborn-as-an-independent-s-win-vol-30682"
headline: "Osborn wins Nebraska Senate (ind.): 29% on $30K"
semantic_title: "Dan Osborn independent Senate bid absorbs fresh speculative flow"
telemetry: "29% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-19T09:49:33+00:00"
event_id: "CM-EVT-37PJ66HMC4"
event_slug: "senatene-26"
event_question: "Nebraska Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATENE-26-DOSB"
  question_raw: "Will Dan Osborn (as an independent)s win the Senate race in Nebraska?"
  current_price: 0.29
  volume_24h_usd: 30682.88
  volume_cumulative_usd: 80938.79
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "29% implies the market treats Osborn as a live long-shot, not a fringe candidate, in a red-state race."
  - "$30.7K in 24h accounts for 38% of all-time Kalshi volume, renewed institutional attention on this seat."
  - "Independent Senate bids rarely poll this high; fresh flow may reflect new endorsement or polling data."
  - "Resolves with November 2026 midterms; Osborn's 2024 near-miss gives the contract historical credibility."
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
      kalshi_vol_24h_usd: 30682.88
sources:
  - label: "ClearMarket market record: Nebraska Senate winner?"
    url: "https://clearmarket.fyi/events/senatene-26"
    retrieved_at: "2026-07-19T09:49:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly 40% of lifetime volume arriving in one session on an independent Senate bid signals political desks are reassessing Osborn's viability, check for new Nebraska polling or organizational news.
