---
signal_id: "CMSIG20260828VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-vol-55695"
headline: "Fed Sept hike >25bps: 2% on $56K volume"
semantic_title: "Fed hike above 25bps in September stays a long shot at 2%"
telemetry: "2% · $56K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-28T19:52:39+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H26"
  question_raw: "Will the Federal Reserve Hike rates by >25bps at their September 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 55695.81
  volume_cumulative_usd: 72153.48
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "2% price reflects near-universal market consensus that the Fed holds or cuts in September 2026."
  - "77% of all-time volume arrived today, suggesting a macro catalyst reignited attention without moving the needle."
  - "Possible trigger: fresh labor or inflation data that traders checked, and dismissed, as insufficient for a hike."
  - "Resolves on the FOMC September 2026 rate decision."
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
      kalshi_vol_24h_usd: 55695.81
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-08-28T19:52:39+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume at 2% with no price lift is a strong signal the market is confidently fading any hike narrative, rates desks can treat a >25bps September move as effectively priced out.
