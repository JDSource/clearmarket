---
signal_id: "CMSIG2026072701"
signal_slug: "july-fed-funds-upper-bound-seen-at-3-75-4-0-kalshi-ladder-2026-07-27"
headline: "July Fed funds upper bound seen at 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds above 4 percent stays a coin flip after July meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.48
  volume_24h_usd: 49.21
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the post-July Fed funds upper bound at 3.75-4.0%, pricing 81% above 3.50% but only 48% above 4.0%."
  - "News that 9 of 19 FOMC members favor higher rates is consistent with the ladder's near-coin-flip at 4.0%, reflecting genuine committee division."
  - "The 3.50% strike at 81% confirms markets see no rate cut; the question is whether Warsh delivers a hike, not a hold."
  - "Companion Kalshi ladder CM-EVT-PHWX2H6DM5 pins a prior meeting's outcome at 3.50-3.75% at 99% above 3.50%, suggesting any hike at the July meeting would be a first move in the current cycle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "With 9 of 19 Fed members signaling higher rates and the July 28-29 meeting imminent, Fed Chair Kevin Warsh faces a divided committee on whether to break a six-meeting hold streak."
    publisher: "David Dierking"
    published_at: "2026-07-27T00:00:00.000Z"
    source_url: "https://www.fool.com/investing/2026/07/27/fed-chair-kevin-warsh-committee-higher-rates/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "David Dierking"
        source_url: "https://www.fool.com/investing/2026/07/27/fed-chair-kevin-warsh-committee-higher-rates/"
        retrieved_at: "2026-07-27T11:15:45+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution shows the July decision is genuinely open between hold at 3.75% and a hike to 4.0%, with near-even odds at the 4.0% strike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "David Dierking: Fed Chair Kevin Warsh Faces a Committee Where 9 of 19 Members Are Sign"
    url: "https://www.fool.com/investing/2026/07/27/fed-chair-kevin-warsh-committee-higher-rates/"
    published_at: "2026-07-27T00:00:00.000Z"
    retrieved_at: "2026-07-27T11:15:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
