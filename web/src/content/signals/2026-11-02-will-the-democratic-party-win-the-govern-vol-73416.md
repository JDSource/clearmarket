---
signal_id: "CMSIG20261102VS03"
signal_slug: "will-the-democratic-party-win-the-govern-vol-73416"
headline: "Maryland Gov Dem: 99% on $73K final surge"
semantic_title: "Maryland governorship is effectively settled for Democrats"
telemetry: "99% · $73K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T07:49:23+00:00"
event_id: "CM-EVT-RYZ7GGP8S0"
event_slug: "govpartymd-26"
event_question: "Maryland Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYMD-26-D"
  question_raw: "Will the Democratic party win the governorship in Maryland"
  current_price: 0.993
  volume_24h_usd: 73416.97
  volume_cumulative_usd: 105231.79
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-18T15:00:00Z"
bullets:
  - "At 99%, Kalshi leaves virtually no probability for a Republican upset in Maryland's governorship."
  - "$73K in 24h is a striking 70% of all-time volume, the bulk of lifetime trading landed today."
  - "Late-stage volume at near-certainty prices likely reflects closing arbitrage and contract cleanup ahead of resolution."
  - "Resolves on Maryland governor race result."
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
      kalshi_vol_24h_usd: 73416.97
sources:
  - label: "ClearMarket market record: Maryland Governor winner?"
    url: "https://clearmarket.fyi/events/govpartymd-26"
    retrieved_at: "2026-11-02T07:49:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 70% all-time volume share arriving at a 99% price signals this is settlement-driven activity, not genuine uncertainty, desks clearing residual positions before resolution.
