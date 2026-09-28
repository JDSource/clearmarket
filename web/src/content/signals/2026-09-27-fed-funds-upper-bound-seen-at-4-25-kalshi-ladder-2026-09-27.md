---
signal_id: "CMSIG2026092702"
signal_slug: "fed-funds-upper-bound-seen-at-4-25-kalshi-ladder-2026-09-27"
headline: "Fed funds upper bound seen at 4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays favored at 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after next Fed meeting"
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
  - "Kalshi ladder puts 60% on the upper bound above 4.25% but only 4% above 4.50%, pinning the consensus at 4.25%."
  - "News flow around rate-hike risk is consistent with this pricing: hawkish Fed bets are building but markets are not pricing an outright 4.50% move."
  - "The hard cliff from 60% to 4% between the 4.25% and 4.50% strikes signals the market is pricing a single-step hike as the base case, not back-to-back moves."
  - "Cross-check: the separate 2-year UST par yield ladder (CM-EVT-FQWTB38T69) prices above 4.70% at 99%, consistent with a funds rate anchored near 4.25%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Investors are assessing employment and inflation data to gauge chances of a sharper Fed rate hike trajectory."
    publisher: "Reuters"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
        retrieved_at: "2026-09-28T16:24:04+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on the federal funds upper bound resolves via Federal Reserve announcement; current distribution strongly favors a 4.25% ceiling."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: Inflation's Impact on Interest Rates and Stocks - GV Wire"
    url: "https://gvwire.com/2026/09/27/jobs-report-inflation-data-to-test-us-rate-path-economic-strength/"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-28T16:24:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
