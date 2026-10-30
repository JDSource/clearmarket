---
signal_id: "CMSIG20261030VS06"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-77542"
headline: "Dem NC-11 Kalshi: 86% on $78K volume"
semantic_title: "Fresh volume backs the Democratic NC-11 win on Kalshi"
telemetry: "86% · $78K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T14:48:27+00:00"
event_id: "CM-EVT-0N8GC3M3K5"
event_slug: "kxhousenc11-26"
event_question: "Who will win the North Carolina 11th congressional district House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSENC11-26-DEM"
  question_raw: "Will Democratic win the House race for NC-11?"
  current_price: 0.86
  volume_24h_usd: 77542.5
  volume_cumulative_usd: 268175.96
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "86% on Kalshi aligns with Polymarket's read (Spike 2), confirming cross-venue Democratic consensus on NC-11."
  - "$78K in 24h is 29% of all-time volume, a meaningful but not climactic single-session share."
  - "Cross-venue price agreement at 86% reduces arbitrage opportunity and strengthens signal reliability."
  - "Resolves on NC-11 certified House election result."
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
      kalshi_vol_24h_usd: 77542.5
sources:
  - label: "ClearMarket market record: Who will win the North Carolina 11th congressional dist"
    url: "https://clearmarket.fyi/events/kxhousenc11-26"
    retrieved_at: "2026-10-30T14:48:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Matching 86% prices across two venues with independent volume spikes on the same NC-11 Democratic contract is strong evidence the market has reached a stable conviction level with no meaningful disagreement.
