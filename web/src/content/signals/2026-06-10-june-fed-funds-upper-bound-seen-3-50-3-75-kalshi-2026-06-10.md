---
signal_id: "CMSIG2026061001"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-10"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "June Fed funds upper bound consensus wavers near 3.5 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T23:17:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "June 2026 Fed funds upper bound"
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
  - "Kalshi pins the June 2026 Fed funds upper bound in the 3.50-3.75% range, pricing 91% above 3.50% but only 34% above 3.75%."
  - "Hot May CPI is consistent with rates staying well above 3.50%, but the market is not aggressively pricing a move above 3.75% despite the inflation shock."
  - "The 3.75% strike at 34% signals the distribution has a real upper tail, Warsh's first meeting carries more uncertainty than a routine hold."
  - "A second Kalshi ladder (CM-EVT-RJ6SMJGK50) shows the longer-horizon upper bound firmly at 3.50-3.75%, with only 2% above 3.75%, suggesting the near-term tail fades quickly in time."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May CPI hit a 3-year high driven by Iran war energy shocks, resetting Fed rate-cut expectations ahead of new Chair Kevin Warsh's first meeting."
    publisher: "Celine Provini"
    published_at: "2026-06-10T23:17:00.000Z"
    source_url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Celine Provini"
        source_url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
        retrieved_at: "2026-06-12T11:42:07+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the Fed's own target-range announcement; the sharp drop from 91% at 3.50% to 34% at 3.75% is the key distribution signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Celine Provini: Hot CPI Resets Fed Rate-Cut Bets Ahead of Warsh Meeting - TheStreet"
    url: "https://www.thestreet.com/fed/hot-may-cpi-sticks-a-pin-in-fed-rate-cut-bets"
    published_at: "2026-06-10T23:17:00.000Z"
    retrieved_at: "2026-06-12T11:42:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
