---
signal_id: "CMSIG2026112501"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-ladder-2026-11-25"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays priced at 4.0-4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-25T13:31:45.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (following next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.04
  volume_24h_usd: 42.54
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.0-4.25% range: 95% above 4.0% but only 4% above 4.25%."
  - "October PCE at 3.8% is the hottest reading in three years, yet the market is not pricing in a hike above 4.25%, odds of a move higher sit near zero."
  - "A separate Kalshi contract on a cut greater than 25 basis points this year is priced at 0%, consistent with the inflation data pushing rate-cut hopes off the table."
  - "The 4.25% strike at just 4% probability signals markets are treating 4.0-4.25% as a ceiling, not a floor, despite the inflation surprise."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed's preferred PCE inflation gauge accelerated to 3.8% in October 2026, a three-year high, raising the stakes for the central bank heading into 2027."
    publisher: "Jeff Cox"
    published_at: "2026-11-25T13:31:45.000Z"
    source_url: "https://www.cnbc.com/2026/11/25/pce-inflation-report-october-2026.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/11/25/pce-inflation-report-october-2026.html"
        retrieved_at: "2026-11-28T07:47:57+00:00"
  - type: "pm_response"
    notes: "Kalshi's Fed funds ladder resolves via the Federal Reserve's post-meeting statement; the sharp cutoff above 4.25% reflects near-unanimous market conviction that the Fed holds and does not hike further."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: PCE inflation report October 2026: Fed’s preferred inflation gauge acc"
    url: "https://www.cnbc.com/2026/11/25/pce-inflation-report-october-2026.html"
    published_at: "2026-11-25T13:31:45.000Z"
    retrieved_at: "2026-11-28T07:47:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
