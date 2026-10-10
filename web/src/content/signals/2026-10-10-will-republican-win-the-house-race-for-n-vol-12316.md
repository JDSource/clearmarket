---
signal_id: "CMSIG20261010VS06"
signal_slug: "will-republican-win-the-house-race-for-n-vol-12316"
headline: "NC-11 GOP House: 24% on $12K volume"
semantic_title: "Republicans trade near a long shot in NC-11 at 24%"
telemetry: "24% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T07:48:40+00:00"
event_id: "CM-EVT-0N8GC3M3K5"
event_slug: "kxhousenc11-26"
event_question: "Who will win the North Carolina 11th congressional district House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSENC11-26-GOP"
  question_raw: "Will Republican win the House race for NC-11?"
  current_price: 0.24
  volume_24h_usd: 12316.73
  volume_cumulative_usd: 30317.73
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican win in NC-11 at 24%, market assigns clear underdog status to the GOP here."
  - "41% of all-time volume, $12K, hit in one day, a notable concentration of activity for a single House race."
  - "NC-11 at 24% Republican reflects either a strong Democratic incumbent advantage or a recent structural shift in the district."
  - "Resolves on 2026 NC-11 House election result."
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
      kalshi_vol_24h_usd: 12316.73
sources:
  - label: "ClearMarket market record: Who will win the North Carolina 11th congressional dist"
    url: "https://clearmarket.fyi/events/kxhousenc11-26"
    retrieved_at: "2026-10-10T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume at 24% on the Republican side in NC-11 suggests market participants are actively re-evaluating whether the district presents a late-cycle opportunity; a desk should track any candidate or redistricting developments.
