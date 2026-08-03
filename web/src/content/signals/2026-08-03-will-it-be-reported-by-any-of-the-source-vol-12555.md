---
signal_id: "CMSIG20260803VS03"
signal_slug: "will-it-be-reported-by-any-of-the-source-vol-12555"
headline: "Senate Judiciary Cmte action: 92% on $13K surge"
semantic_title: "Senate Judiciary Committee action odds hold near 92%"
telemetry: "92% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-03T11:19:10+00:00"
event_id: "CM-EVT-5ZY4R2CPG9"
event_slug: "kxblanchejudiciary-27"
event_question: "Will Todd Blanche's Attorney General nomination advance from committee?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLANCHEJUDICIARY-27-26OCT01"
  question_raw: "Will it be reported by any of the Source Agencies that the Senate Judiciary Committee reports Todd Blanche's nomination to be U.S. Attorney General to the full Senate before Oct 1, 2026?"
  current_price: 0.92
  volume_24h_usd: 12555.92
  volume_cumulative_usd: 43673.83
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-08T14:00:00Z"
bullets:
  - "At 92%, the market prices Senate Judiciary Committee action as nearly assured within the resolution window."
  - "$12.6K traded in 24h is 29% of all-time volume, a sharp single-session burst."
  - "Volume at this late-stage probability typically reflects traders locking in near-certain gains or hedging residual tail risk."
  - "Resolves on a qualifying report from designated source agencies on Committee activity."
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
      kalshi_vol_24h_usd: 12555.92
sources:
  - label: "ClearMarket market record: Will Todd Blanche's Attorney General nomination advance"
    url: "https://clearmarket.fyi/events/kxblanchejudiciary-27"
    retrieved_at: "2026-08-03T11:19:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-conviction volume at 92% suggests a catalyst, likely a scheduled hearing or markup, is now confirmed, and desks are closing out or topping off positions ahead of near-certain resolution.
