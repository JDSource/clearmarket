---
signal_id: "CMSIG2026060306"
signal_slug: "may-2026-payrolls-implied-90k-100k-kalshi-ladder-2026-06-03"
headline: "May 2026 payrolls implied ~90K-100K: Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-06-03T12:15:23.000Z"
event_id: "CM-EVT-QH49Q7F1N3"
event_slug: "kxpayrolls-26may"
event_question: "May 2026 private payrolls (ADP)"
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
  - "Kalshi ladder implied May payrolls in the 90K-100K range: 53% above 90K, 41% above 100K, 29% above 125K."
  - "ADP's 122,000 print beat both the Kalshi market-implied midpoint and the Dow Jones 110K consensus."
  - "The 29% probability above 125K shows markets had already embedded some upside tail before the print."
  - "Companion October 2026 ladder (CM-EVT-6CSLHX0K76) implies a softer 70K-80K range, suggesting markets see May as a one-month beat, not a trend shift."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ADP reported 122,000 private-sector jobs added in May, beating the 110,000 consensus estimate."
    publisher: "Jeff Cox"
    published_at: "2026-06-03T12:15:23.000Z"
    source_url: "https://www.cnbc.com/2026/06/03/adp-jobs-report-may-2026-payrolls-increase-by-122000.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/06/03/adp-jobs-report-may-2026-payrolls-increase-by-122000.html"
        retrieved_at: "2026-06-04T03:24:20+00:00"
  - type: "pm_response"
    notes: "Kalshi's pre-print distribution undershot the ADP beat; the October ladder shows lingering caution about the labor market."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: ADP jobs report May 2026: Payrolls increase by 122,000"
    url: "https://www.cnbc.com/2026/06/03/adp-jobs-report-may-2026-payrolls-increase-by-122000.html"
    published_at: "2026-06-03T12:15:23.000Z"
    retrieved_at: "2026-06-04T03:24:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
