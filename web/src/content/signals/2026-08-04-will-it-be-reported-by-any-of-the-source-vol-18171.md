---
signal_id: "CMSIG20260804VS06"
signal_slug: "will-it-be-reported-by-any-of-the-source-vol-18171"
headline: "Senate Judiciary Cmte action: 97% on $18K volume"
semantic_title: "Senate Judiciary Committee action odds hold firm near certainty"
telemetry: "97% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-04T10:33:57+00:00"
event_id: "CM-EVT-5ZY4R2CPG9"
event_slug: "kxblanchejudiciary-27"
event_question: "Will Todd Blanche's Attorney General nomination advance from committee?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLANCHEJUDICIARY-27-26OCT01"
  question_raw: "Will it be reported by any of the Source Agencies that the Senate Judiciary Committee reports Todd Blanche's nomination to be U.S. Attorney General to the full Senate before Oct 1, 2026?"
  current_price: 0.97
  volume_24h_usd: 18171.68
  volume_cumulative_usd: 64219.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-08T14:00:00Z"
bullets:
  - "At 97%, Kalshi treats a reported Senate Judiciary Committee action as all but certain."
  - "24h volume of $18K is 28% of all-time, a meaningful inflow with resolution likely close."
  - "Volume near a 97% ceiling typically reflects last-mile positioning as a resolution event becomes imminent."
  - "Resolves on sourced reporting from designated agencies confirming the committee action."
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
      kalshi_vol_24h_usd: 18171.68
sources:
  - label: "ClearMarket market record: Will Todd Blanche's Attorney General nomination advance"
    url: "https://clearmarket.fyi/events/kxblanchejudiciary-27"
    retrieved_at: "2026-08-04T10:33:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 97% contract drawing 28% of lifetime volume in one session signals that resolution is likely hours or days away, a desk should flag this as a near-term confirmation event for related legislative or legal positioning.
