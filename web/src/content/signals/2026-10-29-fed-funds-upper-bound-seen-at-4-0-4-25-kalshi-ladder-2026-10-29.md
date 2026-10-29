---
signal_id: "CMSIG2026102901"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-10-29"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 4 percent after hold"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T03:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound (post-October 2026 meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 758.19
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts the post-October meeting fed funds upper bound squarely in the 4.00-4.25% range: 80% above 4.00%, collapsing to just 3% above 4.25%."
  - "The hold Warsh announced is fully consistent with the ladder distribution; trading volume on this contract surged 4,352% day over day, signaling sharp fresh attention."
  - "Two Fed dissenters sought a hike, but the ladder assigns only single-digit probability to 4.25% or above, meaning the market is not pricing the hawks' preferred path."
  - "Kalshi's separate contract on a Fed rate cut greater than 25 basis points this year sits at just 3%, confirming the market sees no imminent easing either."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Federal Reserve Chair Kevin Warsh held rates steady at approximately 3.9% citing elevated inflation, with two dissenters seeking a hike."
    publisher: "Colby Smith, Joe Rennison, Ben Casselman, Tony Romm, Deborah B. Solomon"
    published_at: "2026-10-29T03:00:00.000Z"
    source_url: "https://www.nytimes.com/live/2026/10/28/business/fed-meeting-warsh-interest-rates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Colby Smith, Joe Rennison, Ben Casselman, Tony Romm, Deborah B. Solomon"
        source_url: "https://www.nytimes.com/live/2026/10/28/business/fed-meeting-warsh-interest-rates"
        retrieved_at: "2026-10-29T14:55:20+00:00"
  - type: "pm_response"
    notes: "Kalshi's fed funds ladder is the primary rate-path vehicle here; the 44.5x volume spike confirms this meeting outcome drove heavy contract activity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Colby Smith, Joe Rennison, Ben Casselman, Tony Romm, Deborah B. Solomon: Live Updates: Fed Holds Rates Steady Despite ‘Elevated’ Inflation"
    url: "https://www.nytimes.com/live/2026/10/28/business/fed-meeting-warsh-interest-rates"
    published_at: "2026-10-29T03:00:00.000Z"
    retrieved_at: "2026-10-29T14:55:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
