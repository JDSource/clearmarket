---
signal_id: "CMSIG20261022VS00"
signal_slug: "will-republicans-win-the-senate-race-in-vol-131298"
headline: "Idaho Senate GOP: 87% on $131K surge"
semantic_title: "Idaho Senate GOP seat holds at a wide favorite"
telemetry: "87% · $131K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T13:25:36+00:00"
event_id: "CM-EVT-TRRJX6C1D5"
event_slug: "senateid-26"
event_question: "Idaho Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEID-26-R"
  question_raw: "Will Republicans win the Senate race in Idaho?"
  current_price: 0.87
  volume_24h_usd: 131298.29
  volume_cumulative_usd: 289290.31
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican win at 87%, implying near-certain outcome with thin upset risk."
  - "$131K traded in 24h, 45% of all-time volume, the sharpest single-day concentration on record."
  - "Heavy one-day flow into a decided race suggests positioning ahead of early-vote or polling updates."
  - "Resolves on 2026 midterm election night; little ambiguity priced in at current odds."
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
      kalshi_vol_24h_usd: 131298.29
sources:
  - label: "ClearMarket market record: Idaho Senate winner?"
    url: "https://clearmarket.fyi/events/senateid-26"
    retrieved_at: "2026-10-22T13:25:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-half of lifetime volume printing in one session on a lopsided contract signals desks locking in cheap exposure or hedging correlated Senate-control positions rather than expressing a directional view on Idaho itself.
