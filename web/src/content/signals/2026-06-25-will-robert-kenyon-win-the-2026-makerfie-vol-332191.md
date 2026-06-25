---
signal_id: "CMSIG20260625VS07"
signal_slug: "will-robert-kenyon-win-the-2026-makerfie-vol-332191"
headline: "Kenyon wins Makerfield by-election: 27% on $332K"
semantic_title: "Kenyon Makerfield by-election bid absorbs challenger capital"
telemetry: "27% · $332K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-25T10:39:33+00:00"
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
  - "Polymarket prices Kenyon's win at 27%, a live contest, not a foregone conclusion."
  - "47% of all-time volume in 24h signals fresh attention, likely triggered by canvassing data, polling, or a campaign event."
  - "The 27% level implies the market sees Kenyon as a credible but underdog challenger in the 2026 by-election."
  - "By-election outcome carries UK parliamentary composition implications, sustaining institutional interest."
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
    retrieved_at: "2026-06-25T10:39:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume surge into a 27% contract suggests a desk covering UK political risk should treat Makerfield as a live data point, new information, likely polling or tactical voting dynamics, has prompted meaningful capital redeployment into this seat.
