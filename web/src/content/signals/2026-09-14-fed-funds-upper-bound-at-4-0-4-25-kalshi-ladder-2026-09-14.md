---
signal_id: "CMSIG2026091402"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-09-14"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen climbing toward 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-14T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after September 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.17
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound squarely in the 4.0-4.25% range: 64% above 4.0%, only 17% above 4.25%."
  - "The distribution implies the market expects a single 25-basis-point hike from the current 3.75% upper bound, consistent with economist consensus in the USA Today report."
  - "A companion ladder (CM-EVT-4ZQLQPNH91) prices 86% above 3.75% but only 1% above 4.0%, suggesting a slightly earlier or smaller move, a minor cross-ladder divergence worth watching."
  - "Resolution uses Federal Reserve official post-meeting rate announcement; no ambiguity on the settlement source."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "USA Today outlines why the Fed may raise rates at its September meeting, citing sticky inflation and Chair Kevin Warsh's signaling."
    publisher: "usatoday.com"
    published_at: "2026-09-14T00:00:00.000Z"
    source_url: "https://www.usatoday.com/story/money/economy/2026/09/14/federal-reserve-september-meeting-interest-rates/91655178007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usatoday.com"
        source_url: "https://www.usatoday.com/story/money/economy/2026/09/14/federal-reserve-september-meeting-interest-rates/91655178007/"
        retrieved_at: "2026-09-15T13:05:57+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder distribution is the clearest market read available on terminal rate for this meeting cycle, implying one hike and no follow-through above 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usatoday.com: Why the Fed may raise interest rates at its September meeting"
    url: "https://www.usatoday.com/story/money/economy/2026/09/14/federal-reserve-september-meeting-interest-rates/91655178007/"
    published_at: "2026-09-14T00:00:00.000Z"
    retrieved_at: "2026-09-15T13:05:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
