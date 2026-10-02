---
signal_id: "CMSIG2026100103"
signal_slug: "oct-fed-funds-upper-bound-4-0-4-25-ladder-86-23-2026-10-01"
headline: "Oct Fed funds upper bound 4.0-4.25%: ladder 86%/23%"
semantic_title: "October Fed funds upper bound priced near 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-01T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "October 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.23
  volume_24h_usd: 23.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Ladder shows 86% odds the October upper bound lands above 4.0%, but only 23% above 4.25%, implying a 4.0-4.25% modal outcome."
  - "The news article argues jobs data favors a hike, but the ladder's sharp drop at 4.25% shows the market is not fully buying that case."
  - "Compare the companion ladder (CM-EVT-6BS28TS762) which shows only 28% above 4.0% for a different meeting horizon, suggesting the market sees any hike as near-term not sustained."
  - "Resolves via the Federal Reserve's official rate decision announcement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "FXStreet reports markets have shifted toward pricing a Fed pause at the October meeting despite stronger jobs data signaling a hike may still come."
    publisher: "Ghiles Guezout"
    published_at: "2026-10-01T00:00:00.000Z"
    source_url: "https://www.fxstreet.com/analysis/markets-are-pricing-a-fed-pause-the-jobs-data-says-the-hike-is-still-coming-202610011351"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ghiles Guezout"
        source_url: "https://www.fxstreet.com/analysis/markets-are-pricing-a-fed-pause-the-jobs-data-says-the-hike-is-still-coming-202610011351"
        retrieved_at: "2026-10-02T07:47:52+00:00"
  - type: "pm_response"
    notes: "Ladder carried on Kalshi equivalent data; the gap between 86% above 4.0% and 23% above 4.25% is the key pause-vs-hike dividing line."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ghiles Guezout: Markets are pricing a Fed pause. The jobs data says the hike is still"
    url: "https://www.fxstreet.com/analysis/markets-are-pricing-a-fed-pause-the-jobs-data-says-the-hike-is-still-coming-202610011351"
    published_at: "2026-10-01T00:00:00.000Z"
    retrieved_at: "2026-10-02T07:47:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
