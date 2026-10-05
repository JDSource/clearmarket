---
signal_id: "CMSIG20261005VS03"
signal_slug: "will-the-republican-party-hold-exactly-4-vol-14461"
headline: "GOP exactly 48 seats: 18% on $14K, 53% of all-time vol"
semantic_title: "Odds stay low on Republicans landing at exactly 48 Senate seats"
telemetry: "18% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T07:48:02+00:00"
event_id: "CM-EVT-93ZNVQ37R3"
event_slug: "rsenateseats-27"
event_question: "How many Senate seats will Republicans hold after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "RSENATESEATS-27-E48"
  question_raw: "Will the Republican party hold exactly 48 Senate seats in the 120th Congress?"
  current_price: 0.18
  volume_24h_usd: 14461.33
  volume_cumulative_usd: 27366.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices the exact-48-seat outcome at 18%, the market judges this precise count more likely than a coin flip but well short of probable."
  - "53% of all-time volume transacted in one day, making this the contract's defining session."
  - "Exact-seat contracts are highly sensitive to late-race swings in two or three toss-up states simultaneously."
  - "Resolves after the 120th Congress is certified; precision of the target makes this inherently low-probability."
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
      kalshi_vol_24h_usd: 14461.33
sources:
  - label: "ClearMarket market record: How many Senate seats will Republicans hold after the m"
    url: "https://clearmarket.fyi/events/rsenateseats-27"
    retrieved_at: "2026-10-05T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk running Senate seat-count scenarios should note that volume concentration at 18% on the exact-48 outcome reflects active use of granular congressional contracts for tail-risk structuring, not just directional bets.
