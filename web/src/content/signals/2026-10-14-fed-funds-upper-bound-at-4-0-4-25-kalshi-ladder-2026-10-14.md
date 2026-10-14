---
signal_id: "CMSIG2026101401"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-10-14"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen holding at 4 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (current cycle)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.13
  volume_24h_usd: 48.91
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the fed funds upper bound in the 4.00-4.25% range: 80% above 4.00% but only 13% above 4.25%."
  - "The hold decision is consistent with current pricing; trading volume surged 9,607x day-over-day, flagging intense fresh attention on this contract."
  - "Story 2 separately reports a 25bp hike occurred; the ladder's sharp drop from 80% to 13% between 4.00% and 4.25% suggests the market treats 4.25% as a ceiling for now."
  - "The Kalshi contract on a cut greater than 25bp prices at only 2%, confirming the market sees no near-term easing path despite the weak September jobs print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh held rates steady at his first FOMC meeting while signaling openness to future hikes."
    publisher: "cnnbc.com"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://cnnbc.com/federal-reserve-holds-rates-steady-as-new-chairman-kevin-warsh-signals-openness-to-future-increases"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/federal-reserve-holds-rates-steady-as-new-chairman-kevin-warsh-signals-openness-to-future-increases"
        retrieved_at: "2026-10-14T07:47:32+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Federal Reserve official announcement; volume spike confirms this is the most actively traded macro contract today."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: Federal Reserve Holds Rates Steady as New Chairman Kevin Warsh Signals"
    url: "https://cnnbc.com/federal-reserve-holds-rates-steady-as-new-chairman-kevin-warsh-signals-openness-to-future-increases"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-14T07:47:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
