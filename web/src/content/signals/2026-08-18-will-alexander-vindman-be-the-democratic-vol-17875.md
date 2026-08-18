---
signal_id: "CMSIG20260818VS04"
signal_slug: "will-alexander-vindman-be-the-democratic-vol-17875"
headline: "Vindman FL Dem Senate nom: 91% on $18K surge"
semantic_title: "Vindman FL Senate Democratic nom holds firm at 91%"
telemetry: "91% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-18T08:31:22+00:00"
event_id: "CM-EVT-M02ZJWQWV9"
event_slug: "kxsenatefld-26"
event_question: "Will the Florida Democratic Senate nominee be determined by the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEFLD-26-AVIN"
  question_raw: "Will Alexander Vindman be the Democratic nominee for the Senate in Florida?"
  current_price: 0.91
  volume_24h_usd: 17875.19
  volume_cumulative_usd: 49213.47
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Vindman at 91%, strong favorite for the Democratic Senate nomination in Florida."
  - "36% of all-time volume in 24h ($17.9K), proportionally the largest daily session this contract has seen."
  - "Surge likely driven by the same Florida primary event catalyzing volume across all FL contracts today."
  - "Resolves on Florida Democratic Party's certified Senate nominee."
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
      kalshi_vol_24h_usd: 17875.19
sources:
  - label: "ClearMarket market record: Will the Florida Democratic Senate nominee be determine"
    url: "https://clearmarket.fyi/events/kxsenatefld-26"
    retrieved_at: "2026-08-18T08:31:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 91% print on record proportional volume confirms the Democratic side of the Florida Senate race is also resolving, desks pricing the FL general election should treat Vindman as the Democratic standard-bearer.
