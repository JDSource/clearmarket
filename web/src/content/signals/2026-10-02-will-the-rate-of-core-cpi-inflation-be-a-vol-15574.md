---
signal_id: "CMSIG20261002VS00"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-15574"
headline: "Core CPI above 2.4%: 54% on dominant $15K surge"
semantic_title: "Fresh volume backs core CPI staying above 2.4% through September"
telemetry: "54% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T14:26:08+00:00"
event_id: "CM-EVT-M6P410PY45"
event_slug: "kxcpicoreyoy-26sep"
event_question: "Will core inflation in September 2026 (Core CPI YoY) meet the specified threshold?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26SEP-T2.4"
  question_raw: "Will the rate of core CPI inflation be above 2.4% for the year ending in September 2026?"
  current_price: 0.54
  volume_24h_usd: 15574.78
  volume_cumulative_usd: 23225.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-21T14:00:00Z"
bullets:
  - "Market sits at 54%, treating above-2.4% core CPI for the year ending September as a coin-flip leaning hot."
  - "24h volume of $15.6K is 67% of all-time handle on Kalshi, the bulk of lifetime liquidity arrived today."
  - "October 2 timing points to imminent September CPI print as the catalyst pulling fresh capital in."
  - "Resolves on official BLS release of September year-over-year core CPI; 2.4% is the line."
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
      kalshi_vol_24h_usd: 15574.78
sources:
  - label: "ClearMarket market record: Will core inflation in September 2026 (Core CPI YoY) me"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26sep"
    retrieved_at: "2026-10-02T14:26:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The concentration of nearly all lifetime volume into a single session ahead of the September CPI print signals desks are actively hedging inflation-surprise risk at the 2.4% threshold.
