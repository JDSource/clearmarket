---
signal_id: "CMSIG20260909VS04"
signal_slug: "what-states-will-redistrict-before-the-2-vol-27956"
headline: "2026 Redistricting states: 25% on $28K inflow"
semantic_title: "Redistricting odds sit at 25% as fresh money arrives"
telemetry: "25% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-09T12:40:54+00:00"
event_id: "CM-EVT-L35HG4NH71"
event_slug: "kxredistricting-26"
event_question: "Which states will redistrict before the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXREDISTRICTING-26-MIS"
  question_raw: "What states will redistrict before the 2026 Congressional elections?"
  current_price: 0.25
  volume_24h_usd: 27956.27
  volume_cumulative_usd: 61613.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-01T15:00:00Z"
bullets:
  - "Kalshi prices the redistricting basket at exactly 25%, placing it at the edge of a meaningful threshold."
  - "45% of all-time volume came in over 24h as the 2026 election cycle enters its final pre-election window."
  - "Late-cycle redistricting efforts face steep legal and logistical hurdles; market reflects low but nonzero probability."
  - "Contract resolves based on verified court-approved or legislative redistricting actions before the 2026 election."
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
      kalshi_vol_24h_usd: 27956.27
sources:
  - label: "ClearMarket market record: Which states will redistrict before the midterms?"
    url: "https://clearmarket.fyi/events/kxredistricting-26"
    retrieved_at: "2026-09-09T12:40:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume spike at the 25% threshold signals that desks are actively stress-testing district map assumptions, even a low-probability redistricting event carries outsized downstream impact on multiple House race contracts.
