---
signal_id: "CMSIG20260603VS03"
signal_slug: "strait-of-hormuz-traffic-returns-to-norm-vol-222186"
headline: "Hormuz traffic normal by June 15: 14% on $222K"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-03T01:46:55+00:00"
event_id: "CM-EVT-2MDYQZTGW0"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-june-15"
event_question: "Will the Strait of Hormuz traffic return to normal by June 15?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x46666ceb4c63814f38a8c83784ae10e1c2e1ef52e2db648372bd86dea521cf64"
  question_raw: "Strait of Hormuz traffic returns to normal by June 15?"
  current_price: 0.14
  volume_24h_usd: 222186.66201099998
  volume_cumulative_usd: 283036.49311499967
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-15T00:00:00Z"
bullets:
  - "Polymarket prices 14% chance Strait of Hormuz returns to normal shipping within 12 days."
  - "$222K in 24h, 79% of all-time volume; contract essentially born this session."
  - "Fresh market creation tied to Hormuz disruption headlines; attention precedes resolution catalyst."
  - "Resolves June 15; energy supply and tanker-rate desks have direct exposure."
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
      poly_vol_24h_usd: 222186.66201099998
sources:
  - label: "ClearMarket market record: Will the Strait of Hormuz traffic return to normal by J"
    url: "https://clearmarket.fyi/events/strait-of-hormuz-traffic-returns-to-normal-by-june-15"
    retrieved_at: "2026-06-03T01:46:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

86% probability of continued Hormuz disruption through mid-June, with the bulk of lifetime volume arriving today, signals commodity desks should price ongoing chokepoint risk into near-term oil and freight positioning.
