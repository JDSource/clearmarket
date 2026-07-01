---
signal_id: "CMSIG20260701VS07"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-49494"
headline: "Fed funds above 2.75% post-meeting: 99% on $49K"
semantic_title: "Fed funds upper bound above 2.75% sits near certainty"
telemetry: "99% · $49K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-01T11:21:48+00:00"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Federal funds rate upper bound, July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T2.75"
  question_raw: "Will the upper bound of the federal funds rate be above 2.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.99
  volume_24h_usd: 49494.06
  volume_cumulative_usd: 117696.9
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-29T18:05:00Z"
bullets:
  - "Kalshi at 99%, market treats Fed upper bound remaining above 2.75% as virtually certain."
  - "$49K in 24h is 42% of all-time volume, reflecting active rate-desk hedging into the decision window."
  - "Current Fed funds upper bound well above 2.75% threshold; this contract prices out a dramatic multi-cut scenario."
  - "Near-certain resolution bakes in no emergency easing; residual 1% covers extreme tail-risk hedges."
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
      kalshi_vol_24h_usd: 49494.06
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, July 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26jul"
    retrieved_at: "2026-07-01T11:21:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 99% price with 42% of all-time volume in one session confirms rate desks are using this contract as a near-riskless hedge anchor, signaling consensus that deep Fed cuts to sub-2.75% before the next meeting are not a credible scenario.
