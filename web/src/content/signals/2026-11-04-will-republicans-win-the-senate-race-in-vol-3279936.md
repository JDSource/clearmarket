---
signal_id: "CMSIG20261104VS03"
signal_slug: "will-republicans-win-the-senate-race-in-vol-3279936"
headline: "NE Senate GOP: 99% on $3.3M late confirmation"
semantic_title: "Nebraska Senate GOP stays a near-certainty at 99%"
telemetry: "99% · $3.3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T07:48:42+00:00"
event_id: "CM-EVT-37PJ66HMC4"
event_slug: "senatene-26"
event_question: "Nebraska Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATENE-26-R"
  question_raw: "Will Republicans win the Senate race in Nebraska?"
  current_price: 0.992
  volume_24h_usd: 3279936.91
  volume_cumulative_usd: 7020552.76
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican Nebraska Senate win at 99%, outcome treated as a formality."
  - "47% of all-time volume in 24h points to late-stage position squaring rather than new directional bets."
  - "Nebraska race sees capital inflow consistent with traders closing opposing positions at a loss."
  - "Resolves on certified 2026 Nebraska Senate result."
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
      kalshi_vol_24h_usd: 3279936.91
sources:
  - label: "ClearMarket market record: Nebraska Senate winner?"
    url: "https://clearmarket.fyi/events/senatene-26"
    retrieved_at: "2026-11-04T07:48:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 99% price absorbing nearly half of lifetime volume suggests arb-closing and hedging flows as the market arrives at consensus; desks can treat the Nebraska Republican seat as priced off.
