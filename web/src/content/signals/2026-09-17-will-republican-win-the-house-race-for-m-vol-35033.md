---
signal_id: "CMSIG20260917VS04"
signal_slug: "will-republican-win-the-house-race-for-m-vol-35033"
headline: "GOP MT-1 House: 68% on $35K; 82% all-time"
semantic_title: "Republicans back in MT-1 at 68% as volume floods in"
telemetry: "68% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-17T13:05:20+00:00"
event_id: "CM-EVT-QWGZDJ1DQ6"
event_slug: "housemt1-26"
event_question: "MT-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEMT1-26-R"
  question_raw: "Will Republican win the House race for MT-1?"
  current_price: 0.68
  volume_24h_usd: 35033.22
  volume_cumulative_usd: 42843.51
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 68% to win Montana's 1st Congressional District."
  - "$35K in 24h represents 82% of all-time contract volume, nearly the entire history traded today."
  - "MT-1 has drawn attention as a potential Democratic pickup opportunity in a competitive House map."
  - "Resolves on November 2026 election night."
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
      kalshi_vol_24h_usd: 35033.22
sources:
  - label: "ClearMarket market record: MT-01 House winner?"
    url: "https://clearmarket.fyi/events/housemt1-26"
    retrieved_at: "2026-09-17T13:05:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 82% all-time volume share in a single session signals a sharp reappraisal of MT-1's competitiveness, desks tracking House majority scenarios should update their MT-1 assumptions.
