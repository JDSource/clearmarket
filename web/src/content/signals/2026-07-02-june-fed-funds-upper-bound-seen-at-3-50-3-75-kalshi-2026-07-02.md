---
signal_id: "CMSIG2026070201"
signal_slug: "june-fed-funds-upper-bound-seen-at-3-50-3-75-kalshi-2026-07-02"
headline: "June Fed funds upper bound seen at 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound consensus firms at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-02T13:28:56.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound following June 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.47
  volume_24h_usd: 0.47
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Kalshi pins the Fed funds upper bound at 3.50-3.75%, pricing 94% above 3.50% but only 47% above 3.75%."
  - "A 57,000 June payroll print -- half the consensus -- is consistent with markets pricing out a near-term rate hike."
  - "Companion Kalshi contract CM-EVT-PHWX2H6DM5 prices 98% above 3.50% but only 10% above 3.75%, showing a tighter modal view at the same meeting horizon."
  - "Resolves via the Federal Reserve's post-meeting statement on the federal funds target range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. economy added only 57,000 jobs in June, badly missing the 110,000 consensus estimate, muddying the Federal Reserve's rate outlook."
    publisher: "americanbanker.com"
    published_at: "2026-07-02T13:28:56.000Z"
    source_url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "americanbanker.com"
        source_url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
        retrieved_at: "2026-07-04T10:05:12+00:00"
  - type: "pm_response"
    notes: "Two overlapping Kalshi ladders both anchor the upper bound modal range at 3.50-3.75%, consistent with markets reading the payroll miss as a hold signal rather than a cut catalyst."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "americanbanker.com: US added 57,000 jobs in June; Fed outlook muddied | American Banker"
    url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
    published_at: "2026-07-02T13:28:56.000Z"
    retrieved_at: "2026-07-04T10:05:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
