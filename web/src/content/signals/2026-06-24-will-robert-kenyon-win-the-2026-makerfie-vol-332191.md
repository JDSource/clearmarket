---
signal_id: "CMSIG20260624VS07"
signal_slug: "will-robert-kenyon-win-the-2026-makerfie-vol-332191"
headline: "Kenyon wins Makerfield: 27% on $332K surge"
semantic_title: "Kenyon Makerfield by-election odds draw contested capital"
telemetry: "27% · $332K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-24T10:46:26+00:00"
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
  - "27% price signals Kenyon as a credible underdog, not favored but firmly in contention."
  - "47% of all-time volume in 24h indicates a sudden, sharp escalation in market attention."
  - "Makerfield by-election result carries UK parliamentary composition implications; flows precede news."
  - "Resolution on election day; volume surge may front-run a poll, endorsement, or ground-game signal."
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
    retrieved_at: "2026-06-24T10:46:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-majority all-time volume in a single session suggests new information or polling is being priced into a previously thin market; a desk tracking UK political risk should monitor this contract for further re-rating.
