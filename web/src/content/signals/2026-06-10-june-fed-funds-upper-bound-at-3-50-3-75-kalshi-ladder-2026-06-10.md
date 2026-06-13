---
signal_id: "CMSIG2026061004"
signal_slug: "june-fed-funds-upper-bound-at-3-50-3-75-kalshi-ladder-2026-06-10"
headline: "June Fed funds upper bound at 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen at 3.50-3.75 percent after June meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T23:17:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "June 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 3.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi ladder implies the June 2026 Fed funds upper bound in the 3.50-3.75% range, pricing 95% above 3.50% but only 36% above 3.75%."
  - "The 4.2% CPI print and vanishing rate-cut forecasts are consistent with a market already positioned for rates to remain elevated well above 3.50%."
  - "Companion Kalshi contract prices a Fed hold at 4.25-4.50% with at least one dissent at 67%, suggesting the market also prices a non-trivial chance rates stay at current levels."
  - "Resolves via FRED data on the Fed funds rate following the June FOMC meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May CPI hit 4.2%, a three-year high driven by energy prices, collapsing sell-side rate-cut forecasts ahead of the FOMC meeting."
    publisher: "Celine Provini"
    published_at: "2026-06-10T23:17:00.000Z"
    source_url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Celine Provini"
        source_url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
        retrieved_at: "2026-06-13T10:25:37+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder prices a clear hold scenario, with the sharp drop at 3.75% reflecting limited expectation of cuts at the upcoming meeting."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Celine Provini: Hot CPI Resets Fed Rate-Cut Bets Ahead of Warsh Meeting - TheStreet"
    url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
    published_at: "2026-06-10T23:17:00.000Z"
    retrieved_at: "2026-06-13T10:25:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
