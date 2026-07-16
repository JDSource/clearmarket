---
signal_id: "CMSIG20260716VS02"
signal_slug: "will-mark-lamb-be-the-republican-nominee-vol-11545"
headline: "Lamb AZ-05 GOP nominee: 89% on $11.5K inflow"
semantic_title: "Traders stack conviction behind Lamb locking up AZ-05 GOP nod"
telemetry: "89% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-16T17:21:12+00:00"
event_id: "CM-EVT-843R2H28J1"
event_slug: "az-05-republican-primary-winner"
event_question: "Will Jay Feely be the Republican nominee for AZ-05?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbd6602e1152e6557a87e6d0bad683a21a2d5fa9132872543170ed6c5d1c53ed0"
  question_raw: "Will Mark Lamb be the Republican nominee for AZ-05?"
  current_price: 0.89
  volume_24h_usd: 11545.885009
  volume_cumulative_usd: 36242.325560000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "89% signals the crowd views Lamb's Republican nomination for Arizona's 5th district as near-certain."
  - "$11.5K over 24 hours equals 32% of all-time contract volume, reflecting a concentrated surge into an already-high-confidence position."
  - "Inflow at this price level suggests a catalyst, filing deadline, poll, or rival dropout, sharpened certainty among informed traders."
  - "Nomination outcome likely resolves at or after the primary date; residual 11% reflects ballot or procedural tail risk."
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
      poly_vol_24h_usd: 11545.885009
sources:
  - label: "ClearMarket market record: Will Jay Feely be the Republican nominee for AZ-05?"
    url: "https://clearmarket.fyi/events/az-05-republican-primary-winner"
    retrieved_at: "2026-07-16T17:21:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume piling into an 89% contract points to an event-driven conviction update on Lamb's primary position, signaling political desks should treat his nomination as the operative baseline for AZ-05 general-election modeling.
