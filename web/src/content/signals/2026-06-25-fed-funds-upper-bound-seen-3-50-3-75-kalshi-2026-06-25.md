---
signal_id: "CMSIG2026062503"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-25"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound hardens at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T15:23:35.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 3.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi ladder prices 95% above 3.50% but only 36% above 3.75%, placing the implied upper bound firmly in the 3.50-3.75% range."
  - "Williams speaking publicly as May PCE hits 4.1% is consistent with a market that sees the Fed holding well above the 3.0-3.25% zone, which prices near 97%."
  - "The 4.0% and above strikes price at just 16%, suggesting the market is not expecting a fresh hiking cycle despite the inflation print."
  - "Resolves via the Federal Reserve's announced upper bound target; the sharp drop from 95% at 3.50% to 36% at 3.75% marks the critical decision boundary."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John C. Williams delivered remarks at the Crane's Money Fund Symposium on June 25 amid elevated inflation."
    publisher: "tellerwindow.newyorkfed.org"
    published_at: "2026-06-25T15:23:35.000Z"
    source_url: "https://tellerwindow.newyorkfed.org/2026/06/25/the-strategy-and-the-goals/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tellerwindow.newyorkfed.org"
        source_url: "https://tellerwindow.newyorkfed.org/2026/06/25/the-strategy-and-the-goals/"
        retrieved_at: "2026-06-26T10:48:01+00:00"
  - type: "pm_response"
    notes: "Kalshi's rate ladder reflects a market pricing in a prolonged hold, not resumed hikes, even as the PCE data beats."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tellerwindow.newyorkfed.org: The Strategy and the Goals"
    url: "https://tellerwindow.newyorkfed.org/2026/06/25/the-strategy-and-the-goals/"
    published_at: "2026-06-25T15:23:35.000Z"
    retrieved_at: "2026-06-26T10:48:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
