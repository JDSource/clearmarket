---
signal_id: "CMSIG2026090301"
signal_slug: "sept-fed-funds-upper-bound-seen-at-3-50-3-75-kalshi-2026-09-03"
headline: "Sept Fed funds upper bound seen at 3.50-3.75%: Kalshi"
semantic_title: "Fed hold in September stays near fully priced"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-03T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound, September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.44
  volume_24h_usd: 8118.72
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the September 2026 Fed funds upper bound in the 3.50-3.75% range, with 99% above 3.50% but only 2% above 3.75%."
  - "Fed Governor Christopher Waller's hold signal is fully consistent with this pricing; the market already implied a pause before his remarks."
  - "Kalshi at 99% above 2.75% shows no credible tail for aggressive cuts back toward pre-2025 levels."
  - "A longer-horizon ladder (CM-EVT-MR57HVWJT3) prices 72% above 3.75% and 31% above 4.00%, suggesting the market sees meaningful odds of a hike at a later meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Christopher Waller signaled support for holding rates steady at the September meeting, contrasting with a more hawkish tone from Fed Governor Kevin Warsh."
    publisher: "Jeff Cox"
    published_at: "2026-09-03T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/09/03/fed-governor-waller-indicates-he-will-support-holding-rates-steady-at-september-meeting.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/09/03/fed-governor-waller-indicates-he-will-support-holding-rates-steady-at-september-meeting.html"
        retrieved_at: "2026-09-04T12:28:22+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the Federal Reserve's official rate decision; the September meeting is the near-term trigger."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Fed Governor Waller indicates he will support holding rates steady at"
    url: "https://www.cnbc.com/2026/09/03/fed-governor-waller-indicates-he-will-support-holding-rates-steady-at-september-meeting.html"
    published_at: "2026-09-03T00:00:00.000Z"
    retrieved_at: "2026-09-04T12:28:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
