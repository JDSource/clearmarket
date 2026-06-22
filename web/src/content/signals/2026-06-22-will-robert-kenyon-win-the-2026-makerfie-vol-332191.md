---
signal_id: "CMSIG20260622VS07"
signal_slug: "will-robert-kenyon-win-the-2026-makerfie-vol-332191"
headline: "Kenyon wins Makerfield by-election: 27% on $332K"
semantic_title: "Contested Makerfield by-election draws capital to Kenyon at 27%"
telemetry: "27% · $332K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-22T13:33:01+00:00"
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
  - "Polymarket prices Robert Kenyon winning the 2026 Makerfield by-election at 27%, underdog but live contender."
  - "24h volume of $332K is 47% of all-time float, signaling a sharp uptick in attention to this constituency race."
  - "27% is consistent with a tightening contest; volume surge may precede polling or canvass data entering the market."
  - "Resolves on by-election day; a seat-change outcome would carry UK parliamentary composition implications."
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
    retrieved_at: "2026-06-22T13:33:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume surge on a regional UK by-election at 27% suggests a desk or informed participant is pricing in a tighter-than-expected race, worth monitoring for accompanying polling releases.
