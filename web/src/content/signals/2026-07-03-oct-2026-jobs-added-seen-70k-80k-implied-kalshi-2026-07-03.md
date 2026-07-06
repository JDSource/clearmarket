---
signal_id: "CMSIG2026070303"
signal_slug: "oct-2026-jobs-added-seen-70k-80k-implied-kalshi-2026-07-03"
headline: "Oct 2026 jobs added seen 70K-80K implied: Kalshi"
semantic_title: "October payrolls consensus wavers near 70K-80K implied range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-03T12:10:25.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "Jobs added in October 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2026-11-06T15:00:00Z"
bullets:
  - "Kalshi ladder implies October 2026 job additions in the 70,000-80,000 range: 50% above 70K but only 45% above 80K."
  - "June's 57,000 print, with 74,000 in prior-month revisions stripped out, signals a trend that the market has begun to reflect for later months."
  - "The 79% probability above zero jobs confirms no recession-level payroll contraction is priced for October, even as the trend has weakened."
  - "Resolves via the Bureau of Labor Statistics Employment Situation release for October 2026; benchmark revisions could shift the final figure."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June nonfarm payrolls came in at 57,000 with combined April-May downward revisions of 74,000, signaling a cooling labor market."
    publisher: "B&B Team"
    published_at: "2026-07-03T12:10:25.000Z"
    source_url: "https://banksandbankers.com/us-jobs-growth-june-2026-fed-rate-hike-september/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "B&B Team"
        source_url: "https://banksandbankers.com/us-jobs-growth-june-2026-fed-rate-hike-september/"
        retrieved_at: "2026-07-06T12:00:14+00:00"
  - type: "pm_response"
    notes: "Kalshi's October ladder shows the market embedding a subdued but positive jobs trend, not a contractionary scenario, following the June miss."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "B&B Team: US Jobs Growth Misses Forecast, Fed September Hike in Focus"
    url: "https://banksandbankers.com/us-jobs-growth-june-2026-fed-rate-hike-september/"
    published_at: "2026-07-03T12:10:25.000Z"
    retrieved_at: "2026-07-06T12:00:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
