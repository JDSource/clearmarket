---
signal_id: "CMSIG2026101203"
signal_slug: "fed-funds-upper-bound-post-october-kalshi-4-0-4-25-2026-10-12"
headline: "Fed funds upper bound post-October: Kalshi 4.0-4.25%"
semantic_title: "Markets back a single hike, pricing out aggressive tightening"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-12T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after October meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts the Fed funds upper bound at 4.0-4.25%: 81% above 4.0% but only 19% above 4.25%, aligned with Natixis's single-hike-possible, hold-likely view."
  - "Natixis's base case of a hold in October is consistent with the market pricing: only 19% probability the upper bound exceeds 4.25% after the October 27-28 meeting."
  - "September CPI, due Wednesday, is the immediate resolution catalyst; Natixis's 0.19% core estimate would keep the inflation path manageable."
  - "The Kalshi contract on a Fed cut greater than 25 basis points in 2026 sits at 2%, confirming the distribution is skewed toward hikes or holds, not easing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Natixis expects September core CPI at 0.19% month-on-month and sees August's inflation spike as a one-off, with the Fed holding in October and a possible lone hike if inflation persists."
    publisher: "fxbrokertrust.com"
    published_at: "2026-10-12T00:00:00.000Z"
    source_url: "https://www.fxbrokertrust.com/insights/natixis-september-cpi-may-meet-expectations-lone-rate-hike-possible"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxbrokertrust.com"
        source_url: "https://www.fxbrokertrust.com/insights/natixis-september-cpi-may-meet-expectations-lone-rate-hike-possible"
        retrieved_at: "2026-10-12T07:49:04+00:00"
  - type: "pm_response"
    notes: "Kalshi's Fed funds ladder is the primary venue tracking this outcome, with resolution tied directly to the Federal Reserve's post-meeting rate announcement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxbrokertrust.com: Natixis: September CPI May Meet Expectations, Lone Rate Hike Possible"
    url: "https://www.fxbrokertrust.com/insights/natixis-september-cpi-may-meet-expectations-lone-rate-hike-possible"
    published_at: "2026-10-12T00:00:00.000Z"
    retrieved_at: "2026-10-12T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
