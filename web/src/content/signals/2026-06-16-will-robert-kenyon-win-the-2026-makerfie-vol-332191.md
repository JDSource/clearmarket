---
signal_id: "CMSIG20260616VS07"
signal_slug: "will-robert-kenyon-win-the-2026-makerfie-vol-332191"
headline: "Kenyon Makerfield win: 27% on $332K surge"
semantic_title: "Kenyon Makerfield by-election money stacks at 27%"
telemetry: "27% · $332K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-16T12:50:46+00:00"
event_id: "CM-EVT-LY608MSMM2"
event_slug: "makerfield-by-election-winner"
event_question: "Will Rebecca Shepherd win the 2026 Makerfield by-election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3c169e95aea67be5fac1529b3ad8e891fe97ec54d1f272fab43b02cce948f6c2"
  question_raw: "Will Robert Kenyon win the 2026 Makerfield by-election?"
  current_price: 0.27
  volume_24h_usd: 332191.61503399996
  volume_cumulative_usd: 701518.2993609991
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices 27%, market treats Kenyon as a credible but underdog candidate in the by-election."
  - "24h volume $332K is 47% of all-time; near-half of lifetime flow arriving in a single session."
  - "Sudden attention surge consistent with new polling, canvassing data, or opposition vulnerability news."
  - "By-election result is binary resolution; volume implies informed participants re-rating the race."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 332191.61503399996
sources:
  - label: "ClearMarket market record: Will Rebecca Shepherd win the 2026 Makerfield by-electi"
    url: "https://clearmarket.fyi/events/makerfield-by-election-winner"
    retrieved_at: "2026-06-16T12:50:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume concentration suggests fresh asymmetric information is entering the Makerfield market, a political desk should seek updated ground-level data before the market reprices further.
