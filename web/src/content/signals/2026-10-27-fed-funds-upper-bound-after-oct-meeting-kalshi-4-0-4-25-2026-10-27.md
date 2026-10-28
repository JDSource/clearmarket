---
signal_id: "CMSIG2026102702"
signal_slug: "fed-funds-upper-bound-after-oct-meeting-kalshi-4-0-4-25-2026-10-27"
headline: "Fed funds upper bound after Oct meeting: Kalshi ~4.0-4.25%"
semantic_title: "Fed funds upper bound seen near 4 to 4.25 percent after October"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T17:45:45.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after October 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 831.35
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the post-October Fed funds upper bound in the 4.00-4.25% range: 96% above 3.75%, but only 8% above 4.25%."
  - "Consensus hold reporting aligns with the ladder: the market prices no move from current levels, rejecting both a cut and a hike this week."
  - "The sharp drop from 96% at 3.75% to 8% above 4.25% shows traders see the current band holding, not a surprise hike."
  - "A companion ladder (CM-EVT-6BS28TS762) puts the implied range lower at 3.75-4.00%, with only 6% above 4.00%, suggesting some disagreement on the current standing level across contract series."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Multiple news outlets report the Fed is expected to hold rates unchanged at its October 29 decision, with Warsh potentially flagging further hikes."
    publisher: "Chris Rugaber, Associated Press"
    published_at: "2026-10-27T17:45:45.000Z"
    source_url: "https://www.pbs.org/newshour/economy/5-things-to-watch-for-in-this-weeks-federal-reserve-meeting"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Chris Rugaber, Associated Press"
        source_url: "https://www.pbs.org/newshour/economy/5-things-to-watch-for-in-this-weeks-federal-reserve-meeting"
        retrieved_at: "2026-10-28T07:49:08+00:00"
  - type: "pm_response"
    notes: "The Kalshi rate ladder is the primary pricing signal for the October Fed decision; the two ladder series (MR57 and 6BS2) bracket the implied upper bound between 3.75% and 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Chris Rugaber, Associated Press: 5 things to watch for in this week's Federal Reserve meeting | PBS New"
    url: "https://www.pbs.org/newshour/economy/5-things-to-watch-for-in-this-weeks-federal-reserve-meeting"
    published_at: "2026-10-27T17:45:45.000Z"
    retrieved_at: "2026-10-28T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
