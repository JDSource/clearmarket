---
signal_id: "CMSIG2026102004"
signal_slug: "october-2026-job-adds-kalshi-ladder-70k-80k-implied-2026-10-20"
headline: "October 2026 job adds: Kalshi ladder 70K-80K implied"
semantic_title: "October payrolls seen in the 70K-80K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payroll additions"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.4
  volume_24h_usd: 4.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder implies October payrolls in the 70,000-80,000 range: 53% probability above 70K, only 40% above 80K."
  - "September labor market described as strong; the ladder suggests the market expects a meaningful deceleration by October, not a continuation of the same pace."
  - "The 85% probability above zero and 61% above 50K show the market firmly rules out job losses while still pricing in a softer month."
  - "Resolves via official BLS payroll count for October 2026; any downward revision to prior months could shift the distribution at settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Analyst commentary describes September employment as strong enough to confirm full employment and give the Fed cover to focus on inflation rather than labor market risk."
    publisher: "Yelena Shulyatyeva"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yelena Shulyatyeva"
        source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
        retrieved_at: "2026-10-21T13:24:06+00:00"
  - type: "pm_response"
    notes: "The Kalshi payroll ladder carries no elevated volume flag, so the current distribution reflects pre-existing positioning rather than a fresh surge of trading activity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yelena Shulyatyeva: Labor Market Strong Enough for Fed to Focus on Inflation"
    url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-21T13:24:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
