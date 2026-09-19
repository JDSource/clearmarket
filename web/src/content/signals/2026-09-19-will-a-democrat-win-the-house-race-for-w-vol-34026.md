---
signal_id: "CMSIG20260919VS02"
signal_slug: "will-a-democrat-win-the-house-race-for-w-vol-34026"
headline: "Democrat wins WI-3: 72% on $34K inflow"
semantic_title: "Democrats back in the WI-3 House race at 72%"
telemetry: "72% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T12:15:36+00:00"
event_id: "CM-EVT-6C7CNWJ6R7"
event_slug: "housewi3-26"
event_question: "WI-03 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWI3-26-D"
  question_raw: "Will a Democrat win the House race for WI-3?"
  current_price: 0.72
  volume_24h_usd: 34026.08
  volume_cumulative_usd: 82587.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in Wisconsin's 3rd congressional district at 72%, moderate-to-strong lean."
  - "24h volume of $34K is 41% of all-time, signaling a decisive session relative to the contract's history."
  - "WI-3 is a competitive swing seat; fresh volume at this level implies new polling or candidate news driving re-evaluation."
  - "Resolves on 2026 general election results."
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
      kalshi_vol_24h_usd: 34026.08
sources:
  - label: "ClearMarket market record: WI-03 House winner?"
    url: "https://clearmarket.fyi/events/housewi3-26"
    retrieved_at: "2026-09-19T12:15:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 41% all-time share in a single session on a competitive House race signals that new district-level information is moving desks to reprice the Democratic edge meaningfully.
