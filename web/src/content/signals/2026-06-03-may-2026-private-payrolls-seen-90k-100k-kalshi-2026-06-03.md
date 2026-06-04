---
signal_id: "CMSIG2026060303"
signal_slug: "may-2026-private-payrolls-seen-90k-100k-kalshi-2026-06-03"
headline: "May 2026 private payrolls seen 90k-100k: Kalshi"
semantic_title: "Private payrolls above 100K in May sits near a coin flip"
telemetry: "Kalshi 41%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T12:15:00.000Z"
event_id: "CM-EVT-QH49Q7F1N3"
event_slug: "kxpayrolls-26may"
event_question: "May 2026 private payrolls added"
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
  - "Kalshi implies May payrolls in the 90k-100k range: 53% above 90k but only 41% above 100k."
  - "The ADP print of 122k prints above the Kalshi market-implied midpoint, suggesting the prediction market was positioned cautiously."
  - "The 80% probability above 30k confirms the market ruled out a severe miss well before the print."
  - "A companion ladder for October 2026 payrolls implies 70k-80k, suggesting market expects hiring to decelerate further."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ADP reported May private sector employment rose 122,000, with annual pay up 4.4% year-over-year."
    publisher: "ADP, Inc."
    published_at: "2026-06-03T12:15:00.000Z"
    source_url: "https://www.prnewswire.com/news-releases/adp-national-employment-report-private-sector-employment-increased-by-122-000-jobs-in-may-annual-pay-was-up-4-4-302790127.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ADP, Inc."
        source_url: "https://www.prnewswire.com/news-releases/adp-national-employment-report-private-sector-employment-increased-by-122-000-jobs-in-may-annual-pay-was-up-4-4-302790127.html"
        retrieved_at: "2026-06-04T11:14:54+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via fred.stlouisfed.org official payroll data release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ADP, Inc.: ADP National Employment Report: Private Sector Employment Increased by"
    url: "https://www.prnewswire.com/news-releases/adp-national-employment-report-private-sector-employment-increased-by-122-000-jobs-in-may-annual-pay-was-up-4-4-302790127.html"
    published_at: "2026-06-03T12:15:00.000Z"
    retrieved_at: "2026-06-04T11:14:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
