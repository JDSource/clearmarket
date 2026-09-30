---
signal_id: "CMSIG20260930VS05"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-22173"
headline: "Fed funds above 4%: 34% on $22K spike"
semantic_title: "Fed funds staying above 4.00% after October draws fresh bets"
telemetry: "34% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T14:33:50+00:00"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds rate upper bound, October 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 22173.9
  volume_cumulative_usd: 47691.33
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi prices the upper bound of fed funds above 4.00% post-meeting at 34%, meaningful residual risk."
  - "24h volume of $22K is 46% of all-time, marking the most active single session on this contract."
  - "Contract directly tracks the rate-level outcome and complements the hike/hold contracts trading simultaneously."
  - "Resolves following the October 2026 FOMC meeting announcement."
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
      kalshi_vol_24h_usd: 22173.9
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, October 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26oct"
    retrieved_at: "2026-09-30T14:33:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 46% all-time volume share on the rate-level contract, alongside the hike/hold spikes, tells desks that traders are building layered rate-path hedges across multiple Kalshi instruments simultaneously.
