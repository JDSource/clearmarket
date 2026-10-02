---
signal_id: "CMSIG20261002VS03"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-15257"
headline: "Core CPI above 2.4% yr/yr: 53% on $15K surge"
semantic_title: "Core CPI above 2.4% for the year ending September sits near a coin flip"
telemetry: "53% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T07:48:52+00:00"
event_id: "CM-EVT-M6P410PY45"
event_slug: "kxcpicoreyoy-26sep"
event_question: "Will core inflation in September 2026 (Core CPI YoY) meet the specified threshold?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26SEP-T2.4"
  question_raw: "Will the rate of core CPI inflation be above 2.4% for the year ending in September 2026?"
  current_price: 0.53
  volume_24h_usd: 15257.55
  volume_cumulative_usd: 22766.47
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-21T14:00:00Z"
bullets:
  - "53% price is essentially a toss-up, with the market split on whether core inflation holds above 2.4% for the year ending September."
  - "$15K in 24h represents 67% of all-time handle, the highest lifetime-share ratio in this batch, indicating this market was dormant until now."
  - "Sudden attention at near-50% odds suggests the September CPI release is live for Fed policy signaling."
  - "Resolves on BLS core CPI for the 12 months ending September 2026."
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
      kalshi_vol_24h_usd: 15257.55
sources:
  - label: "ClearMarket market record: Will core inflation in September 2026 (Core CPI YoY) me"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26sep"
    retrieved_at: "2026-10-02T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-50-50 core CPI contract drawing two-thirds of its lifetime volume in one day signals genuine uncertainty about the inflation path and warrants close attention for rate-cut timing models.
