---
signal_id: "CMSIG20261011VS03"
signal_slug: "will-republican-win-the-house-race-for-m-vol-48767"
headline: "MT-1 GOP House win: 74% on $49K surge"
semantic_title: "Buyers back the GOP in Montana's MT-1 House race at 74%"
telemetry: "74% · $49K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T14:36:40+00:00"
event_id: "CM-EVT-QWGZDJ1DQ6"
event_slug: "housemt1-26"
event_question: "MT-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEMT1-26-R"
  question_raw: "Will Republican win the House race for MT-1?"
  current_price: 0.74
  volume_24h_usd: 48767.84
  volume_cumulative_usd: 166133.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican win in Montana's MT-1 district at 74%, a solid but not locked favourite."
  - "29% of all-time volume arrived in 24 hours, meaningful fresh capital into a competitive district."
  - "MT-1 has emerged as a bellwether swing district; elevated volume signals traders see resolution risk rising."
  - "Resolves after 2026 MT-1 House race results are certified."
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
      kalshi_vol_24h_usd: 48767.84
sources:
  - label: "ClearMarket market record: MT-01 House winner?"
    url: "https://clearmarket.fyi/events/housemt1-26"
    retrieved_at: "2026-10-11T14:36:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a 74% GOP line on a competitive House seat signals desks are treating MT-1 as a live swing race worth hedging, not a foregone conclusion.
