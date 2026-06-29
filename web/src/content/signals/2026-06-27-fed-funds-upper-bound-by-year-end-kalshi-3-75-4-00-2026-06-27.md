---
signal_id: "CMSIG2026062705"
signal_slug: "fed-funds-upper-bound-by-year-end-kalshi-3-75-4-00-2026-06-27"
headline: "Fed funds upper bound by year-end: Kalshi 3.75-4.00%"
semantic_title: "Fed funds upper bound seen in 3.75 to 4 percent range by year end"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound, year-end 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Kalshi ladder pins the year-end Fed funds upper bound in the 3.75-4.00% range: 55% above 3.75% but only 36% above 4.00%."
  - "Solid first-half economic data supports the Fed holding, consistent with market pricing clustering around one to two cuts by year-end."
  - "Near-term Kalshi ladder for the June meeting implies the current upper bound at 3.50-3.75% (90% above 3.50%, only 34% above 3.75%), showing modest easing priced for H2."
  - "Resolves via Federal Reserve official rate decision; year-end ladder settles on the December 2026 FOMC outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wall Street enters the second half focused on jobs data and rate bets after stocks closed a solid first half."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-06-27T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/wall-street-week-ahead-jobs-data-rate-bets-in-focus-as-us-stocks-close-solid-first-half/articleshow/132028322.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/wall-street-week-ahead-jobs-data-rate-bets-in-focus-as-us-stocks-close-solid-first-half/articleshow/132028322.cms"
        retrieved_at: "2026-06-29T12:28:56+00:00"
  - type: "pm_response"
    notes: "Kalshi's year-end ladder shows markets expect modest rate relief in H2 2026, with the 3.75-4.00% range as the modal outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: Wall Street Week Ahead: Jobs data, rate bets in focus as US stocks clo"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/news/wall-street-week-ahead-jobs-data-rate-bets-in-focus-as-us-stocks-close-solid-first-half/articleshow/132028322.cms"
    published_at: "2026-06-27T00:00:00.000Z"
    retrieved_at: "2026-06-29T12:28:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
