---
signal_id: "CMSIG20261024VS03"
signal_slug: "will-the-republican-party-hold-exactly-4-vol-11275"
headline: "GOP exactly 47 Senate seats: 15% on $11.3K"
semantic_title: "Republicans holding exactly 47 Senate seats stays unlikely"
telemetry: "15% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-24T12:26:49+00:00"
event_id: "CM-EVT-93ZNVQ37R3"
event_slug: "rsenateseats-27"
event_question: "How many Senate seats will Republicans hold after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "RSENATESEATS-27-E47"
  question_raw: "Will the Republican party hold exactly 47 Senate seats in the 120th Congress?"
  current_price: 0.15
  volume_24h_usd: 11275.97
  volume_cumulative_usd: 42177.74
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices the Republican party finishing the 120th Congress with exactly 47 Senate seats at 15%, a specific count seen as a clear minority outcome."
  - "24h volume of $11.28K is 27% of all-time, a notable single-day share for a precise seat-count contract."
  - "Fresh volume into an exact-number contract one week from Election Day suggests traders are refining seat-by-seat scenario models."
  - "Resolves on certified 120th Congress Senate composition."
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
      kalshi_vol_24h_usd: 11275.97
sources:
  - label: "ClearMarket market record: How many Senate seats will Republicans hold after the m"
    url: "https://clearmarket.fyi/events/rsenateseats-27"
    retrieved_at: "2026-10-24T12:26:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Activity in a precise seat-count contract at 15% indicates desks are mapping the tails of Senate composition scenarios, using exact-number markets to calibrate probability mass around the 47-seat threshold as competitive races approach resolution.
