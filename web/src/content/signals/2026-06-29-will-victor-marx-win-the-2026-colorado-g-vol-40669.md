---
signal_id: "CMSIG20260629VS02"
signal_slug: "will-victor-marx-win-the-2026-colorado-g-vol-40669"
headline: "Marx CO GOP primary: 93% on $41K volume spike"
semantic_title: "Flows defend Victor Marx as Colorado GOP primary locks in"
telemetry: "93% · $41K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T01:47:13+00:00"
event_id: "CM-EVT-QQXJ0J98N1"
event_slug: "colorado-governor-republican-primary-winner"
event_question: "Will a Republican win the Colorado Governor primary?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0b94b4e361a4797c94c4802dec1080f7d60005c04885a8930e931e62b12ea879"
  question_raw: "Will Victor Marx win the 2026 Colorado Governor Republican primary election?"
  current_price: 0.93
  volume_24h_usd: 40669.170171
  volume_cumulative_usd: 80202.41004599999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices 93%, market assigns near-certain Marx victory in the Republican gubernatorial primary."
  - "$41K in 24h equals 51% of all-time volume; majority of lifetime liquidity concentrated at resolution."
  - "Primary result imminent; heavy one-sided flow at 93% implies result is effectively known or broadly anticipated."
  - "Resolution follows official primary canvass; contract closes at 100% on confirmed Marx win."
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
      poly_vol_24h_usd: 40669.170171
sources:
  - label: "ClearMarket market record: Will a Republican win the Colorado Governor primary?"
    url: "https://clearmarket.fyi/events/colorado-governor-republican-primary-winner"
    retrieved_at: "2026-06-29T01:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

For a desk tracking 2026 state-level political risk, the 51% lifetime-volume-in-one-day print at 93% signals the primary outcome is widely anticipated, making this a low-surprise resolution event.
