---
signal_id: "CMSIG2026100101"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-10-01"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed pause stays heavily favored after jobs and inflation data"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-01T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.23
  volume_24h_usd: 23.92
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 4.0-4.25% range: 83% above 4.0% but only 23% above 4.25%."
  - "News headline argues the jobs data justifies a hike, but the Kalshi distribution is consistent with a pause being the dominant scenario."
  - "ADP September print of 90,000 and below-forecast PCE are the catalysts; the market is not treating the jobs data as decisive."
  - "The 4.25% strike at only 23% versus 83% at 4.0% shows the distribution is sharply concentrated at a one-and-done hold, not a hike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Softer-than-expected inflation data and a weak ADP jobs print have sharply reduced bets on an October Fed rate hike, with markets now pricing a pause."
    publisher: "Ghiles Guezout"
    published_at: "2026-10-01T00:00:00.000Z"
    source_url: "https://www.fxstreet.com/analysis/markets-are-pricing-a-fed-pause-the-jobs-data-says-the-hike-is-still-coming-202610011351"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ghiles Guezout"
        source_url: "https://www.fxstreet.com/analysis/markets-are-pricing-a-fed-pause-the-jobs-data-says-the-hike-is-still-coming-202610011351"
        retrieved_at: "2026-10-01T15:03:15+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via FRED; the 4.0-4.25% implied range reflects the market absorbing both the inflation undershoot and the soft labor print simultaneously."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ghiles Guezout: Markets are pricing a Fed pause. The jobs data says the hike is still"
    url: "https://www.fxstreet.com/analysis/markets-are-pricing-a-fed-pause-the-jobs-data-says-the-hike-is-still-coming-202610011351"
    published_at: "2026-10-01T00:00:00.000Z"
    retrieved_at: "2026-10-01T15:03:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
