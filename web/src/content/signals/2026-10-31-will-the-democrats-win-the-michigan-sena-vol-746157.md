---
signal_id: "CMSIG20261031VS00"
signal_slug: "will-the-democrats-win-the-michigan-sena-vol-746157"
headline: "Michigan Senate Dem win: 78% on $746K surge"
semantic_title: "Democrats hold a wide lead in Michigan Senate betting"
telemetry: "78% · $746K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T07:49:19+00:00"
event_id: "CM-EVT-P8B8CLLCB5"
event_slug: "michigan-senate-election-winner"
event_question: "Will a Michigan Senate election winner be determined by the next election cycle?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbfeb6d4cf3eab6071e204219b0647c8224d63a12778df467311b5f2a4b3a5bd4"
  question_raw: "Will the Democrats win the Michigan Senate race in 2026?"
  current_price: 0.78
  volume_24h_usd: 746157.467928
  volume_cumulative_usd: 2104628.092615
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 78%, a commanding favorite reflecting strong structural advantage."
  - "$746K traded in 24h, equal to 35% of all-time volume, marking a major late-cycle commitment."
  - "Election-eve money concentrating here signals the race is viewed as a near-lock but not fully settled."
  - "Resolves on Michigan 2026 midterm Senate result."
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
      poly_vol_24h_usd: 746157.467928
sources:
  - label: "ClearMarket market record: Will a Michigan Senate election winner be determined by"
    url: "https://clearmarket.fyi/events/michigan-senate-election-winner"
    retrieved_at: "2026-10-31T07:49:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 35% single-day share of all-time volume on an already-high 78% price suggests desks are either closing hedges or making final directional bets before Tuesday's result.
