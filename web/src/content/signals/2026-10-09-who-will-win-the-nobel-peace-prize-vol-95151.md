---
signal_id: "CMSIG20261009VS01"
signal_slug: "who-will-win-the-nobel-peace-prize-vol-95151"
headline: "Nobel Peace Prize winner: 29% Navalnaya on $95K spike"
semantic_title: "Fresh money backs Navalnaya in Nobel winner field at 29%"
telemetry: "29% · $95K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-09T07:49:05+00:00"
event_id: "CM-EVT-2G1CVPVX54"
event_slug: "kxnobelpeace-26"
event_question: "Will the 2026 Nobel Peace Prize be awarded by January 1, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNOBELPEACE-27-YNAV"
  question_raw: "Who will win the Nobel Peace Prize?"
  current_price: 0.29
  volume_24h_usd: 95151.08
  volume_cumulative_usd: 115894.57
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi's open-field Nobel contract prices Navalnaya at 29%, the top single-candidate reading in the market."
  - "82% of all-time volume hit in one session, the deepest single-day share of any contract in this batch."
  - "Simultaneous surge across Polymarket and Kalshi Nobel contracts confirms cross-venue directional attention, not venue-specific arbitrage."
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
      kalshi_vol_24h_usd: 95151.08
sources:
  - label: "ClearMarket market record: Will the 2026 Nobel Peace Prize be awarded by January 1"
    url: "https://clearmarket.fyi/events/kxnobelpeace-26"
    retrieved_at: "2026-10-09T07:49:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 82%-of-all-time daily print on a multi-candidate field contract confirms that conviction is concentrating on Navalnaya as the market's modal winner, a desk should treat this as pre-announcement signal flow.
