---
signal_id: "CMSIG20261005VS03"
signal_slug: "will-republican-win-the-house-race-for-c-vol-34028"
headline: "CO-04 Republican win: 68% on $34K surge"
semantic_title: "Heavy trading tests CO-04 Republican odds at 68%"
telemetry: "68% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T16:45:18+00:00"
event_id: "CM-EVT-GZL5K2GKF0"
event_slug: "kxhouserace-co04-26"
event_question: "CO-04 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-CO04-26-R"
  question_raw: "Will Republican win the House race for CO-04?"
  current_price: 0.68
  volume_24h_usd: 34028.55
  volume_cumulative_usd: 51338.91
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican hold in CO-04 at 68%, a solid but not overwhelming favorite."
  - "24h volume equals 66% of all-time handle, the largest all-time share concentration in this batch."
  - "Candidate news or a new poll in Colorado's 4th likely triggered the rush of fresh capital."
  - "Resolves on the CO-04 House general election result."
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
      kalshi_vol_24h_usd: 34028.55
sources:
  - label: "ClearMarket market record: CO-04 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-co04-26"
    retrieved_at: "2026-10-05T16:45:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two-thirds of lifetime volume arriving in one session on a House race is an extreme concentration signal, a desk is making a decisive directional call, possibly on new opposition-research or polling data.
