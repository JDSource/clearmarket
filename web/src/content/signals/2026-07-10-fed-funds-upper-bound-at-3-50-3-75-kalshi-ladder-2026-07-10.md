---
signal_id: "CMSIG2026071002"
signal_slug: "fed-funds-upper-bound-at-3-50-3-75-kalshi-ladder-2026-07-10"
headline: "Fed funds upper bound at 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound near full pricing at 3.5 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-10T10:04:54.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.21
  volume_24h_usd: 335.4
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50% but only 21% above 3.75%."
  - "Fed officials fretting over inflation and weighing hikes is consistent with the ladder's sharp cutoff just above 3.75%."
  - "The distribution implies near-certainty of no cut from current levels, with hike risk contained to one increment at most."
  - "A companion long-horizon Kalshi ladder (CM-EVT-KWX3HB7XG9) implies a terminal range of 3.0-3.25%, suggesting the market sees limited further tightening beyond the near term."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed officials expressed concern about inflation and signaled readiness to hike if price pressures persist, per Reuters reporting from the latest FOMC meeting readout."
    publisher: "AOL"
    published_at: "2026-07-10T10:04:54.000Z"
    source_url: "https://www.aol.com/articles/fed-officials-fret-over-inflation-100454000.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/articles/fed-officials-fret-over-inflation-100454000.html"
        retrieved_at: "2026-07-12T09:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves against the Federal Reserve's official post-meeting rate announcement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: Fed officials fret over inflation risk, weigh rate hikes - AOL"
    url: "https://www.aol.com/articles/fed-officials-fret-over-inflation-100454000.html"
    published_at: "2026-07-10T10:04:54.000Z"
    retrieved_at: "2026-07-12T09:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
