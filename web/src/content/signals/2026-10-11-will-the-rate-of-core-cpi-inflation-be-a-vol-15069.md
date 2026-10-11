---
signal_id: "CMSIG20261011VS07"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-15069"
headline: "Core CPI above 2.1% Sep YoY: 99% on $15K"
semantic_title: "Core CPI above 2.1% for the year ending September is a near-certainty"
telemetry: "99% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T07:48:50+00:00"
event_id: "CM-EVT-M6P410PY45"
event_slug: "kxcpicoreyoy-26sep"
event_question: "Will core inflation in September 2026 (Core CPI YoY) meet the specified threshold?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26SEP-T2.1"
  question_raw: "Will the rate of core CPI inflation be above 2.1% for the year ending in September 2026?"
  current_price: 0.99
  volume_24h_usd: 15069.8
  volume_cumulative_usd: 27860.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-21T14:00:00Z"
bullets:
  - "Kalshi prices core CPI exceeding 2.1% for the year ending September 2026 at 99%, essentially resolved in the market's view."
  - "54% of all-time volume on this contract placed in 24h, reflecting renewed macro positioning."
  - "A 99% price with fresh volume implies traders are using this contract as a macro hedge or collateral reference ahead of the September CPI print."
  - "Resolves on BLS September 2026 CPI release."
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
      kalshi_vol_24h_usd: 15069.8
sources:
  - label: "ClearMarket market record: Will core inflation in September 2026 (Core CPI YoY) me"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26sep"
    retrieved_at: "2026-10-11T07:48:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

99% pricing with over half of all-time volume in one day signals the desk that this contract is functioning as a macro hedge vehicle, not a price-discovery instrument, relevant for rates positioning ahead of the September print.
