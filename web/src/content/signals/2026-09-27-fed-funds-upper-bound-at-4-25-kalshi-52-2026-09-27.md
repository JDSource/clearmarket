---
signal_id: "CMSIG2026092701"
signal_slug: "fed-funds-upper-bound-at-4-25-kalshi-52-2026-09-27"
headline: "Fed funds upper bound at 4.25%: Kalshi 52%"
semantic_title: "Fed funds upper bound prices in at 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.50"
  question_raw: "Will the upper bound of the federal funds rate be above 4.50% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.04
  volume_24h_usd: 5.95
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound at 4.25%, with 52% odds above 4.25% but only 4% above 4.50%, implying market sees 4.25% as the likely ceiling."
  - "Inflation and jobs-focused news flow is consistent with the ladder's near-50/50 split at 4.25%; the market is not yet committing to a further hike beyond that level."
  - "Volume surged 82.5x day over day on this Kalshi contract, a strong signal fresh capital is positioning around the October FOMC decision."
  - "The sharp drop from 52% at 4.25% to just 4% at 4.50% signals the market treats 4.50% as a tail scenario, not a base case, heading into key PCE and NFP prints."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Investors are watching employment and inflation data to assess chances of a sharper rate-hike trajectory, with markets already pricing more than 50% odds of a Fed hike at the October FOMC meeting."
    publisher: "Reuters"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
        retrieved_at: "2026-09-29T07:47:25+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Federal Reserve announcement; volume spike of 8150% day over day confirms this is the active focus for FOMC positioning."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: Inflation's Impact on Interest Rates and Stocks - GV Wire"
    url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-29T07:47:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
