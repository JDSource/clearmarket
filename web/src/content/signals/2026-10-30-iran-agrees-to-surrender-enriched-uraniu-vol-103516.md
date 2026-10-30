---
signal_id: "CMSIG20261030VS04"
signal_slug: "iran-agrees-to-surrender-enriched-uraniu-vol-103516"
headline: "Iran uranium deal by Oct 31: 0% on $104K"
semantic_title: "Iran uranium surrender by Oct 31 stays at zero"
telemetry: "0% · $104K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T07:48:50+00:00"
event_id: "CM-EVT-Z3K4DFFZY1"
event_slug: "iran-agrees-to-surrender-enriched-uranium-stockpile-by"
event_question: "Will Iran agree to surrender its enriched uranium stockpile by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaff5b702feef28fd0207583e17f8f2610d8191b5951441974e166dcdb61366e2"
  question_raw: "Iran agrees to surrender enriched uranium stockpile by October 31, 2026?"
  current_price: 0.002
  volume_24h_usd: 103516.83193
  volume_cumulative_usd: 260100.47729
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-31T00:00:00Z"
bullets:
  - "Polymarket prices Iran agreeing to surrender its enriched uranium stockpile by October 31 at 0%, the deadline is tomorrow."
  - "24h volume of $104K is 40% of all-time $260K, the largest single-day flow on this contract."
  - "A zero-price surge this size reflects traders locking in certainty of non-resolution before the cutoff."
  - "Contract expires worthless if no agreement is announced by October 31, 2026."
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
      poly_vol_24h_usd: 103516.83193
sources:
  - label: "ClearMarket market record: Will Iran agree to surrender its enriched uranium stock"
    url: "https://clearmarket.fyi/events/iran-agrees-to-surrender-enriched-uranium-stockpile-by"
    retrieved_at: "2026-10-30T07:48:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $104K rush to a 0% contract one day before deadline signals geopolitical desks are booking confirmed losses on any residual YES exposure with zero diplomatic signal on the horizon.
