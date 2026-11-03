---
signal_id: "CMSIG20261103VS03"
signal_slug: "will-republicans-win-the-senate-race-in-vol-934182"
headline: "Michigan GOP Senate: 22% on $934K volume pickup"
semantic_title: "Long-shot GOP Michigan Senate bid draws fresh attention at 22%"
telemetry: "22% · $934K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T15:46:45+00:00"
event_id: "CM-EVT-GBSY094P67"
event_slug: "senatemi-26"
event_question: "Michigan Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMI-26-R"
  question_raw: "Will Republicans win the Senate race in Michigan?"
  current_price: 0.22
  volume_24h_usd: 934182.99
  volume_cumulative_usd: 3651138.35
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 22%, Kalshi traders price Michigan as a Democratic-leaning Senate hold, with Republicans as underdogs."
  - "$934K in 24h equals 26% of all-time volume, a notable session for a race widely seen as secondary."
  - "A 22% Republican price in Michigan reflects renewed but skeptical interest, possibly tied to candidate news or polling shifts."
  - "Resolves on the 2026 Michigan Senate election result."
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
      kalshi_vol_24h_usd: 934182.99
sources:
  - label: "ClearMarket market record: Michigan Senate winner?"
    url: "https://clearmarket.fyi/events/senatemi-26"
    retrieved_at: "2026-11-03T15:46:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume at a 22% price is unusual, a desk should check whether new polling or a candidate announcement triggered the turnover, as attention at this level can precede a price adjustment.
