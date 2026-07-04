---
signal_id: "CMSIG2026070203"
signal_slug: "sept-2026-cpi-monthly-gain-seen-at-0-3-0-4-kalshi-2026-07-02"
headline: "Sept 2026 CPI monthly gain seen at 0.3-0.4%: Kalshi"
semantic_title: "September CPI monthly gain consensus wavers near 0.30-0.40 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-02T10:04:09.037Z"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "CPI monthly change, September 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.4"
  question_raw: "Will CPI rise more than 0.4% in September 2026?"
  current_price: 0.37
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-10-14T13:56:00Z"
bullets:
  - "Kalshi ladder prices 52% on CPI rising more than 0.3% in September 2026 and only 37% above 0.4%, implying a modal range of 0.30-0.40%."
  - "The soft jobs print shifts Fed attention to inflation, and September CPI pricing reflects continued above-consensus monthly gains well past summer."
  - "August 2026 CPI ladder (CM-EVT-D057W6W251) implies 0.10-0.20% for that month, suggesting markets see a modest reacceleration into September."
  - "Resolves via the Bureau of Labor Statistics CPI monthly change figure for September 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A cooler June jobs report is expected to keep the Fed focused on inflation rather than labor market concerns, with analysts watching the CPI trajectory closely."
    publisher: "finance.yahoo.com"
    published_at: "2026-07-02T10:04:09.037Z"
    source_url: "https://finance.yahoo.com/economy/policy/article/cooler-june-jobs-report-to-keep-fed-focused-on-inflation-with-possibility-of-hikes-later-this-year-124547980.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "finance.yahoo.com"
        source_url: "https://finance.yahoo.com/economy/policy/article/cooler-june-jobs-report-to-keep-fed-focused-on-inflation-with-possibility-of-hikes-later-this-year-124547980.html"
        retrieved_at: "2026-07-04T10:05:12+00:00"
  - type: "pm_response"
    notes: "Kalshi's September CPI ladder shows the market is not pricing a return to 2% inflation dynamics through the third quarter of 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "finance.yahoo.com: Cooler June jobs report to keep Fed focused on inflation, with ..."
    url: "https://finance.yahoo.com/economy/policy/article/cooler-june-jobs-report-to-keep-fed-focused-on-inflation-with-possibility-of-hikes-later-this-year-124547980.html"
    published_at: "2026-07-02T10:04:09.037Z"
    retrieved_at: "2026-07-04T10:05:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
