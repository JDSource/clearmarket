---
signal_id: "CMSIG2026081002"
signal_slug: "fed-funds-upper-bound-post-meeting-kalshi-ladder-3-75-4-2026-08-10"
headline: "Fed funds upper bound post-meeting: Kalshi ladder 3.75-4%"
semantic_title: "Fed funds upper bound seen near 3.75 to 4 percent after next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-10T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after next FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.23
  volume_24h_usd: 9.36
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the next-meeting Fed funds upper bound in the 3.75-4.00% range: 84% above 3.50%, 53% above 3.75%, only 23% above 4.00%."
  - "The soft jobs report and in-line CPI are consistent with market indecision, the distribution is wide, with meaningful probability spread across three adjacent strikes."
  - "Near-term ladder CM-EVT-4ZQLQPNH91 prices 98% above 3.50% but only 36% above 3.75%, suggesting the next meeting is seen as more likely to hold than hike while this ladder implies a subsequent meeting hike is more credible."
  - "Resolution follows the Federal Reserve's official rate decision announcement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Investors focused on the July inflation print as the decisive data point following a surprise job-loss report, with rate-path uncertainty at its highest in months."
    publisher: "William Edwards"
    published_at: "2026-08-10T00:00:00.000Z"
    source_url: "https://www.businessinsider.com/inflation-cpi-july-stock-market-warsh-fed-rates-jobs-report-2026-8"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "William Edwards"
        source_url: "https://www.businessinsider.com/inflation-cpi-july-stock-market-warsh-fed-rates-jobs-report-2026-8"
        retrieved_at: "2026-08-13T09:07:47+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution; the wide spread across 3.50-4.00% reflects genuine two-sided uncertainty heading into the September FOMC."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "William Edwards: Investors' Eyes Are on Inflation This Week After Dismal Jobs Report -"
    url: "https://www.businessinsider.com/inflation-cpi-july-stock-market-warsh-fed-rates-jobs-report-2026-8"
    published_at: "2026-08-10T00:00:00.000Z"
    retrieved_at: "2026-08-13T09:07:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
