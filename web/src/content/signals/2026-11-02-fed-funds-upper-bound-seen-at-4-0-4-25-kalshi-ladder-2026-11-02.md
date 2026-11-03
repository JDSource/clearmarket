---
signal_id: "CMSIG2026110202"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-11-02"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 4 percent after October hold"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-02T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 63.66
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts the federal funds upper bound in the 4.00-4.25% range, with 74% above 4.00% but only 3% above 4.25%."
  - "The 10-2 hold vote and 3.6% PCE print are consistent with market pricing: a hike to 4.25% or above is nearly fully faded at 3%."
  - "The sharp drop from 74% at 4.00% to 3% at 4.25% signals the market treats 4.00% as the credible ceiling, not a stepping stone."
  - "Resolution via the next FOMC policy statement; two dissenting votes in favor of a hike add a small residual risk premium to the 4.25% strike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve voted 10-2 on October 28 to hold rates as September PCE inflation rose to 3.6% and real consumption stalled."
    publisher: "Goodman"
    published_at: "2026-11-02T00:00:00.000Z"
    source_url: "https://www.goodman-macro.com/en/articles/20261102-fed/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Goodman"
        source_url: "https://www.goodman-macro.com/en/articles/20261102-fed/"
        retrieved_at: "2026-11-03T07:48:22+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder spans 2.75% to 5.25% with ten strikes; the implied range compresses tightly between the 4.00% and 4.25% rungs."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Goodman: November 2 | Fed Weekly: 10, 2 Vote Pauses Rate Hikes as September PCE"
    url: "https://www.goodman-macro.com/en/articles/20261102-fed/"
    published_at: "2026-11-02T00:00:00.000Z"
    retrieved_at: "2026-11-03T07:48:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
