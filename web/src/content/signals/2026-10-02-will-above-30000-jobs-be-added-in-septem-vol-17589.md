---
signal_id: "CMSIG20261002VS02"
signal_slug: "will-above-30000-jobs-be-added-in-septem-vol-17589"
headline: "30K+ Sept jobs added: 76% on $18K surge"
semantic_title: "Buyers back 30K+ September payrolls at 76%"
telemetry: "76% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T07:48:52+00:00"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "Will the September 2026 jobs report show positive job growth?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T30000"
  question_raw: "Will above 30000 jobs be added in September 2026?"
  current_price: 0.76
  volume_24h_usd: 17589.11
  volume_cumulative_usd: 29072.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "76% price reflects meaningful but not overwhelming confidence that payrolls exceed the 30K threshold in September."
  - "61% of all-time volume arrived in a single session, the sharpest concentration of any contract in this batch."
  - "A 30K hurdle is low by historical standards, suggesting the volume reflects hedging against a near-recessionary miss rather than bullish positioning."
  - "Resolves on BLS nonfarm payrolls for September 2026."
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
      kalshi_vol_24h_usd: 17589.11
sources:
  - label: "ClearMarket market record: Will the September 2026 jobs report show positive job g"
    url: "https://clearmarket.fyi/events/kxpayrolls-26sep"
    retrieved_at: "2026-10-02T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The fact that three-quarters of the market still expects even a modest 30K print, combined with a volume spike, flags pre-report tail-risk hedging on a potential soft payrolls number a desk should monitor.
