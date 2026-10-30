---
signal_id: "CMSIG20261030VS05"
signal_slug: "will-the-margin-of-victory-for-democrats-vol-30560"
headline: "NC Senate Dem margin: 98% on $31K spike"
semantic_title: "Traders back a wide Democrat margin in NC Senate at 98%"
telemetry: "98% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T07:48:50+00:00"
event_id: "CM-EVT-22Y3TGXT19"
event_slug: "kxmidtermmov-ncsend"
event_question: "Will the North Carolina Senate margin of victory be less than 5 percentage points?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMMOV-NCSEND-P1"
  question_raw: "Will the margin of victory for Democrats in the U.S. Senate election in North Carolina be at least 1 percentage points?"
  current_price: 0.978
  volume_24h_usd: 30560.7
  volume_cumulative_usd: 41386.7
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Democrats winning the North Carolina Senate race by the specified margin at 98%, near-certain."
  - "24h volume of $31K is 74% of all-time $41K; contract is almost entirely a single-day event."
  - "98% pricing with a fresh-volume surge implies any residual uncertainty is being priced out by the market."
  - "Resolves on the certified Democratic margin of victory in the NC U.S. Senate election."
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
      kalshi_vol_24h_usd: 30560.7
sources:
  - label: "ClearMarket market record: Will the North Carolina Senate margin of victory be les"
    url: "https://clearmarket.fyi/events/kxmidtermmov-ncsend"
    retrieved_at: "2026-10-30T07:48:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Overwhelming volume on a 98% line this late in the cycle tells desks the market has fully digested the NC Senate outcome and is simply settling remaining open interest.
