---
signal_id: "CMSIG20261008VS03"
signal_slug: "will-republican-win-the-house-race-for-t-vol-19949"
headline: "TX-35 GOP win: 40% on $19.9K volume push"
semantic_title: "TX-35 Republican odds draw heavy trading at 40%"
telemetry: "40% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T07:49:04+00:00"
event_id: "CM-EVT-30RGTM2V02"
event_slug: "kxhousetx35-26"
event_question: "Will there be a winner determined in the TX-35 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSETX35-26-R"
  question_raw: "Will Republican win the House race for TX-35?"
  current_price: 0.4
  volume_24h_usd: 19949.92
  volume_cumulative_usd: 33274.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican win in TX-35 at 40%, suggesting a competitive but Democratic-leaning district."
  - "60% of all-time volume, $19.9K, traded in 24 hours, a sharp concentration of activity."
  - "TX-35 has been a battleground target; fresh volume at 40% signals the market sees a genuine contest worth pricing."
  - "Resolves on TX-35 House race result; Republican would need to close a meaningful gap from current odds."
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
      kalshi_vol_24h_usd: 19949.92
sources:
  - label: "ClearMarket market record: Will there be a winner determined in the TX-35 House ra"
    url: "https://clearmarket.fyi/events/kxhousetx35-26"
    retrieved_at: "2026-10-08T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 60% all-time volume share at 40% odds tells desks this is an actively contested race being repriced in real time, worth monitoring as a leading indicator of district-level swing.
