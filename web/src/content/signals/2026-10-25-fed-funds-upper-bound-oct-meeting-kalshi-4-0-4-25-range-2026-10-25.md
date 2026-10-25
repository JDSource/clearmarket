---
signal_id: "CMSIG2026102501"
signal_slug: "fed-funds-upper-bound-oct-meeting-kalshi-4-0-4-25-range-2026-10-25"
headline: "Fed funds upper bound Oct meeting: Kalshi 4.0-4.25% range"
semantic_title: "Fed funds upper bound stays near 4 percent after October meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after October 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 0.8
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.0-4.25% range: 78% above 4.0%, only 10% above 4.25%."
  - "With inflation at 3.7% and near-unanimous economist consensus for a hold, the Kalshi distribution is fully consistent with a pause this week."
  - "The sharp drop from 96% at 3.75% to 78% at 4.0% confirms the market treats 4.0% as the effective floor, not the ceiling."
  - "All 100 surveyed economists project a December hike; December meeting contracts would reveal whether that consensus is priced, but no December ladder data is available here."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "U.S. inflation reached 3.7% ahead of the Fed's October meeting, with 94 of 100 economists surveyed expecting no change this week and all 100 projecting a December rate increase."
    publisher: "Miriam Hart"
    published_at: "2026-10-25T00:00:00.000Z"
    source_url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Miriam Hart"
        source_url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
        retrieved_at: "2026-10-25T12:56:07+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder across multiple strikes shows tight consensus for an October hold, with pricing aligned with the Reuters economist survey."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Miriam Hart: U.S. Inflation Reaches 3.7% Ahead of Fed’s October Meeting | EconoTime"
    url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
    published_at: "2026-10-25T00:00:00.000Z"
    retrieved_at: "2026-10-25T12:56:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
