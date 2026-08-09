---
signal_id: "CMSIG20260809VS07"
signal_slug: "will-average-gas-prices-be-above-4-vol-10112"
headline: "Gas above $4.000: 82% on $10K volume"
semantic_title: "Gas above $4.00 stays a live bet at 82%"
telemetry: "82% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-09T08:37:25+00:00"
event_id: "CM-EVT-FCL1JMT0V9"
event_slug: "kxaaagasw-26aug10"
event_question: "AAA national average gas price, August 17, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASW-26AUG10-4.000"
  question_raw: "Will average **gas prices** be above $4.000?"
  current_price: 0.82
  volume_24h_usd: 10112.64
  volume_cumulative_usd: 33282.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-17T14:00:00Z"
bullets:
  - "Kalshi prices average gas above $4.00 at 82%, elevated conviction but with meaningful residual doubt at the round-dollar threshold."
  - "24h volume of $10K is 30% of a $33K all-time pool, indicating a notable but not dominant single-day draw."
  - "The 18% against-probability at a psychologically significant level suggests traders are hedging against a sub-$4.00 average reading."
  - "Contract resolves against the same gas price benchmark as the $3.980 contract, one tick higher."
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
      kalshi_vol_24h_usd: 10112.64
sources:
  - label: "ClearMarket market record: AAA national average gas price, August 17, 2026"
    url: "https://clearmarket.fyi/events/kxaaagasw-26aug10"
    retrieved_at: "2026-08-09T08:37:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 82% reading at the $4.00 level with fresh volume tells a desk there is a live 18-cent gap risk being actively hedged, pair with the $3.98 contract for a refined view of the distribution around the round-dollar mark.
