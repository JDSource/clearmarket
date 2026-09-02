---
signal_id: "CMSIG20260902VS06"
signal_slug: "will-the-federal-reserve-hike-rates-by-vol-21945"
headline: "Fed hike >25bps in Sept: 1% on $22K volume"
semantic_title: "A September Fed hike stays a long shot at 1%"
telemetry: "1% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-02T12:29:56+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H26"
  question_raw: "Will the Federal Reserve Hike rates by >25bps at their September 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 21945.25
  volume_cumulative_usd: 66673.09
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi prices the probability of a Fed rate hike of more than 25bps in September 2026 at just 1%, effectively ruled out."
  - "$22K in 24h is 33% of all-time, a moderate session that likely reflects traders closing residual long positions."
  - "Paired with the above-3.50% contract pricing at 98%, the market is fully aligned: rates hold, no hike."
  - "Resolves YES only if the September 2026 FOMC decision includes a hike exceeding 25 basis points."
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
      kalshi_vol_24h_usd: 21945.25
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-09-02T12:29:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 1% with modest but real volume, this contract is telling desks the market has no credible hike scenario priced; any flow here is likely hedging tail risk rather than expressing a directional view.
