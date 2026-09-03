---
signal_id: "CMSIG20260903VS04"
signal_slug: "will-anthony-dilorenzo-be-the-republican-vol-16785"
headline: "DiLorenzo NH-01 GOP nominee: 76% on $16K surge"
semantic_title: "DiLorenzo leads NH-01 GOP field at 76% on Polymarket"
telemetry: "76% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-03T12:31:50+00:00"
event_id: "CM-EVT-CGQ5HMR728"
event_slug: "nh-01-republican-primary-winner"
event_question: "Will the Republican primary winner be decided for New Hampshire's 1st Congressional District?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x91586130efb8231715189a281e3769005986ab9bed02033e647739171c940959"
  question_raw: "Will Anthony DiLorenzo be the Republican Nominee for NH-01?"
  current_price: 0.76
  volume_24h_usd: 16785.076477
  volume_cumulative_usd: 31798.11988999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "Polymarket prices DiLorenzo at 76%, market assigns him a strong but not certain path to the nomination."
  - "24h volume of $16K is 53% of all-time flow, the majority of lifetime trading arriving in a single day."
  - "Primary consolidation dynamics or a rival's exit may be concentrating capital behind DiLorenzo."
  - "Resolves on the Republican nominee outcome for New Hampshire's 1st Congressional District."
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
      poly_vol_24h_usd: 16785.076477
sources:
  - label: "ClearMarket market record: Will the Republican primary winner be decided for New H"
    url: "https://clearmarket.fyi/events/nh-01-republican-primary-winner"
    retrieved_at: "2026-09-03T12:31:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of lifetime volume printing at three-to-one odds in one session points to a race-defining development, likely a competitor's withdrawal or a decisive endorsement, that desks should investigate.
