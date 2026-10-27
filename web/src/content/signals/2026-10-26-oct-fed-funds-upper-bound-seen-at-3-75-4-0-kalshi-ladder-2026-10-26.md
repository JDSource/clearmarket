---
signal_id: "CMSIG2026102602"
signal_slug: "oct-fed-funds-upper-bound-seen-at-3-75-4-0-kalshi-ladder-2026-10-26"
headline: "Oct Fed funds upper bound seen at 3.75-4.0%: Kalshi ladder"
semantic_title: "October Fed hold near certain as market puts long odds on 4 percent ceiling"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-26T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "October 2026 Fed funds upper bound (alt contract)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 154.65
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder for this contract puts 99% odds on the upper bound staying above 3.75%, but only 8% above 4.0%, implying the market-implied level is at 3.75-4.0%."
  - "The near-zero probability above 4.0% aligns with the Kiplinger and AP reporting that a hold is universally expected; this contract is consistent with no hike this week."
  - "Cross-referencing the companion contract (CM-EVT-MR57HVWJT3), which prices 84% above 4.0%, suggests a modest spread between the two contracts worth monitoring for resolution-date differences."
  - "Resolution via Library of Congress; the sharp 99%-to-8% cliff at the 4.0% strike leaves almost no market probability for a surprise hike at this meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The October 2026 Fed meeting is the week's biggest economic event, with Chair Kevin Warsh expected to hold rates steady amid sticky inflation at 3.7%."
    publisher: "Karee Venema"
    published_at: "2026-10-26T00:00:00.000Z"
    source_url: "https://www.kiplinger.com/investing/live/fed-meeting-updates-and-commentary-october-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Karee Venema"
        source_url: "https://www.kiplinger.com/investing/live/fed-meeting-updates-and-commentary-october-2026"
        retrieved_at: "2026-10-27T07:48:12+00:00"
  - type: "pm_response"
    notes: "This Kalshi ladder on the October meeting confirms the hold consensus and cross-checks against the higher-volume companion contract showing a slightly higher implied ceiling."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Karee Venema: October Fed Meeting: Live Updates and Commentary | Kiplinger"
    url: "https://www.kiplinger.com/investing/live/fed-meeting-updates-and-commentary-october-2026"
    published_at: "2026-10-26T00:00:00.000Z"
    retrieved_at: "2026-10-27T07:48:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
