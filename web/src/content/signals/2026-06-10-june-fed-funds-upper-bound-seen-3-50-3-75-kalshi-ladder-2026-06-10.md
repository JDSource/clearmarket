---
signal_id: "CMSIG2026061001"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-ladder-2026-06-10"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen anchored at 3.5 to 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T23:17:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound after June 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi ladder pins the June 2026 Fed funds upper bound in the 3.50-3.75% range: 91% above 3.50% but only 34% above 3.75%."
  - "May CPI hitting a three-year high is consistent with the market firmly ruling out any cut from the current 4.25-4.50% range, the implied mode is well below current rates, signaling cuts are priced but not imminent."
  - "A separate Kalshi binary puts 70% on the Fed holding at 4.25-4.50% with at least one dissent at the next meeting, reinforcing the ladder's central tendency."
  - "Resolution uses the Federal Reserve's post-meeting rate announcement; any split decision or emergency action between now and the meeting date would reprice both markets simultaneously."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May CPI surged to a three-year high driven by Iran-war energy shocks, resetting Fed rate-cut expectations ahead of Chair Kevin Warsh's upcoming meeting."
    publisher: "Celine Provini"
    published_at: "2026-06-10T23:17:00.000Z"
    source_url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Celine Provini"
        source_url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
        retrieved_at: "2026-06-11T12:08:11+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution shows market consensus squarely in the 3.50-3.75% band for the Fed funds upper bound following the June FOMC, with tail risk above 3.75% priced at only 34%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Celine Provini: Hot CPI Resets Fed Rate-Cut Bets Ahead of Warsh Meeting - TheStreet"
    url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
    published_at: "2026-06-10T23:17:00.000Z"
    retrieved_at: "2026-06-11T12:08:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
