---
signal_id: "CMSIG20260829VS02"
signal_slug: "will-the-federal-reserve-hike-rates-by-vol-33505"
headline: "Fed >25bps Sept hike: 1% on $34K"
semantic_title: "Odds of a Fed hike above 25bps stay near zero on record flow"
telemetry: "1% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-29T13:34:58+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H26"
  question_raw: "Will the Federal Reserve Hike rates by >25bps at their September 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 33505.24
  volume_cumulative_usd: 41737.2
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "1% price means the market treats a jumbo-or-larger September hike as a near-impossibility."
  - "Kalshi records $34K in 24h, a striking 80% of all-time volume, the highest all-time share in this batch."
  - "Surge likely reflects traders closing residual long positions or arbitraging against the companion 25bps contract (Spike 0)."
  - "Resolves on the September 2026 FOMC decision."
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
      kalshi_vol_24h_usd: 33505.24
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-08-29T13:34:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

80% of all-time volume in one session on a 1% contract signals active arbitrage or position cleanup linked to the main Fed hike market, a desk should treat this as a spread-trading signal, not a standalone directional view.
