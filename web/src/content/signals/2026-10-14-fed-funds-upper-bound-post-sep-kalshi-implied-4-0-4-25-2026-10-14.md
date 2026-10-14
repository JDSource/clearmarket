---
signal_id: "CMSIG2026101407"
signal_slug: "fed-funds-upper-bound-post-sep-kalshi-implied-4-0-4-25-2026-10-14"
headline: "Fed funds upper bound post-Sep: Kalshi-implied 4.0-4.25%"
semantic_title: "Fed funds upper bound seen near 4.0 to 4.25 percent after September"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.33
  volume_24h_usd: 1129.38
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "The Kalshi ladder implies a September 2026 Fed funds upper bound in the 4.0-4.25% range: 93% above 4.0% but only 33% above 4.25%, with trading volume up 9,607x day-over-day."
  - "A 29,000 September payroll print, far below typical expectations, is a dovish data shock that markets may be absorbing via the sharp drop in probability above 4.25%."
  - "The extreme volume surge (9,607x day-over-day) signals this contract is drawing intense fresh attention following the weak jobs report, even if the implied level has not visibly shifted in the data provided."
  - "The Fed's concurrent 25bp hike (see Story 2) and Williams' 2027 pause signal frame the 4.0-4.25% zone as a likely terminal range, consistent with this ladder distribution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US economy added only 29,000 jobs in September, a sharp hiring slowdown that adds uncertainty to the Federal Reserve's rate path ahead of upcoming meetings."
    publisher: "cnnbc.com"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://cnnbc.com/us-economy-adds-just-29-000-jobs-in-september"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/us-economy-adds-just-29-000-jobs-in-september"
        retrieved_at: "2026-10-14T13:17:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows massive volume spike alongside the weak jobs print, the 4.0-4.25% implied range is the market's current best estimate of where the cycle peaks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: US Economy Adds Just 29,000 Jobs in September - CNNBC"
    url: "https://cnnbc.com/us-economy-adds-just-29-000-jobs-in-september"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-14T13:17:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
