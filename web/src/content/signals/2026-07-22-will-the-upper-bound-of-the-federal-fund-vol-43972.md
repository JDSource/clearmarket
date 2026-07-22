---
signal_id: "CMSIG20260722VS02"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-43972"
headline: "Fed funds above 3.75%: 15% on $44K inflow"
semantic_title: "Traders push back on the fed funds rate staying above 3.75%"
telemetry: "15% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-22T10:22:39+00:00"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Federal funds rate upper bound, July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.15
  volume_24h_usd: 43972.99
  volume_cumulative_usd: 153668.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi puts the odds of the upper bound remaining above 3.75% at just 15%, cuts are the base case."
  - "24h volume of $44K is 29% of all-time, the largest single-day print on this longer-horizon contract."
  - "Fresh activity ahead of the July FOMC meeting suggests traders are repricing the easing path lower."
  - "Resolves on the Fed's published upper-bound target following the relevant policy decision."
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
      kalshi_vol_24h_usd: 43972.99
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, July 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26jul"
    retrieved_at: "2026-07-22T10:22:39+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 15% price with a significant volume spike on the 'above 3.75%' contract tells a desk the market is actively building positions around an aggressive cutting cycle, worth monitoring against rates derivatives.
