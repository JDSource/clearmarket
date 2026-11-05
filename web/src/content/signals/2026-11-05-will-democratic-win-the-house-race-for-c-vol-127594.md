---
signal_id: "CMSIG20261105VS04"
signal_slug: "will-democratic-win-the-house-race-for-c-vol-127594"
headline: "CO-04 House Dem: 94% on $128K Election Day flow"
semantic_title: "Democrats near-certain in CO-04 House race at 94%"
telemetry: "94% · $128K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T16:03:26+00:00"
event_id: "CM-EVT-GZL5K2GKF0"
event_slug: "kxhouserace-co04-26"
event_question: "CO-04 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-CO04-26-D"
  question_raw: "Will Democratic win the House race for CO-04?"
  current_price: 0.935
  volume_24h_usd: 127594.86
  volume_cumulative_usd: 388528.45
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Market prices a Democratic CO-04 House win at 94%, high-conviction hold."
  - "$128K in 24h is 33% of all-time; meaningful Election Day rotation into the contract."
  - "Colorado's 4th district result feeds directly into House majority running tallies."
  - "Kalshi contract resolves on certified winner; same-day returns may close it out quickly."
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
      kalshi_vol_24h_usd: 127594.86
sources:
  - label: "ClearMarket market record: CO-04 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-co04-26"
    retrieved_at: "2026-11-05T16:03:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Steady Election Day volume into a high-probability Democratic hold suggests traders are updating House seat-count models in real time and treating CO-04 as a confirmed blue tally.
