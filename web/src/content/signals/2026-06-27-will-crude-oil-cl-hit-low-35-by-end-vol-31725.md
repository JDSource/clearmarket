---
signal_id: "CMSIG20260627VS07"
signal_slug: "will-crude-oil-cl-hit-low-35-by-end-vol-31725"
headline: "WTI low $35 by June end: 0% on $32K"
semantic_title: "Crude Oil $35 June low dismissed as an extreme tail scenario"
telemetry: "0% · $32K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T01:36:27+00:00"
event_id: "CM-EVT-648V1NDKW1"
event_slug: "cl-hit-jun-2026"
event_question: "Will Crude Oil (CL) hit (HIGH) $200 by end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x524b6f7e2838e22a90983fc29aeb978983d94818a0f6abd165b9f28524595b97"
  question_raw: "Will Crude Oil (CL) hit (LOW) $35 by end of June?"
  current_price: 0.001
  volume_24h_usd: 31725.326999999997
  volume_cumulative_usd: 121049.00361700002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T18:30:00Z"
bullets:
  - "Zero probability priced, market sees no credible path to crude printing $35 by June 30."
  - "$32K in 24h is 26% of all-time volume, reflecting end-of-month position cleanup."
  - "Current WTI spot is well above $35; reaching that level would require a historic demand shock."
  - "Contract resolves at June month-end, volume is mechanical, not a fresh bearish crude call."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 31725.326999999997
sources:
  - label: "ClearMarket market record: Will Crude Oil (CL) hit (HIGH) $200 by end of June?"
    url: "https://clearmarket.fyi/events/cl-hit-jun-2026"
    retrieved_at: "2026-06-27T01:36:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume surge at zero price is purely expiry-driven and carries no incremental signal for energy desks on near-term crude direction.
