---
signal_id: "CMSIG2026102502"
signal_slug: "oct-fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-84-2026-10-25"
headline: "Oct Fed funds upper bound at 4.0-4.25%: Kalshi ladder 84%"
semantic_title: "Market prices a hold as inflation at 3.7 percent keeps December hike alive"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Oct 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 193.42
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices 84% on the upper bound staying above 4.0% after this meeting, with only 10% at the 4.25% strike, implying a hold at current levels."
  - "The 3.7% inflation print and unanimous economist expectation of a December hike are consistent with the market's pricing of a pause now but elevated terminal rate risk."
  - "The near-zero probability above 4.5% (4%) suggests markets are not pricing a surprise hike this week despite the firmer inflation data."
  - "Resolution follows the Federal Reserve's official rate decision announcement; any inter-meeting communication from Chair Kevin Warsh before Wednesday could reprice the 4.25% strike rapidly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "U.S. inflation reached 3.7% ahead of the Fed's October meeting, with a Reuters survey showing all 100 economists projecting a December rate increase."
    publisher: "Miriam Hart"
    published_at: "2026-10-25T00:00:00.000Z"
    source_url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Miriam Hart"
        source_url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
        retrieved_at: "2026-10-27T13:54:00+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder volume rose 274x day over day on this contract, consistent with elevated pre-decision interest around the inflation catalyst."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Miriam Hart: U.S. Inflation Reaches 3.7% Ahead of Fed’s October Meeting | EconoTime"
    url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
    published_at: "2026-10-25T00:00:00.000Z"
    retrieved_at: "2026-10-27T13:54:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
