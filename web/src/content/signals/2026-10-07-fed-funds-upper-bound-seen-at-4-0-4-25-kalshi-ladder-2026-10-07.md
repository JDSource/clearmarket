---
signal_id: "CMSIG2026100702"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-10-07"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Markets price one more hike but keep December, not October, in view"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound following a subsequent Fed decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 10.78
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder implies the federal funds upper bound in the 4.0-4.25% range: 82% above 4.0%, only 19% above 4.25%."
  - "FOMC minutes flagged another hike this year but explicitly signaled no October move, market pricing is consistent with that read."
  - "The companion near-term Kalshi ladder (CM-EVT-6BS28TS762) prices only 18% above 4.0%, confirming the market is dating the final hike to December, not October."
  - "The Kalshi contract on rate cuts greater than 25 basis points this year (CM-EVT-RWRZ1R3SD6) sits at just 3%, no pivot scenario is being priced."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September FOMC minutes showed consensus for one more hike this year, with an October move seen as unlikely."
    publisher: "Hwang Yoonju"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.asiae.co.kr/en/article/2026100804564226796"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Hwang Yoonju"
        source_url: "https://www.asiae.co.kr/en/article/2026100804564226796"
        retrieved_at: "2026-10-08T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; pricing is tightly consistent with the minutes' 'one more hike, not yet' signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Hwang Yoonju: September FOMC Minutes: Consensus on Another Hike This Year... October"
    url: "https://www.asiae.co.kr/en/article/2026100804564226796"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-08T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
