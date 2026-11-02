---
signal_id: "CMSIG20261102VS06"
signal_slug: "will-the-republican-party-hold-exactly-4-vol-49726"
headline: "GOP holds 46 seats, 120th Congress: 21% on $50K"
semantic_title: "Betting picks up on Republicans holding exactly 46 Senate seats"
telemetry: "21% · $50K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T17:45:32+00:00"
event_id: "CM-EVT-93ZNVQ37R3"
event_slug: "rsenateseats-27"
event_question: "How many Senate seats will Republicans hold after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "RSENATESEATS-27-E46"
  question_raw: "Will the Republican party hold exactly 46 Senate seats in the 120th Congress?"
  current_price: 0.21
  volume_24h_usd: 49726.88
  volume_cumulative_usd: 119201.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices the exact 46-seat GOP outcome at 21%, a specific structural bet on a narrow seat-count scenario within a wide distribution."
  - "24h volume of $50K is 42% of all-time flow, the single largest daily share in this contract's history."
  - "An exact-seat-count contract is sensitive to individual race outcomes; the surge implies traders are stress-testing specific map configurations."
  - "Resolves when the 120th Congress seat composition is confirmed."
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
      kalshi_vol_24h_usd: 49726.88
sources:
  - label: "ClearMarket market record: How many Senate seats will Republicans hold after the m"
    url: "https://clearmarket.fyi/events/rsenateseats-27"
    retrieved_at: "2026-11-02T17:45:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 42% all-time share in one session on a precise seat-count contract signals that quantitative Senate-map modelers are stress-testing specific configurations as individual state races reprice.
