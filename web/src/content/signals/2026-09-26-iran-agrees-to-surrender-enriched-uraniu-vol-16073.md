---
signal_id: "CMSIG20260926VS04"
signal_slug: "iran-agrees-to-surrender-enriched-uraniu-vol-16073"
headline: "Iran uranium deal by Oct 31: 3% on $16K surge"
semantic_title: "Iran uranium surrender by October stays a long shot"
telemetry: "3% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T12:40:21+00:00"
event_id: "CM-EVT-Z3K4DFFZY1"
event_slug: "iran-agrees-to-surrender-enriched-uranium-stockpile-by"
event_question: "Will Iran agree to surrender its enriched uranium stockpile by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaff5b702feef28fd0207583e17f8f2610d8191b5951441974e166dcdb61366e2"
  question_raw: "Iran agrees to surrender enriched uranium stockpile by October 31, 2026?"
  current_price: 0.028
  volume_24h_usd: 16073.792102
  volume_cumulative_usd: 51901.614438000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-31T00:00:00Z"
bullets:
  - "Polymarket prices Iran agreeing to surrender its enriched uranium stockpile by October 31, 2026, at just 3%."
  - "$16.1K in 24h is 31% of all-time volume, a notable spike on a contract the market treats as nearly off the table."
  - "Volume this size on a 3% contract typically reflects hedging against a geopolitical surprise or speculative tail-risk buying."
  - "Contract resolves on a verified Iran agreement to transfer enriched uranium by the stated deadline."
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
      poly_vol_24h_usd: 16073.792102
sources:
  - label: "ClearMarket market record: Will Iran agree to surrender its enriched uranium stock"
    url: "https://clearmarket.fyi/events/iran-agrees-to-surrender-enriched-uranium-stockpile-by"
    retrieved_at: "2026-09-26T12:40:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 31% all-time volume day on a near-zero geopolitical contract signals that some desks are actively pricing tail risk around Iran nuclear diplomacy, worth flagging for macro and energy books.
