---
signal_id: "CMSIG20261105VS05"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-72334"
headline: "Fed rate above 4%: 65% on $72K policy-bet spike"
semantic_title: "Fed funds above 4% after next meeting stays likely at 65%"
telemetry: "65% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T16:03:26+00:00"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound, December 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.65
  volume_24h_usd: 72334.73
  volume_cumulative_usd: 154169.05
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Market prices a 65% chance the federal funds rate upper bound stays above 4.00% post-meeting."
  - "$72K in 24h is 47% of all-time, nearly half of all trading compressed into one session."
  - "Election Day macro uncertainty and any surprise economic data are driving rates re-pricing."
  - "Kalshi contract resolves after the Fed's next scheduled policy decision."
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
      kalshi_vol_24h_usd: 72334.73
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, December 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26dec"
    retrieved_at: "2026-11-05T16:03:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume arriving in a single session signals that rates traders are actively repricing the Fed's near-term path, this contract is worth watching as an Election Day macro read on 2026 policy expectations.
