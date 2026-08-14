---
signal_id: "CMSIG20260814VS06"
signal_slug: "will-megan-degenfelder-win-the-2026-wyom-vol-15605"
headline: "Degenfelder WY GOP primary: 22% on $16K surge"
semantic_title: "Degenfelder trails Barlow in Wyoming primary at 22%"
telemetry: "22% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-14T09:04:43+00:00"
event_id: "CM-EVT-ZZBTDSPX00"
event_slug: "wyoming-governor-republican-primary-winner"
event_question: "Will the Republican Party nominee win the Wyoming Governor primary by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa875e0b4802818c2ed51fa4a44eeb303d2a11b1df946de66c0444d80468e78b6"
  question_raw: "Will Megan Degenfelder win the 2026 Wyoming Governor Republican primary election?"
  current_price: 0.216
  volume_24h_usd: 15605.836213
  volume_cumulative_usd: 57247.189139
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-18T00:00:00Z"
bullets:
  - "22% prices Degenfelder as a clear underdog against Barlow in the Republican primary."
  - "$16K in 24h represents 27% of all-time volume, notable given the paired Barlow spike."
  - "Mirror-image volume with Spike 5 suggests traders actively rotating between the two candidates."
  - "Resolves on the same Wyoming Republican gubernatorial primary result."
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
      poly_vol_24h_usd: 15605.836213
sources:
  - label: "ClearMarket market record: Will the Republican Party nominee win the Wyoming Gover"
    url: "https://clearmarket.fyi/events/wyoming-governor-republican-primary-winner"
    retrieved_at: "2026-08-14T09:04:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Coordinated volume in both Wyoming primary contracts on the same day points to active reallocation between candidates, signaling a desk-level view that Barlow's lead is credible but not guaranteed.
