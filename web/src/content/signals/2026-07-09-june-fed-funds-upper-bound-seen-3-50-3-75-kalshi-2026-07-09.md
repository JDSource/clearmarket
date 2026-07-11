---
signal_id: "CMSIG2026070901"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-09"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds hold at 3.50-3.75 near full pricing after FOMC divide"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-09T11:17:00.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound, next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.2
  volume_24h_usd: 2642.98
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi ladder pins the implied Fed funds upper bound in the 3.50-3.75% range, pricing 98% above 3.50% but only 20% above 3.75%."
  - "FOMC minutes flagged inflation risks from tariffs, Iran conflict, and AI buildout, consistent with a hold but not a hike; trading volume on this contract rose 522x day over day, signaling sharp fresh attention."
  - "The distribution shows near-zero probability above 4.0%, meaning markets are absorbing the hawkish rhetoric without pricing actual hikes this cycle."
  - "The 7% Kalshi probability on a cut greater than 25 basis points this year (CM-EVT-RWRZ1R3SD6) confirms the market sees the Fed frozen, not easing, despite the divide narrative."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "FOMC minutes revealed a deep divide among policymakers over whether tariffs, the Iran war, and AI investment could force rate hikes later in 2026."
    publisher: "AOL"
    published_at: "2026-07-09T11:17:00.000Z"
    source_url: "https://www.aol.com/finance/fomc-minutes-expose-deep-divide-111700425.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/finance/fomc-minutes-expose-deep-divide-111700425.html"
        retrieved_at: "2026-07-11T09:24:13+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Federal Reserve announcement; volume surge of 522x day over day confirms this is the primary instrument drawing new capital on the FOMC minutes story."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: FOMC minutes expose deep divide over interest-rate outlook at Warsh's"
    url: "https://www.aol.com/finance/fomc-minutes-expose-deep-divide-111700425.html"
    published_at: "2026-07-09T11:17:00.000Z"
    retrieved_at: "2026-07-11T09:24:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
