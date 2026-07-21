---
signal_id: "CMSIG2026071804"
signal_slug: "oct-2026-payrolls-seen-70k-80k-kalshi-ladder-2026-07-18"
headline: "Oct 2026 payrolls seen 70K-80K: Kalshi ladder"
semantic_title: "October payrolls implied range holds near 70K-80K in Kalshi pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-18T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payroll change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder implies October payrolls in the 70K-80K range: 50% probability above 70K, 45% above 80K."
  - "June's 57K print, while below expectations, is broadly consistent with a market already pricing a soft but positive payroll regime ahead."
  - "The distribution shows 85% above minus 25K, meaning outright contraction is heavily discounted despite the weak June read."
  - "Resolves via Bureau of Labor Statistics nonfarm payroll release for October 2026; benchmark revisions could shift final settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June 2026 jobs report showed only 57,000 jobs added, missing expectations, with unemployment edging down to 4.2%."
    publisher: "treeplmn.com"
    published_at: "2026-07-18T00:00:00.000Z"
    source_url: "https://treeplmn.com/article/u-s-jobs-report-june-2026-economic-outlook-and-market-reactions"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "treeplmn.com"
        source_url: "https://treeplmn.com/article/u-s-jobs-report-june-2026-economic-outlook-and-market-reactions"
        retrieved_at: "2026-07-21T10:22:25+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder for October payrolls; June's weak 57K actual is softer than the 70K-80K market-implied forward range, suggesting some downside risk to later months."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "treeplmn.com: U.S. Jobs Report: June 2026 - Economic Outlook and Market Reactions (2"
    url: "https://treeplmn.com/article/u-s-jobs-report-june-2026-economic-outlook-and-market-reactions"
    published_at: "2026-07-18T00:00:00.000Z"
    retrieved_at: "2026-07-21T10:22:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
