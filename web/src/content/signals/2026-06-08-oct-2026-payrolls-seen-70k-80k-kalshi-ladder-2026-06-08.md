---
signal_id: "CMSIG2026060801"
signal_slug: "oct-2026-payrolls-seen-70k-80k-kalshi-ladder-2026-06-08"
headline: "Oct 2026 payrolls seen 70K-80K: Kalshi ladder"
semantic_title: "October jobs market-implied range anchors at 70K-80K"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T16:49:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payroll additions"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau Of Labor Statistics"
  resolves_at: "2026-11-06T15:00:00Z"
bullets:
  - "Kalshi ladder pins October 2026 payrolls in the 70K-80K range: 50% above 70K, only 45% above 80K."
  - "May's 172K print crushed the 85K forecast, yet the forward market implies a significant cooldown by October."
  - "The 50K strike sits at 54%, suggesting the market is not extrapolating May's strength into autumn."
  - "Resolution via Bureau of Labor Statistics Employment Situation release; the relevant month's data must be the official BLS print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May 2026 nonfarm payrolls came in at 172,000, more than double the 85,000 consensus forecast, with leisure, government, and healthcare leading gains."
    publisher: "seekingalpha.com"
    published_at: "2026-06-08T16:49:00.000Z"
    source_url: "https://seekingalpha.com/article/4912946-may-2026-employment-report-strong-strong-jobs"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "seekingalpha.com"
        source_url: "https://seekingalpha.com/article/4912946-may-2026-employment-report-strong-strong-jobs"
        retrieved_at: "2026-06-09T10:57:53+00:00"
  - type: "pm_response"
    notes: "Kalshi's October payroll ladder is consistent with a market discounting May as an outlier rather than a new trend."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "seekingalpha.com: May 2026 Employment Report - Strong, Strong Jobs | Seeking Alpha"
    url: "https://seekingalpha.com/article/4912946-may-2026-employment-report-strong-strong-jobs"
    published_at: "2026-06-08T16:49:00.000Z"
    retrieved_at: "2026-06-09T10:57:53+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
