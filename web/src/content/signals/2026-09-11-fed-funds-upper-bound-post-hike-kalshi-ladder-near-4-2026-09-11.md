---
signal_id: "CMSIG2026091102"
signal_slug: "fed-funds-upper-bound-post-hike-kalshi-ladder-near-4-2026-09-11"
headline: "Fed funds upper bound post-hike: Kalshi ladder near 4%"
semantic_title: "Fed funds upper bound seen near 4 percent after hike cycle"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-11T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound (post-hike cycle)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.47
  volume_24h_usd: 575.93
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound near 4.0%, with 88% above 3.75% but only 47% above 4.0%."
  - "Hot August CPI print is consistent with the market pricing a rate path that clears 3.75% but stops short of 4.25%, where odds drop to 13%."
  - "The sharp cliff between 4.0% (47%) and 4.25% (13%) reflects the market treating 4.0% as the ceiling of the most likely outcome, not a stepping stone."
  - "A companion Kalshi ladder (CM-EVT-4ZQLQPNH91) shows 81% above 3.75% but only 2% above 4.0%, suggesting the two contracts differ on the precise terminal bound -- traders should note the resolution horizon difference."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Accelerating August CPI reinforced market expectations that the Fed will raise rates, pushing the implied terminal rate higher."
    publisher: "Reuters"
    published_at: "2026-09-11T00:00:00.000Z"
    source_url: "https://virginiabusiness.com/us-consumer-prices-rise-august-fed-rate-hike/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://virginiabusiness.com/us-consumer-prices-rise-august-fed-rate-hike/"
        retrieved_at: "2026-09-12T11:56:19+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves against the official Fed funds upper bound; the gap between 4ZQLQPNH91 and MR57HVWJT3 likely reflects different settlement dates."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: US consumer prices accelerate in August, push Fed closer to rate hike"
    url: "https://virginiabusiness.com/us-consumer-prices-rise-august-fed-rate-hike/"
    published_at: "2026-09-11T00:00:00.000Z"
    retrieved_at: "2026-09-12T11:56:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
