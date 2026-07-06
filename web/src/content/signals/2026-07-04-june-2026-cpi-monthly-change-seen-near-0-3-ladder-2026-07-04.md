---
signal_id: "CMSIG2026070404"
signal_slug: "june-2026-cpi-monthly-change-seen-near-0-3-ladder-2026-07-04"
headline: "June 2026 CPI monthly change seen near -0.3%: ladder"
semantic_title: "June CPI monthly change consensus anchors near negative 0.3 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-04T17:14:00.000Z"
event_id: "CM-EVT-KJ2LGV0M57"
event_slug: "kxcpi-26jun"
event_question: "June 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26JUN-T-0.2"
  question_raw: "Will CPI rise more than -0.2% in June 2026?"
  current_price: 0.34
  volume_24h_usd: 578.03
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-14T13:56:00Z"
bullets:
  - "Ladder implies June CPI monthly change near -0.3%: 82% probability above -0.3% but only 34% above -0.2%."
  - "A soft labor market print supports a benign or negative monthly CPI read; the ladder distribution is consistent with disinflation expectations."
  - "The sharp drop from 82% to 34% between the -0.3% and -0.2% strikes signals the market has strong conviction around that narrow band."
  - "Resolves via the Bureau of Labor Statistics CPI release for June 2026; seasonal adjustment methodology can shift the final monthly figure."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June payrolls missed badly at 57,000 versus a 115,000 forecast, yet the Dow hit an all-time high, with attention now on inflation data."
    publisher: "talkmarkets.com"
    published_at: "2026-07-04T17:14:00.000Z"
    source_url: "https://talkmarkets.com/article/june-jobs-report-miss-57000-payrolls-vs-115000-forecast-so-why-did-the-dow-hit-an-all-time-high-1783179187"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "talkmarkets.com"
        source_url: "https://talkmarkets.com/article/june-jobs-report-miss-57000-payrolls-vs-115000-forecast-so-why-did-the-dow-hit-an-all-time-high-1783179187"
        retrieved_at: "2026-07-06T12:00:14+00:00"
  - type: "pm_response"
    notes: "The CPI ladder shows tight market conviction around a near-zero or slightly negative monthly print, complementing the weak labor market narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "talkmarkets.com: June Jobs Report Miss: 57,000 Payrolls Vs. 115,000 Forecast. So Why Di"
    url: "https://talkmarkets.com/article/june-jobs-report-miss-57000-payrolls-vs-115000-forecast-so-why-did-the-dow-hit-an-all-time-high-1783179187"
    published_at: "2026-07-04T17:14:00.000Z"
    retrieved_at: "2026-07-06T12:00:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
