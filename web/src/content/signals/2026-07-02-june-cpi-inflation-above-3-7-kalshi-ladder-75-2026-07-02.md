---
signal_id: "CMSIG2026070202"
signal_slug: "june-cpi-inflation-above-3-7-kalshi-ladder-75-2026-07-02"
headline: "June CPI inflation above 3.7%: Kalshi ladder 75%"
semantic_title: "CPI above 3.7 percent for June anchors in prediction pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-02T10:04:09.037Z"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "CPI year-over-year rate for year ending June 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.25
  volume_24h_usd: 875.61
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi ladder prices 75% on CPI above 3.7% and 25% above 3.8%, implying a modal range of 3.70-3.80% for the year ending June 2026."
  - "News framing a stagflation scenario is consistent with the market holding above 3.7% with only a thin tail pricing 3.80% or higher."
  - "August 2026 CPI ladder (CM-EVT-D057W6W251) implies 0.10-0.20% monthly gain, suggesting markets see inflation easing only gradually."
  - "Resolves via the Bureau of Labor Statistics CPI release for the 12-month period ending June 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Headlines warn of a Fed nightmare scenario -- weak jobs paired with elevated inflation -- as June payrolls missed badly while price pressures remain sticky."
    publisher: "investing.com"
    published_at: "2026-07-02T10:04:09.037Z"
    source_url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
        retrieved_at: "2026-07-04T10:05:12+00:00"
  - type: "pm_response"
    notes: "Kalshi's CPI ladder reflects persistent above-target inflation pricing even as the labor market softens, consistent with the stagflation narrative in the news."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Fed's Nightmare Scenario Has Arrived: Weak Jobs, High Inflation"
    url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
    published_at: "2026-07-02T10:04:09.037Z"
    retrieved_at: "2026-07-04T10:05:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
