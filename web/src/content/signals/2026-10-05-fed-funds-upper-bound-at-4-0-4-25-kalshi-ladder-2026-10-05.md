---
signal_id: "CMSIG2026100501"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-10-05"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 4 percent after jobs miss"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-05T11:57:55.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.17
  volume_24h_usd: 44.22
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.00-4.25% range: 72% above 4.00% but only 17% above 4.25%."
  - "The 29,000 September payroll print is well below consensus, consistent with markets pricing a pause rather than a hike at the next meeting."
  - "A separate Kalshi ladder (CM-EVT-6BS28TS762) prices only 20% above 4.00%, suggesting one contract reflects a prior meeting's terminal level while this one tracks the next decision window."
  - "Resolution via Federal Reserve policy announcement; any surprise hike would collapse the 4.00-4.25% modal range sharply."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A weak September jobs report of just 29,000 payrolls added has cooled expectations for another Fed rate hike, with sticky inflation keeping the Fed's path uncertain."
    publisher: "Durva More"
    published_at: "2026-10-05T11:57:55.000Z"
    source_url: "https://www.hindustantimes.com/world-news/us-news/us-jobs-report-cools-fed-rate-hike-bets-why-october-cpi-and-record-diesel-prices-now-matter-101791198371546.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Durva More"
        source_url: "https://www.hindustantimes.com/world-news/us-news/us-jobs-report-cools-fed-rate-hike-bets-why-october-cpi-and-record-diesel-prices-now-matter-101791198371546.html"
        retrieved_at: "2026-10-06T14:42:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on Fed funds upper bound shows the market is consistent with a hold narrative after the soft jobs print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Durva More: US jobs report cools Fed rate hike bets: Why October CPI and record di"
    url: "https://www.hindustantimes.com/world-news/us-news/us-jobs-report-cools-fed-rate-hike-bets-why-october-cpi-and-record-diesel-prices-now-matter-101791198371546.html"
    published_at: "2026-10-05T11:57:55.000Z"
    retrieved_at: "2026-10-06T14:42:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
