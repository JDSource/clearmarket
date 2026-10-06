---
signal_id: "CMSIG2026100501"
signal_slug: "fed-funds-upper-bound-implied-4-0-4-25-kalshi-ladder-2026-10-05"
headline: "Fed funds upper bound implied 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds rate seen near 4 percent after weak jobs print"
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
  volume_24h_usd: 42.31
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.0-4.25% range: 70% chance above 4.0%, only 17% above 4.25%."
  - "September payrolls of 29,000 are consistent with cooling hike expectations, but the market has not moved to price cuts, the 4.0% strike still leads."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) prices only 20% above 4.0%, suggesting split signals across contract horizons, one meeting versus further out."
  - "Resolves via the Federal Reserve's official policy statement for the relevant FOMC meeting date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September payrolls came in at just 29,000 jobs, sharply below expectations, cooling rate-hike bets but leaving the Fed in a stagflationary bind with sticky inflation."
    publisher: "Durva More"
    published_at: "2026-10-05T11:57:55.000Z"
    source_url: "https://www.hindustantimes.com/world-news/us-news/us-jobs-report-cools-fed-rate-hike-bets-why-october-cpi-and-record-diesel-prices-now-matter-101791198371546.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Durva More"
        source_url: "https://www.hindustantimes.com/world-news/us-news/us-jobs-report-cools-fed-rate-hike-bets-why-october-cpi-and-record-diesel-prices-now-matter-101791198371546.html"
        retrieved_at: "2026-10-06T07:48:15+00:00"
  - type: "pm_response"
    notes: "Kalshi carries two separate Fed funds ladder contracts with meaningfully different implied ranges, flagging horizon uncertainty across the forward curve."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Durva More: US jobs report cools Fed rate hike bets: Why October CPI and record di"
    url: "https://www.hindustantimes.com/world-news/us-news/us-jobs-report-cools-fed-rate-hike-bets-why-october-cpi-and-record-diesel-prices-now-matter-101791198371546.html"
    published_at: "2026-10-05T11:57:55.000Z"
    retrieved_at: "2026-10-06T07:48:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
