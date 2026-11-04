---
signal_id: "CMSIG2026110403"
signal_slug: "oct-jobs-implied-60k-70k-adp-86k-beats-forecast-2026-11-04"
headline: "Oct jobs implied 60K-70K: ADP 86K beats forecast"
semantic_title: "ADP beat nudges payroll odds toward upper Kalshi range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-04T09:30:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T70000"
  question_raw: "Will above 70000 jobs be added in October 2026?"
  current_price: 0.46
  volume_24h_usd: 412.41
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder modal range for October payrolls sits at 60K-70K; the ADP beat of 86K lands above that central case."
  - "ADP print is consistent with the market's positive-growth bias, 91% of Kalshi ladder probability sits above zero, but the beat tests the upper tail."
  - "Only 33% probability priced above 100K; a strong NFP on Friday would be needed to push the distribution meaningfully rightward."
  - "Resolves via BLS Employment Situation release; ADP and BLS figures have diverged in recent months, limiting the signal value of the ADP beat alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ADP reported 86,000 private-sector jobs added in October, above the 69,000 consensus estimate."
    publisher: "FXStreet Team"
    published_at: "2026-11-04T09:30:00.000Z"
    source_url: "https://www.fxstreet.com/news/adp-employment-report-expected-to-show-slower-job-growth-in-october-202611040930"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "FXStreet Team"
        source_url: "https://www.fxstreet.com/news/adp-employment-report-expected-to-show-slower-job-growth-in-october-202611040930"
        retrieved_at: "2026-11-04T15:56:48+00:00"
  - type: "pm_response"
    notes: "Same Kalshi ladder as Story 2 (CM-EVT-6CSLHX0K76); ADP is a leading indicator, not the resolution source."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "FXStreet Team: Breaking: United States private sector employment rises by 86K in Octo"
    url: "https://www.fxstreet.com/news/adp-employment-report-expected-to-show-slower-job-growth-in-october-202611040930"
    published_at: "2026-11-04T09:30:00.000Z"
    retrieved_at: "2026-11-04T15:56:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
