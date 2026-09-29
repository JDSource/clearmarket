---
signal_id: "CMSIG2026092702"
signal_slug: "fed-funds-upper-bound-above-4-25-kalshi-53-volume-up-82x-2026-09-27"
headline: "Fed funds upper bound above 4.25%: Kalshi 53%, volume up 82x"
semantic_title: "Fed funds upper bound stays near 4.25 percent after hike talk"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound post-meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.50"
  question_raw: "Will the upper bound of the federal funds rate be above 4.50% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.04
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound most likely in the 4.25-4.50% range: 53% above 4.25% but only 4% above 4.50%."
  - "Trading volume on the Kalshi ladder jumped 82.5x day-over-day, consistent with fresh positioning as hike-path news intensified."
  - "The market is not fully pricing a move above 4.50%, pushing back against the more aggressive hike narratives circulating in media."
  - "Resolution depends on the official Federal Reserve post-meeting statement, with the October FOMC meeting now flagged as the hinge point by Citi."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Reuters reports investors are assessing employment and inflation data this week to gauge the probability of a sharper rate-hike path."
    publisher: "Reuters"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
        retrieved_at: "2026-09-29T14:34:30+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on the federal funds upper bound; 82.5x volume surge is a strong signal of new positioning tied to this week's macro data slate."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: Inflation's Impact on Interest Rates and Stocks - GV Wire"
    url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-29T14:34:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
