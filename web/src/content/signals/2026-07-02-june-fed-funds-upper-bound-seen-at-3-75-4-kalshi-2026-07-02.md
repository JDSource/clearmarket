---
signal_id: "CMSIG2026070201"
signal_slug: "june-fed-funds-upper-bound-seen-at-3-75-4-kalshi-2026-07-02"
headline: "June Fed funds upper bound seen at 3.75-4%: Kalshi"
semantic_title: "Fed funds upper bound consensus wavers near 3.75 to 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-02T13:28:56.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound following June 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound near 3.75-4.00%, pricing 93% above 3.50% but only 29% above 4.00%."
  - "A 57,000 June payroll print, well below the 113,000 consensus, is consistent with the market clustering below 4.00% rather than pricing in further hikes."
  - "The 55% reading at the 3.75% strike and sharp drop to 29% at 4.00% signals the market sees 3.75% as the probable ceiling, not a floor."
  - "Companion Kalshi ladder CM-EVT-PHWX2H6DM5 shows 99% above 3.50% but only 9% above 3.75%, implying a tighter consensus around 3.50-3.75% for a subsequent meeting, a steepening term structure."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US added only 57,000 nonfarm payrolls in June, roughly half the consensus estimate, muddying the Fed's rate outlook."
    publisher: "americanbanker.com"
    published_at: "2026-07-02T13:28:56.000Z"
    source_url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "americanbanker.com"
        source_url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
        retrieved_at: "2026-07-03T10:32:12+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; distribution spans 2.75%-5.25% with the sharpest probability cliff between 3.75% and 4.00%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "americanbanker.com: US added 57,000 jobs in June; Fed outlook muddied | American Banker"
    url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
    published_at: "2026-07-02T13:28:56.000Z"
    retrieved_at: "2026-07-03T10:32:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
