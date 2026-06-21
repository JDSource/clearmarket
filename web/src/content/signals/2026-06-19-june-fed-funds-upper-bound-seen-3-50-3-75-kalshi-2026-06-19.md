---
signal_id: "CMSIG2026061904"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-19"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound seen firmly in the 3.50-3.75 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-19T14:42:17.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound (current cycle)"
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
  - "The Kalshi ladder prices 95% above 3.50% but only 36% above 3.75%, pinning the market-implied upper bound squarely in the 3.50-3.75% range."
  - "Warsh's hold decision and removal of forward guidance are fully consistent with this distribution, no cut signal means no repricing below 3.50%."
  - "The 16% pricing above 4.00% reflects residual tail risk from Warsh's hawkish posture, not a base-case hike scenario the market is pricing in."
  - "The Kalshi contract on a single cut of more than 25 basis points prices at only 7%, confirming the ladder read: the market sees rates anchored at current levels."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh held rates steady at 3.50-3.75% at his first FOMC meeting and dropped forward guidance, dot plots, and any signal of a dovish pivot."
    publisher: "Tim McMahon"
    published_at: "2026-06-19T14:42:17.000Z"
    source_url: "https://inflationdata.com/articles/2026/06/19/warsh-first-fomc-meeting/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tim McMahon"
        source_url: "https://inflationdata.com/articles/2026/06/19/warsh-first-fomc-meeting/"
        retrieved_at: "2026-06-21T11:13:58+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution is fully consistent with the hold; the sharp drop from 95% above 3.50% to 36% above 3.75% confirms the market is not pricing any incremental hike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tim McMahon: Warsh's First FOMC: No Dot, No Guidance, and No Dovish Pivot"
    url: "https://inflationdata.com/articles/2026/06/19/warsh-first-fomc-meeting/"
    published_at: "2026-06-19T14:42:17.000Z"
    retrieved_at: "2026-06-21T11:13:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
