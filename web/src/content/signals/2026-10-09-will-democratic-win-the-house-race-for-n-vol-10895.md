---
signal_id: "CMSIG20261009VS02"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-10895"
headline: "NY-21 Dem win: 28% on $11K volume spike"
semantic_title: "Democratic bid for NY-21 priced as a long shot at 28%"
telemetry: "28% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-09T14:56:08+00:00"
event_id: "CM-EVT-H11V46ZQN5"
event_slug: "kxhouserace-ny21-26"
event_question: "Will the winner of the New York's 21st Congressional District House election be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-NY21-26-D"
  question_raw: "Will Democratic win the House race for NY-21?"
  current_price: 0.28
  volume_24h_usd: 10895.54
  volume_cumulative_usd: 22504.43
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in NY-21 at 28%, the market treats this as a Republican-leaning seat."
  - "48% of all-time contract volume cleared in 24h, suggesting a sharp catalyst pulled fresh money to both sides."
  - "NY-21 was flipped red in 2022 and has trended competitive; a polling release or candidate event could explain the attention spike."
  - "Resolves on the certified NY-21 House general election result."
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
      kalshi_vol_24h_usd: 10895.54
sources:
  - label: "ClearMarket market record: Will the winner of the New York's 21st Congressional Di"
    url: "https://clearmarket.fyi/events/kxhouserace-ny21-26"
    retrieved_at: "2026-10-09T14:56:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half the contract's lifetime volume arriving in a single session at a 28% Democratic price signals that some participants see underpriced upside, desks should watch for a catalyst that justifies the sudden interest.
