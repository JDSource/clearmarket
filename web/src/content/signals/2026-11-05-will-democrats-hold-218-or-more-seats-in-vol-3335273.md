---
signal_id: "CMSIG20261105VS02"
signal_slug: "will-democrats-hold-218-or-more-seats-in-vol-3335273"
headline: "Dems 218+ House seats: 99% on $3.3M Election Day bet"
semantic_title: "Traders pile into Democrats holding 218+ House seats at 99%"
telemetry: "99% · $3.3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T07:49:08+00:00"
event_id: "CM-EVT-QK0HJYVMX2"
event_slug: "kxbluewavecombo-27feb"
event_question: "Will there be a blue wave in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLUEWAVECOMBO-27FEB"
  question_raw: "Will Democrats hold 218 or more seats in the House after the 2026 midterms AND hold 49 or more seats in the Senate after the 2026 midterms?"
  current_price: 0.991
  volume_24h_usd: 3335273.38
  volume_cumulative_usd: 12491746.67
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Democrats holding 218 or more seats in the House at 99%, near-certain majority status."
  - "27% of all-time contract volume, $3.3M, executed in one day, reflecting maximum Election Day conviction."
  - "Live House race results rolling in are collapsing uncertainty and crowding capital to the 'yes' side."
  - "Resolves once certified seat totals confirm the 218-seat threshold is met or missed."
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
      kalshi_vol_24h_usd: 3335273.38
sources:
  - label: "ClearMarket market record: Will there be a blue wave in 2026?"
    url: "https://clearmarket.fyi/events/kxbluewavecombo-27feb"
    retrieved_at: "2026-11-05T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 99% price with one-quarter of all-time volume in a single session tells the desk the House majority question is effectively settled by live returns, any position against this faces near-zero implied odds.
