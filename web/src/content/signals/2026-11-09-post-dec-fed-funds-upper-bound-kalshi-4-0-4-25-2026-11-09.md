---
signal_id: "CMSIG2026110902"
signal_slug: "post-dec-fed-funds-upper-bound-kalshi-4-0-4-25-2026-11-09"
headline: "Post-Dec Fed funds upper bound: Kalshi 4.0-4.25%"
semantic_title: "Fed funds upper bound seen at 4.0 to 4.25 percent after December"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-09T21:39:07.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound after December 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 1304.97
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "The Kalshi ladder prices the post-December federal funds upper bound overwhelmingly in the 4.0-4.25% range: 96% above 4.0% but only 10% above 4.25%."
  - "October CPI beat and Fed dissents from Lisa Cook and Beth Hammack both pointed toward higher rates, fully consistent with the 4.0-4.25% market-implied destination."
  - "Trading volume surged 5,455% day-over-day (55.5x), signaling a sharp influx of fresh positioning in this contract following the inflation print."
  - "Companion Kalshi cut contract (CM-EVT-X2TT2M9D02) sits at 2% for any cut before 2027, confirming the market sees hikes not pivots through year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A December rate hike is widely anticipated as the Fed holds its final 2026 meeting, with September projections and October dissents pointing higher."
    publisher: "Simon Moore"
    published_at: "2026-11-09T21:39:07.000Z"
    source_url: "https://www.forbes.com/sites/simonmoore/2026/11/09/what-to-expect-from-the-feds-december-meeting/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Simon Moore"
        source_url: "https://www.forbes.com/sites/simonmoore/2026/11/09/what-to-expect-from-the-feds-december-meeting/"
        retrieved_at: "2026-11-12T07:47:48+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder implies near-certainty of a December hike landing the upper bound at 4.25%, with volume explosion confirming the inflation data drove fresh contract activity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Simon Moore: Fed December Meeting What To Expect For Interest Rates In 2027"
    url: "https://www.forbes.com/sites/simonmoore/2026/11/09/what-to-expect-from-the-feds-december-meeting/"
    published_at: "2026-11-09T21:39:07.000Z"
    retrieved_at: "2026-11-12T07:47:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
