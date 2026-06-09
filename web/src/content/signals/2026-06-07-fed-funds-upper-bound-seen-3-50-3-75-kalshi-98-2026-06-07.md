---
signal_id: "CMSIG2026060703"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-98-2026-06-07"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi 98%"
semantic_title: "Fed funds upper bound anchors at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-07T09:00:00.000Z"
event_id: "CM-EVT-RJ6SMJGK50"
event_slug: "kxfed-26jun"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUN-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jun 17, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 1599.49
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-06-17T18:05:00Z"
bullets:
  - "Kalshi ladder prices 98% above 3.50% but only 2% above 3.75%, pinning the expected upper bound firmly in the 3.50-3.75% range."
  - "Hike talk in media contrasts with the market: the distribution shows near-zero probability of the upper bound reaching 3.75% or beyond."
  - "The market is absorbing hawkish headlines without pricing a hike; consensus treats current levels as the ceiling."
  - "Resolves via the Federal Reserve's official federal funds rate target announcement; the relevant settlement date is implicit in the contract question."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Strong jobs data is fueling arguments from some Fed officials that rates may need to rise later this year, pressure-testing new Fed Chair Kevin Warsh."
    publisher: "newstribune.com"
    published_at: "2026-06-07T09:00:00.000Z"
    source_url: "https://www.newstribune.com/news/2026/jun/07/pressure-mounts-on-warsh-as-jobs-data-means-fed/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newstribune.com"
        source_url: "https://www.newstribune.com/news/2026/jun/07/pressure-mounts-on-warsh-as-jobs-data-means-fed/"
        retrieved_at: "2026-06-09T10:57:53+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder distribution shows the hike narrative in media is not being priced; the market holds the upper bound at 3.50-3.75%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newstribune.com: Pressure mounts on Warsh as jobs data means Fed may have to hike rates"
    url: "https://www.newstribune.com/news/2026/jun/07/pressure-mounts-on-warsh-as-jobs-data-means-fed/"
    published_at: "2026-06-07T09:00:00.000Z"
    retrieved_at: "2026-06-09T10:57:53+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
