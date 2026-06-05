---
signal_id: "CMSIG2026060302"
signal_slug: "may-2026-nonfarm-payrolls-implied-90k-100k-kalshi-2026-06-03"
headline: "May 2026 nonfarm payrolls implied 90K-100K: Kalshi"
semantic_title: "May 2026 payroll consensus anchors near 90K-100K jobs"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T12:15:00.000Z"
event_id: "CM-EVT-QH49Q7F1N3"
event_slug: "kxpayrolls-26may"
event_question: "May 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26MAY-T100000"
  question_raw: "Will above 100000 jobs be added in May 2026?"
  current_price: 0.41
  volume_24h_usd: 2088.9
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau Of Labor Statistics"
  resolves_at: "2026-06-05T14:00:00Z"
bullets:
  - "Kalshi pins May 2026 nonfarm payrolls in the 90K-100K range: 53% above 90K but only 41% above 100K."
  - "ADP's 122K print is above the Kalshi modal range, suggesting official payrolls could surprise to the upside relative to current market pricing."
  - "Separately, rising jobless claims (Story 7) and the Challenger report showing 97K job cuts in May (Story 8) argue the ADP beat may not fully carry into the BLS headline."
  - "The Kalshi contract resolves via FRED/BLS official nonfarm payrolls data; the BLS and ADP series regularly diverge, limiting ADP's predictive edge."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ADP reported 122,000 private-sector jobs added in May, above the depressed consensus, ahead of Friday's official nonfarm payrolls release."
    publisher: "ADP, Inc."
    published_at: "2026-06-03T12:15:00.000Z"
    source_url: "https://www.prnewswire.com/news-releases/adp-national-employment-report-private-sector-employment-increased-by-122-000-jobs-in-may-annual-pay-was-up-4-4-302790127.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ADP, Inc."
        source_url: "https://www.prnewswire.com/news-releases/adp-national-employment-report-private-sector-employment-increased-by-122-000-jobs-in-may-annual-pay-was-up-4-4-302790127.html"
        retrieved_at: "2026-06-05T11:24:05+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via fred.stlouisfed.org BLS nonfarm payroll release; ADP is a leading but imperfect predictor of the official figure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ADP, Inc.: ADP National Employment Report: Private Sector Employment Increased by"
    url: "https://www.prnewswire.com/news-releases/adp-national-employment-report-private-sector-employment-increased-by-122-000-jobs-in-may-annual-pay-was-up-4-4-302790127.html"
    published_at: "2026-06-03T12:15:00.000Z"
    retrieved_at: "2026-06-05T11:24:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
