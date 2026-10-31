---
signal_id: "CMSIG20261031VS05"
signal_slug: "will-democratic-win-the-house-race-for-f-vol-28371"
headline: "FL-09 Dem House win: 38% on 57% all-time share"
semantic_title: "FL-09 Democratic House bid stays a toss-up under 40%"
telemetry: "38% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T07:49:19+00:00"
event_id: "CM-EVT-DZ1HCD1GF9"
event_slug: "kxhouserace-fl09-26"
event_question: "FL-09 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL09-26-D"
  question_raw: "Will Democratic win the House race for FL-09?"
  current_price: 0.38
  volume_24h_usd: 28371.08
  volume_cumulative_usd: 50062.62
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi marks Democrats at 38% in FL-09, a clear underdog, but not a foregone conclusion."
  - "57% of all-time volume hit in 24h, a dominant single-session share pointing to a contested race entering final hours."
  - "Sub-40% pricing in a district where Democrats are investing signals the GOP structural advantage is holding."
  - "Resolves on FL-09 2026 House election result."
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
      kalshi_vol_24h_usd: 28371.08
sources:
  - label: "ClearMarket market record: FL-09 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-fl09-26"
    retrieved_at: "2026-10-31T07:49:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of all-time volume arriving at a 38% price suggests active two-way positioning, desks should cross-reference with SPIKE 7 (Polymarket FL-09 at 40%) for cross-venue arbitrage reads.
