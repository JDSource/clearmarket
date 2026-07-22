---
signal_id: "CMSIG2026072105"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-ladder-2026-07-21"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds pinned near 3.5 to 3.75 percent through year-end"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-21T00:00:00.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound, year-end 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.15
  volume_24h_usd: 43972.99
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "The Kalshi rate ladder prices the Fed funds upper bound firmly in the 3.50-3.75% range: 99% above 3.50% but only 15% above 3.75%."
  - "Reuters economist consensus for a hold is consistent with this tight market-implied band, with hike risk barely registering in the distribution."
  - "The separate Kalshi contract pricing only 9% on a cut greater than 25 basis points this year confirms the market sees the Fed pinned, not easing."
  - "Resolves via Federal Reserve official rate announcements; the 3.75% strike is the live tail to watch."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Reuters poll of economists found the Federal Reserve will hold its key interest rate steady this year despite high inflation, even as a minority see meaningful chances of a hike."
    publisher: "Thomson Reuters"
    published_at: "2026-07-21T00:00:00.000Z"
    source_url: "https://kelo.com/2026/07/21/fed-to-hold-rates-this-year-despite-high-inflation-but-economists-cite-high-chances-of-a-hike-reuters-poll/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://kelo.com/2026/07/21/fed-to-hold-rates-this-year-despite-high-inflation-but-economists-cite-high-chances-of-a-hike-reuters-poll/"
        retrieved_at: "2026-07-22T10:22:09+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder leaves only 15% above 3.75%, making the rate-hold view the overwhelming market consensus alongside the Reuters economist survey."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Fed to hold rates this year despite high inflation, but economists cit"
    url: "https://kelo.com/2026/07/21/fed-to-hold-rates-this-year-despite-high-inflation-but-economists-cite-high-chances-of-a-hike-reuters-poll/"
    published_at: "2026-07-21T00:00:00.000Z"
    retrieved_at: "2026-07-22T10:22:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
