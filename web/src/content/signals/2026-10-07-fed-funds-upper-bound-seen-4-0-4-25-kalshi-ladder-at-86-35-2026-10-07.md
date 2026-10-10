---
signal_id: "CMSIG2026100703"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-ladder-at-86-35-2026-10-07"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi ladder at 86%/35%"
semantic_title: "Fed funds upper bound holds near 4.0-4.25% range on Kalshi"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-5P6C5JFKT9"
event_slug: "kxfed-27jan"
event_question: "Federal funds rate upper bound following the September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-27JAN-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Jan 27, 2027 meeting?"
  current_price: 0.35
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2027-02-03T19:05:00Z"
bullets:
  - "Kalshi ladder prices 86% that the upper bound exceeds 4.00% and only 35% that it exceeds 4.25%, pinning the implied mode at 4.00-4.25%."
  - "Fed officials' fear of spreading inflation is consistent with a hold rather than a cut; the ladder does not price in any easing at this horizon."
  - "The separate Kalshi contract on a cut greater than 25bps this year sits at 3%, reinforcing that aggressive easing remains a long shot."
  - "Resolution via the Federal Reserve's official post-September-meeting statement; the tight 4.00-4.25% clustering leaves little room for a hawkish surprise above 4.25%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed minutes showed officials feared energy, AI, and other shocks could spread inflation pressures more broadly."
    publisher: "Courtenay Brown"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.axios.com/2026/10/07/fed-warsh-minutes-rates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Courtenay Brown"
        source_url: "https://www.axios.com/2026/10/07/fed-warsh-minutes-rates"
        retrieved_at: "2026-10-10T14:11:44+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve announcement; pricing is internally consistent with the 3% binary cut contract also on Kalshi."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Courtenay Brown: Fed officials feared inflation pressures could spread, minutes show"
    url: "https://www.axios.com/2026/10/07/fed-warsh-minutes-rates"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-10T14:11:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
