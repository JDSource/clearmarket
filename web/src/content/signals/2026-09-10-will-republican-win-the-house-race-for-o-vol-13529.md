---
signal_id: "CMSIG20260910VS05"
signal_slug: "will-republican-win-the-house-race-for-o-vol-13529"
headline: "OH-10 GOP House: 84% on $14K inflow"
semantic_title: "OH-10 Republican House seat holds at 84% through fresh volume"
telemetry: "84% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-10T12:40:48+00:00"
event_id: "CM-EVT-TY2DWD9XJ0"
event_slug: "kxhouserace-oh10-26"
event_question: "OH-10 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-OH10-26-R"
  question_raw: "Will Republican win the House race for OH-10?"
  current_price: 0.84
  volume_24h_usd: 13529.88
  volume_cumulative_usd: 29765.2
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi holds the Republican candidate at 84% in OH-10, consistent with a safe-lean Republican read."
  - "45% of all-time volume arrived in a single 24-hour window, a sharp acceleration in market attention."
  - "Parallel movement with MN-01 at the same 84% level suggests systematic House race repricing, not isolated news."
  - "Resolves on the 2026 OH-10 House election."
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
      kalshi_vol_24h_usd: 13529.88
sources:
  - label: "ClearMarket market record: OH-10 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-oh10-26"
    retrieved_at: "2026-09-10T12:40:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 45% all-time share in one session alongside a matching MN-01 move indicates coordinated House map activity, desks modeling 2026 majority math should note both seats being firmed up simultaneously.
