---
signal_id: "CMSIG20261104VS01"
signal_slug: "will-democrats-hold-218-or-more-seats-in-vol-5910701"
headline: "Dems 218+ House seats: 100% on $5.9M"
semantic_title: "Democrats holding 218+ House seats trades to certainty"
telemetry: "100% · $5.9M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T15:57:35+00:00"
event_id: "CM-EVT-QK0HJYVMX2"
event_slug: "kxbluewavecombo-27feb"
event_question: "Will there be a blue wave in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLUEWAVECOMBO-27FEB"
  question_raw: "Will Democrats hold 218 or more seats in the House after the 2026 midterms AND hold 49 or more seats in the Senate after the 2026 midterms?"
  current_price: 0.996
  volume_24h_usd: 5910701.2
  volume_cumulative_usd: 11146496.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Democratic House majority threshold at 100%, the market has closed on this outcome."
  - "53% of all-time volume, $5.9M, printed in 24h as results sharpen on Election Day."
  - "A 100% price implies call results are already sufficiently clear to erase residual doubt."
  - "Resolves once 218+ Democratic seats are certified in the 120th Congress."
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
      kalshi_vol_24h_usd: 5910701.2
sources:
  - label: "ClearMarket market record: Will there be a blue wave in 2026?"
    url: "https://clearmarket.fyi/events/kxbluewavecombo-27feb"
    retrieved_at: "2026-11-04T15:57:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 100% print on $5.9M of same-day volume signals the desk community is treating Democratic House control as resolved and unwinding hedges in size.
