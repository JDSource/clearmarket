---
signal_id: "CMSIG20261009VS04"
signal_slug: "who-will-win-the-nobel-peace-prize-vol-12645"
headline: "Nobel Peace Prize field alt: 40% on $12.6K volume"
semantic_title: "Traders back a non-Navalnaya Nobel outcome at 40% on Kalshi"
telemetry: "40% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-09T07:49:05+00:00"
event_id: "CM-EVT-2G1CVPVX54"
event_slug: "kxnobelpeace-26"
event_question: "Will the 2026 Nobel Peace Prize be awarded by January 1, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNOBELPEACE-27-MKUL"
  question_raw: "Who will win the Nobel Peace Prize?"
  current_price: 0.4
  volume_24h_usd: 12645.68
  volume_cumulative_usd: 36205.95
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi's alternate Nobel contract prices non-Navalnaya outcomes collectively at 40%, reflecting meaningful residual uncertainty in the field."
  - "35% of all-time volume in 24h, lighter than the 82% spike in Spike 1, but still active given proximity to announcement."
  - "Divergence across Kalshi Nobel contracts implies traders are hedging between Navalnaya and the broader field, not converging on a single name."
  - "Resolves on the 2026 Nobel Peace Prize announcement."
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
      kalshi_vol_24h_usd: 12645.68
sources:
  - label: "ClearMarket market record: Will the 2026 Nobel Peace Prize be awarded by January 1"
    url: "https://clearmarket.fyi/events/kxnobelpeace-26"
    retrieved_at: "2026-10-09T07:49:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous activity in both the Navalnaya-specific and field contracts on Kalshi tells a desk that positioning is split, some capital is hedging the scenario where the Committee surprises with a less-discussed candidate.
