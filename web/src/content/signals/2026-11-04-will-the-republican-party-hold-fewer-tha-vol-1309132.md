---
signal_id: "CMSIG20261104VS03"
signal_slug: "will-the-republican-party-hold-fewer-tha-vol-1309132"
headline: "GOP under 45 Senate seats: 89% on $1.3M"
semantic_title: "Odds hold that Republicans fall below 45 Senate seats"
telemetry: "89% · $1.3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T15:57:35+00:00"
event_id: "CM-EVT-93ZNVQ37R3"
event_slug: "rsenateseats-27"
event_question: "How many Senate seats will Republicans hold after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "RSENATESEATS-27-B45"
  question_raw: "Will the Republican party hold fewer than 45 Senate seats in the 120th Congress?"
  current_price: 0.89
  volume_24h_usd: 1309132.39
  volume_cumulative_usd: 1965321.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Republicans holding fewer than 45 Senate seats at 89%, a heavy lean."
  - "$1.3M is 67% of all-time volume on this contract, surging as seat counts clarify."
  - "With Mississippi and Alaska both pricing Democratic wins above 90%, this macro seat-count contract is repricing accordingly."
  - "Resolves on final certified composition of the 120th Senate."
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
      kalshi_vol_24h_usd: 1309132.39
sources:
  - label: "ClearMarket market record: How many Senate seats will Republicans hold after the m"
    url: "https://clearmarket.fyi/events/rsenateseats-27"
    retrieved_at: "2026-11-04T15:57:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 67% all-time volume share at 89% on Election Day tells desks that the broader Senate map has moved decisively Democratic and macro seat-count exposure is being closed out.
