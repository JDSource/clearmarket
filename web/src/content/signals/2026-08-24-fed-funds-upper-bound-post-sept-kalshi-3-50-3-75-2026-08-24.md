---
signal_id: "CMSIG2026082401"
signal_slug: "fed-funds-upper-bound-post-sept-kalshi-3-50-3-75-2026-08-24"
headline: "Fed funds upper bound post-Sept: Kalshi 3.50-3.75%"
semantic_title: "Fed funds upper bound stays near 3.5% after Jackson Hole"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-24T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Post-Sept 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.33
  volume_24h_usd: 15254.1
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the post-September Fed funds upper bound squarely at 3.50-3.75%, with 99% above 3.50% but only 33% above 3.75%."
  - "The market is consistent with a Fed on hold: despite bond market anxiety around Fed Chair Kevin Warsh's debut Jackson Hole speech, no rate move is priced."
  - "The 99%-vs-33% gap across the 3.50%/3.75% strikes implies the market sees the current floor as untouchable but the ceiling as only modestly likely to be breached."
  - "Resolution turns on the FOMC's formal post-meeting rate decision announcement, not the Jackson Hole speech itself."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh arrives at Jackson Hole facing a stagflationary bind, with the benchmark rate at 3.5-3.75% and inflation above 2% while hiring slows."
    publisher: "nile1.com"
    published_at: "2026-08-24T00:00:00.000Z"
    source_url: "https://nile1.com/en/2026/08/24/jackson-hole-is-coming-what-is-the-fed-about-to-do-with-interest-rates/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nile1.com"
        source_url: "https://nile1.com/en/2026/08/24/jackson-hole-is-coming-what-is-the-fed-about-to-do-with-interest-rates/"
        retrieved_at: "2026-08-26T08:38:02+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder concentrates 99% probability above 3.50% but only 33% above 3.75%, bracketing current policy and signaling no move expected."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nile1.com: Jackson Hole Is Coming, What Is the Fed About to Do With Interest Rat"
    url: "https://nile1.com/en/2026/08/24/jackson-hole-is-coming-what-is-the-fed-about-to-do-with-interest-rates/"
    published_at: "2026-08-24T00:00:00.000Z"
    retrieved_at: "2026-08-26T08:38:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
