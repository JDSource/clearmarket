---
signal_id: "CMSIG20260627VS05"
signal_slug: "will-us-annex-any-territory-in-2026-vol-45091"
headline: "US annexes territory in 2026: 7% on $45K"
semantic_title: "US annexation in 2026 sits in deep tail territory at 7%"
telemetry: "7% · $45K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T01:36:27+00:00"
event_id: "CM-EVT-9XS608W3B5"
event_slug: "will-us-annex-any-territory-in-2026"
event_question: "Will the US annex any territory by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7b0ed36d5d86756b0f854dd2d5a721c951c2e2c6273c63b00c837b1842bb62e4"
  question_raw: "Will US annex any territory in 2026?"
  current_price: 0.07
  volume_24h_usd: 45091.509732000006
  volume_cumulative_usd: 152517.274845
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "7% probability, market treats annexation as a remote but non-trivial geopolitical tail risk."
  - "$45K in 24h is 30% of all-time volume, signaling renewed institutional attention mid-year."
  - "Greenland, Panama Canal, and Canada scenarios likely driving residual long interest."
  - "Full-year 2026 resolution window means risk stays open despite low headline probability."
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
      poly_vol_24h_usd: 45091.509732000006
sources:
  - label: "ClearMarket market record: Will the US annex any territory by the end of 2026?"
    url: "https://clearmarket.fyi/events/will-us-annex-any-territory-in-2026"
    retrieved_at: "2026-06-27T01:36:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh mid-year volume at 7% tells geopolitical desks that a small but meaningful cohort is willing to pay for annexation tail coverage with six months still on the clock.
