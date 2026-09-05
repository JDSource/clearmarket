---
signal_id: "CMSIG2026090403"
signal_slug: "unemployment-above-4-5-before-2027-16-implied-2026-09-04"
headline: "Unemployment above 4.5% before 2027: 16% implied"
semantic_title: "Unemployment topping 4.5 percent before 2027 stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T00:00:00.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak unemployment rate before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-4.5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.16
  volume_24h_usd: 18.97
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-09T15:00:00Z"
bullets:
  - "The ladder implies only 16% odds that unemployment will exceed 4.5% before 2027, with probabilities collapsing rapidly above that, 7% at 4.8%, 5% at 5.5%."
  - "August unemployment printed at 4.1%, consistent with the ladder's heavy mass below 4.5%; the strong hiring data supports that low-tail reading."
  - "The distribution's long right tail, 3% at 15%, 3% at 17%, 3% at 20%, reflects residual but small catastrophic-scenario pricing."
  - "A companion ladder (CM-EVT-2X91TW50H2) shows 67% odds unemployment stays above 4.1% in October, suggesting the market sees the current 4.1% reading as near the floor, not a peak."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "August jobs report confirmed unemployment at 4.1% with 162,000 positions added, beating all forecasts."
    publisher: "Eric Revell"
    published_at: "2026-09-04T00:00:00.000Z"
    source_url: "https://www.foxbusiness.com/economy/us-jobs-report-august-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eric Revell"
        source_url: "https://www.foxbusiness.com/economy/us-jobs-report-august-2026"
        retrieved_at: "2026-09-05T11:34:19+00:00"
  - type: "pm_response"
    notes: "Resolution source is unspecified on the peak-unemployment ladder; the October above-4.1% contract uses the same underlying BLS U-3 series."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eric Revell: August jobs report: US adds 162,000 positions, unemployment at 4.1% |"
    url: "https://www.foxbusiness.com/economy/us-jobs-report-august-2026"
    published_at: "2026-09-04T00:00:00.000Z"
    retrieved_at: "2026-09-05T11:34:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
