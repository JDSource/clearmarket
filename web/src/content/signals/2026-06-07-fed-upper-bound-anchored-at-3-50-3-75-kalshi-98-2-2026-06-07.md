---
signal_id: "CMSIG2026060702"
signal_slug: "fed-upper-bound-anchored-at-3-50-3-75-kalshi-98-2-2026-06-07"
headline: "Fed upper bound anchored at 3.50-3.75%: Kalshi 98%/2%"
semantic_title: "Rate hike narrative absorbed at 3.50-3.75 percent ceiling"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-07T09:00:00.000Z"
event_id: "CM-EVT-RJ6SMJGK50"
event_slug: "kxfed-26jun"
event_question: "Fed funds upper bound (Warsh-era meeting)"
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
  - "Kalshi ladder prices 98% above 3.50% but only 2% above 3.75%, market caps the likely upper bound at 3.75%."
  - "Media hike-pressure narrative is only partly endorsed: markets see a move to 3.50-3.75% as near-certain but reject pricing above 4.00% at just 1%."
  - "The Kalshi contract on a jumbo cut (CM-EVT-RWRZ1R3SD6) sits at 10%, signaling the rate path is seen as flat-to-up, not down."
  - "Resolves via Federal Reserve official announcement; the near-zero probability above 4.25% implies markets are not pricing a multi-hike cycle despite hawkish commentary."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Analysts and headlines argue the strong jobs data puts pressure on Fed Chair Kevin Warsh to hike rates later in 2026."
    publisher: "newstribune.com"
    published_at: "2026-06-07T09:00:00.000Z"
    source_url: "https://www.newstribune.com/news/2026/jun/07/pressure-mounts-on-warsh-as-jobs-data-means-fed/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newstribune.com"
        source_url: "https://www.newstribune.com/news/2026/jun/07/pressure-mounts-on-warsh-as-jobs-data-means-fed/"
        retrieved_at: "2026-06-08T12:25:51+00:00"
  - type: "pm_response"
    notes: "Kalshi rates ladder resolves via Federal Reserve; the hard cliff at 3.75% is the key inflection point in current pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newstribune.com: Pressure mounts on Warsh as jobs data means Fed may have to hike rates"
    url: "https://www.newstribune.com/news/2026/jun/07/pressure-mounts-on-warsh-as-jobs-data-means-fed/"
    published_at: "2026-06-07T09:00:00.000Z"
    retrieved_at: "2026-06-08T12:25:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
