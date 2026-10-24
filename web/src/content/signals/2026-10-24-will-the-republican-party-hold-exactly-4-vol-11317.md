---
signal_id: "CMSIG20261024VS03"
signal_slug: "will-the-republican-party-hold-exactly-4-vol-11317"
headline: "GOP holds exactly 47 seats: 15% on $11.3K"
semantic_title: "Traders back 47-seat Republican Senate scenario at 15%"
telemetry: "15% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-24T07:48:55+00:00"
event_id: "CM-EVT-93ZNVQ37R3"
event_slug: "rsenateseats-27"
event_question: "How many Senate seats will Republicans hold after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "RSENATESEATS-27-E47"
  question_raw: "Will the Republican party hold exactly 47 Senate seats in the 120th Congress?"
  current_price: 0.15
  volume_24h_usd: 11317.74
  volume_cumulative_usd: 42177.74
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Republicans finishing the 120th Congress at exactly 47 Senate seats at 15%, a live but minority scenario."
  - "$11.3K in 24h volume is 27% of all-time handle, a meaningful liquidity uptick for a precise seat-count contract."
  - "Exact seat-count markets attract sharp late money as state-level races clarify; attention here implies Georgia and other toss-ups are in focus."
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
      kalshi_vol_24h_usd: 11317.74
sources:
  - label: "ClearMarket market record: How many Senate seats will Republicans hold after the m"
    url: "https://clearmarket.fyi/events/rsenateseats-27"
    retrieved_at: "2026-10-24T07:48:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a specific seat-count outcome at 15% signals desks are stress-testing Senate composition scenarios as final races approach resolution.
