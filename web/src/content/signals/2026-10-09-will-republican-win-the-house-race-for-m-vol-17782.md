---
signal_id: "CMSIG20261009VS03"
signal_slug: "will-republican-win-the-house-race-for-m-vol-17782"
headline: "Republican ME-2 House: 67% on fresh $17.8K volume"
semantic_title: "Republican ME-2 House odds hold at 67% through renewed trading"
telemetry: "67% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-09T07:49:05+00:00"
event_id: "CM-EVT-JWBGQF2D62"
event_slug: "houseme2-26"
event_question: "Will a new representative be elected in Maine's 2nd congressional district?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEME2-26-R"
  question_raw: "Will Republican win the House race for ME-2?"
  current_price: 0.67
  volume_24h_usd: 17782.01
  volume_cumulative_usd: 48432.35
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices the Republican at 67% in ME-2, the highest win probability in this batch of House races."
  - "24h volume is 37% of all-time, a moderate but notable uptick given the district's competitive history."
  - "ME-2 is a perennial swing seat; renewed volume at 67% suggests traders are backing away from a competitive baseline toward a Republican lean."
  - "Resolves on the certified winner of the Maine 2nd Congressional District race."
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
      kalshi_vol_24h_usd: 17782.01
sources:
  - label: "ClearMarket market record: Will a new representative be elected in Maine's 2nd con"
    url: "https://clearmarket.fyi/events/houseme2-26"
    retrieved_at: "2026-10-09T07:49:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Renewed activity in ME-2 at a 67% Republican price warrants attention from political desks tracking House margin scenarios, as this district has historically been a bellwether for rural swing-state outcomes.
