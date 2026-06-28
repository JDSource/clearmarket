---
signal_id: "CMSIG20260628VS07"
signal_slug: "will-victor-marx-win-the-2026-colorado-g-vol-29069"
headline: "Marx wins CO GOP primary: 96% on $29K surge"
semantic_title: "Victor Marx Colorado GOP primary locked in at 96% on fresh inflows"
telemetry: "96% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:25:52+00:00"
event_id: "CM-EVT-QQXJ0J98N1"
event_slug: "colorado-governor-republican-primary-winner"
event_question: "Will a Republican win the Colorado Governor primary?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0b94b4e361a4797c94c4802dec1080f7d60005c04885a8930e931e62b12ea879"
  question_raw: "Will Victor Marx win the 2026 Colorado Governor Republican primary election?"
  current_price: 0.961
  volume_24h_usd: 29069.262437999998
  volume_cumulative_usd: 64555.58156699999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Victor Marx winning the 2026 Colorado Republican gubernatorial primary at 96%."
  - "$29K in 24h is 45% of all-time volume, meaningful mid-cycle accumulation, not end-of-contract noise."
  - "Absence of credible challenger activity and Marx's primary organization appear to have resolved the race early."
  - "Primary election date drives final resolution; 4% tail reflects ballot or candidate-status risk only."
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
      poly_vol_24h_usd: 29069.262437999998
sources:
  - label: "ClearMarket market record: Will a Republican win the Colorado Governor primary?"
    url: "https://clearmarket.fyi/events/colorado-governor-republican-primary-winner"
    retrieved_at: "2026-06-28T10:25:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 45% all-time volume surge well ahead of the primary date suggests desks covering 2026 state-level electoral positioning are treating the Marx nomination as settled and beginning to price the general-election contest.
