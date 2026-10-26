---
signal_id: "CMSIG2026102501"
signal_slug: "fed-funds-upper-bound-implied-4-0-4-25-kalshi-ladder-2026-10-25"
headline: "Fed funds upper bound implied 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 4 percent after Oct meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after Oct 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 1.3
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Oct 2026 Fed funds upper bound in the 4.0-4.25% range: 78% above 4.0%, only 10% above 4.25%."
  - "Inflation at 3.7% and unanimous economist consensus for a hold are consistent with the ladder's near-zero probability of cuts and a tight cap just above 4.0%."
  - "The 96% probability above 3.75% versus only 10% above 4.25% signals the market sees this as a straightforward hold, not a hike meeting."
  - "Resolution via the Federal Reserve's official rate announcement on Oct 28; a surprise hike above 4.25% would require dramatic upward repricing across all ladder strikes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "U.S. inflation reached 3.7% ahead of the Fed's October 28 meeting, with 94 of 100 economists surveyed expecting no rate change this week but all 100 projecting a December increase."
    publisher: "Miriam Hart"
    published_at: "2026-10-25T00:00:00.000Z"
    source_url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Miriam Hart"
        source_url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
        retrieved_at: "2026-10-26T14:48:08+00:00"
  - type: "pm_response"
    notes: "Kalshi's rate-ladder distribution is the cleanest pricing of the Oct 28 decision, with the implied mode at 4.0-4.25% and minimal probability mass above 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Miriam Hart: U.S. Inflation Reaches 3.7% Ahead of Fed’s October Meeting | EconoTime"
    url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
    published_at: "2026-10-25T00:00:00.000Z"
    retrieved_at: "2026-10-26T14:48:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
