---
signal_id: "CMSIG20260923VS03"
signal_slug: "who-will-win-the-2026-providence-ri-may-vol-51998"
headline: "Providence mayor 2026: 98% on $52K fresh volume"
semantic_title: "Providence mayor race is effectively a settled bet at 98%"
telemetry: "98% · $52K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T07:48:28+00:00"
event_id: "CM-EVT-2T4GQHNZN2"
event_slug: "kxprovidencemayor-26"
event_question: "Will there be a winner of the Providence mayoral election by November 3, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPROVIDENCEMAYOR-26-DMOR"
  question_raw: "Who will win the 2026 Providence, RI mayoral election?"
  current_price: 0.98
  volume_24h_usd: 51998.76
  volume_cumulative_usd: 155308.41
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "At 98%, Kalshi has the leading candidate as a near-certain winner of the 2026 Providence mayoral election."
  - "24h volume of $52K is 33% of all-time, a significant one-day commitment on an already-resolved-looking race."
  - "Volume at 98% odds suggests either late liquidity provision or a sharp move following a decisive primary or poll result."
  - "Contract resolves on the certified result of the 2026 Providence, RI mayoral election."
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
      kalshi_vol_24h_usd: 51998.76
sources:
  - label: "ClearMarket market record: Will there be a winner of the Providence mayoral electi"
    url: "https://clearmarket.fyi/events/kxprovidencemayor-26"
    retrieved_at: "2026-09-23T07:48:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk can treat this as a near-closed contract; the volume at 98% is likely market-makers clearing inventory rather than speculative positioning, but confirmation of the catalyst driving finality is worth noting.
