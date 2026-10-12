---
signal_id: "CMSIG20261012VS00"
signal_slug: "will-cpi-rise-more-than-0-2-in-septembe-vol-29996"
headline: "Sept CPI >0.2%: 99% on $30K surge"
semantic_title: "September CPI above 0.2% holds near certainty"
telemetry: "99% · $30K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-12T17:18:20+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.2"
  question_raw: "Will CPI rise more than 0.2% in September 2026?"
  current_price: 0.99
  volume_24h_usd: 29996.3
  volume_cumulative_usd: 58504.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Kalshi prices a September CPI beat above 0.2% at 99%, near-certain outcome."
  - "24h volume of $30K is 51% of all-time handle, signaling a decisive late-stage consensus push."
  - "October 12 timing aligns with imminent BLS release, drawing last-minute positioning."
  - "Resolves on official September CPI print; near-zero residual uncertainty priced in."
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
      kalshi_vol_24h_usd: 29996.3
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-12T17:18:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk reads this as the market treating a hot September CPI print as a done deal, any lingering short side has effectively vanished ahead of the release.
