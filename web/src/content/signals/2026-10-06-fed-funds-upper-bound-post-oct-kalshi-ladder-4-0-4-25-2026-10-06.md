---
signal_id: "CMSIG2026100601"
signal_slug: "fed-funds-upper-bound-post-oct-kalshi-ladder-4-0-4-25-2026-10-06"
headline: "Fed funds upper bound post-Oct: Kalshi ladder 4.0-4.25%"
semantic_title: "Fed funds upper bound seen near 4 to 4.25 percent after October"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-06T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound following next Fed meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 157.58
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the post-October Fed funds upper bound in the 4.00-4.25% range: 78% above 4.00%, only 19% above 4.25%."
  - "September payrolls of 29,000 and a rising unemployment rate are consistent with the market pricing out further hikes beyond the current level."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) puts 99% odds on the upper bound above 3.75% but only 18% above 4.00%, suggesting the market sees the current cycle peak near 4.00%."
  - "Resolution follows the Federal Reserve's official post-meeting rate announcement; any emergency inter-meeting action would reset the ladder."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September payrolls rose only 29,000 and unemployment moved higher, sharply reducing expectations for a Fed rate hike at the October 27-28 meeting."
    publisher: "tradetalkjournal.com"
    published_at: "2026-10-06T00:00:00.000Z"
    source_url: "https://tradetalkjournal.com/2026/10/06/us-jobs-report-payrolls-rise-just-29000-fed-october-hike-bets-fade/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradetalkjournal.com"
        source_url: "https://tradetalkjournal.com/2026/10/06/us-jobs-report-payrolls-rise-just-29000-fed-october-hike-bets-fade/"
        retrieved_at: "2026-10-07T07:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data is available; no intraday price move can be confirmed, only the current distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradetalkjournal.com: US jobs report: Payrolls rise just 29,000; Fed October hike bets fade"
    url: "https://tradetalkjournal.com/2026/10/06/us-jobs-report-payrolls-rise-just-29000-fed-october-hike-bets-fade/"
    published_at: "2026-10-06T00:00:00.000Z"
    retrieved_at: "2026-10-07T07:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
