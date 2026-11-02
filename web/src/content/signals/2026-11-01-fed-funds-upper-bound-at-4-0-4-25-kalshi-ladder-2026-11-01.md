---
signal_id: "CMSIG2026110101"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-11-01"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 4 percent after jobs data"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-01T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound following next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 132.6
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 4.0-4.25% range: 73% above 4.0%, but only 3% above 4.25%."
  - "Bloomberg reports a jobs pickup may keep the Fed on track to hike; the Kalshi distribution is consistent with one more hike being the modal outcome."
  - "The sharp drop from 73% to 3% between the 4.0% and 4.25% strikes signals the market sees the 4.0-4.25% band as a ceiling, not a floor."
  - "Chartstopper data (Story 8) separately notes December hike odds at 75%, closely aligned with the Kalshi ladder's implied range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A stronger-than-expected US jobs pickup is raising expectations the Fed will hike rates again, with the December decision now in focus."
    publisher: "Matthew Boesler, Craig Stirling"
    published_at: "2026-11-01T00:00:00.000Z"
    source_url: "https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Matthew Boesler, Craig Stirling"
        source_url: "https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again"
        retrieved_at: "2026-11-02T17:44:20+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the Fed's official policy announcement; the 4.0-4.25% range is the market's dominant scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Matthew Boesler, Craig Stirling: US Jobs Pickup May Keep Fed on Track to Hike Rates Again"
    url: "https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again"
    published_at: "2026-11-01T00:00:00.000Z"
    retrieved_at: "2026-11-02T17:44:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
