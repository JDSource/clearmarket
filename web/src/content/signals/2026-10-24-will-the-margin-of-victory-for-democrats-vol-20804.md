---
signal_id: "CMSIG20261024VS02"
signal_slug: "will-the-margin-of-victory-for-democrats-vol-20804"
headline: "GA Senate Dem margin win: 92% on $20.8K"
semantic_title: "Democrats heavily favored to win Georgia Senate race"
telemetry: "92% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-24T07:48:55+00:00"
event_id: "CM-EVT-3295WZKLQ3"
event_slug: "kxmidtermmov-gasend"
event_question: "Will the Georgia Senate election margin of victory be less than 5 percentage points?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMMOV-GASEND-P2"
  question_raw: "Will the margin of victory for Democrats in the U.S. Senate election in Georgia be at least 2 percentage points?"
  current_price: 0.915
  volume_24h_usd: 20804.64
  volume_cumulative_usd: 29427.86
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic victory margin in Georgia's U.S. Senate race at 92%, strong consensus around the outcome."
  - "24h volume of $20.8K represents 71% of the contract's entire all-time volume, a near-total liquidity event."
  - "Late-cycle concentration of volume at a high price signals conviction traders are locking in positions ahead of results."
  - "Resolves on certified Georgia Senate election results."
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
      kalshi_vol_24h_usd: 20804.64
sources:
  - label: "ClearMarket market record: Will the Georgia Senate election margin of victory be l"
    url: "https://clearmarket.fyi/events/kxmidtermmov-gasend"
    retrieved_at: "2026-10-24T07:48:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 71% all-time volume share in one session at 92% pricing tells desks this contract is reaching terminal consensus, most two-sided price discovery is effectively over.
