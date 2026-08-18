---
signal_id: "CMSIG2026081703"
signal_slug: "year-end-fed-funds-upper-bound-3-50-3-75-range-2026-08-17"
headline: "Year-end Fed funds upper bound: 3.50-3.75% range"
semantic_title: "Year-end Fed funds upper bound priced in the 3.50-3.75% range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-17T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Year-end 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.31
  volume_24h_usd: 1880.68
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "The prediction market ladder pins the year-end Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50% but only 31% above 3.75%."
  - "The Reuters economist hold consensus aligns with this distribution, which implies no hike from current levels through December."
  - "The sharp drop from 98% to 31% between the 3.50% and 3.75% strikes reveals a clean consensus ceiling, any hike scenario is a clear minority view."
  - "Companion ladder CM-EVT-MR57HVWJT3, which appears to reference a nearer meeting, shows 51% above 3.75% and 21% above 4.00%, implying slightly more near-term uncertainty."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Reuters poll of economists unanimously expects the Fed to hold its key rate unchanged at the September meeting and through year-end."
    publisher: "Thomson Reuters"
    published_at: "2026-08-17T00:00:00.000Z"
    source_url: "https://krro.com/2026/08/17/fed-to-hold-interest-rates-this-year-economists-say-sticking-to-their-view-reuters-poll/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://krro.com/2026/08/17/fed-to-hold-interest-rates-this-year-economists-say-sticking-to-their-view-reuters-poll/"
        retrieved_at: "2026-08-18T08:30:34+00:00"
  - type: "pm_response"
    notes: "Ladder resolves via Federal Reserve official rate announcement; the two ladders together suggest markets see minimal movement between now and year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Fed to hold interest rates this year, economists say, sticking to thei"
    url: "https://krro.com/2026/08/17/fed-to-hold-interest-rates-this-year-economists-say-sticking-to-their-view-reuters-poll/"
    published_at: "2026-08-17T00:00:00.000Z"
    retrieved_at: "2026-08-18T08:30:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
