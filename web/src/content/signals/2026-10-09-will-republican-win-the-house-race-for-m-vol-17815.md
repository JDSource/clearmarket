---
signal_id: "CMSIG20261009VS01"
signal_slug: "will-republican-win-the-house-race-for-m-vol-17815"
headline: "ME-2 Republican win: 67% on $18K inflow"
semantic_title: "ME-2 GOP odds hold near 67% through fresh volume"
telemetry: "67% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-09T14:56:08+00:00"
event_id: "CM-EVT-JWBGQF2D62"
event_slug: "houseme2-26"
event_question: "Will a new representative be elected in Maine's 2nd congressional district?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEME2-26-R"
  question_raw: "Will Republican win the House race for ME-2?"
  current_price: 0.67
  volume_24h_usd: 17815.58
  volume_cumulative_usd: 48465.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi marks GOP at 67% in ME-2, a district that split a presidential ticket as recently as 2020."
  - "37% of all-time volume arrived in 24h, a meaningful but not exhaustive surge, leaving room for further positioning."
  - "ME-2 uses ranked-choice voting, adding resolution complexity that can draw speculative attention near campaign milestones."
  - "Contract resolves on the certified ME-2 House election outcome."
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
      kalshi_vol_24h_usd: 17815.58
sources:
  - label: "ClearMarket market record: Will a new representative be elected in Maine's 2nd con"
    url: "https://clearmarket.fyi/events/houseme2-26"
    retrieved_at: "2026-10-09T14:56:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Renewed interest in ME-2 at a 67% GOP price warrants monitoring for any internal-poll or fundraising release that may have prompted fresh one-sided flow.
