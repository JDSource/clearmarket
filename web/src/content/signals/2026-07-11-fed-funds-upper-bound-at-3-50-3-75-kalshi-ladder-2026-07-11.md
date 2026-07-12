---
signal_id: "CMSIG2026071104"
signal_slug: "fed-funds-upper-bound-at-3-50-3-75-kalshi-ladder-2026-07-11"
headline: "Fed funds upper bound at 3.50-3.75%: Kalshi ladder"
semantic_title: "Near-term Fed funds upper bound wavers on weak jobs data"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-11T09:37:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Fed funds upper bound (near-term meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.46
  volume_24h_usd: 2.76
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound at 3.50-3.75%: 91% above 3.50% but only 46% above 3.75%, showing a split between hold and one hike."
  - "A weak June jobs miss is in tension with the hawkish inflation framing; the 46% probability above 3.75% reflects that uncertainty directly."
  - "This ladder's 91% above 3.50% is slightly softer than the CM-EVT-PHWX2H6DM5 ladder's 98%, suggesting marginal extra doubt from the jobs data."
  - "Resolves via the Federal Reserve's official post-meeting rate announcement; downward revisions to prior months could shift the distribution further."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June jobs report missed expectations and prior months were revised down, complicating the Fed's inflation-fighting posture under Chair Kevin Warsh."
    publisher: "AOL"
    published_at: "2026-07-11T09:37:00.000Z"
    source_url: "https://www.aol.com/articles/latest-jobs-report-missed-expectations-093700000.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/articles/latest-jobs-report-missed-expectations-093700000.html"
        retrieved_at: "2026-07-12T09:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; the spread between the two near-term Fed funds ladders (CM-EVT-PHWX2H6DM5 and CM-EVT-6BS28TS762) captures incremental labor-market uncertainty."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: Latest Jobs Report Missed Expectations - What That Means for Investors"
    url: "https://www.aol.com/articles/latest-jobs-report-missed-expectations-093700000.html"
    published_at: "2026-07-11T09:37:00.000Z"
    retrieved_at: "2026-07-12T09:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
