---
signal_id: "CMSIG2026080701"
signal_slug: "sept-2026-payrolls-ladder-implies-50k-60k-range-2026-08-07"
headline: "Sept 2026 payrolls: ladder implies 50K-60K range"
semantic_title: "September jobs outlook stays cautious after shock print"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T15:31:12.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 nonfarm payroll change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T60000"
  question_raw: "Will above 60000 jobs be added in September 2026?"
  current_price: 0.44
  volume_24h_usd: 279.59
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Ladder pins September 2026 payrolls in the 50K-60K range: 93% above -25K, 83% above zero, but only 44% above 60K."
  - "July came in at -23K vs. +80K expected; the ladder's subdued September outlook is consistent with a weakening trend."
  - "October ladder (CM-EVT-6CSLHX0K76) implies 70K-80K, suggesting markets see July as a one-month shock rather than a sustained collapse."
  - "Both ladders resolve via BLS Employment Situation releases; benchmark revisions could shift implied ranges materially."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "July 2026 nonfarm payrolls fell 23,000 against an 80,000 consensus forecast, with 103,000 in downward revisions to prior months."
    publisher: "financefeeds.com"
    published_at: "2026-08-07T15:31:12.000Z"
    source_url: "https://financefeeds.com/july-jobs-report-payrolls-fall-september-fed-cut/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "financefeeds.com"
        source_url: "https://financefeeds.com/july-jobs-report-payrolls-fall-september-fed-cut/"
        retrieved_at: "2026-08-08T08:35:11+00:00"
  - type: "pm_response"
    notes: "Ladder distribution data via ClearMarket reference layer; no single-venue attribution available for these ladder events."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "financefeeds.com: https://financefeeds.com/july-jobs-report-payrolls-fall-september-fed-"
    url: "https://financefeeds.com/july-jobs-report-payrolls-fall-september-fed-cut/"
    published_at: "2026-08-07T15:31:12.000Z"
    retrieved_at: "2026-08-08T08:35:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
