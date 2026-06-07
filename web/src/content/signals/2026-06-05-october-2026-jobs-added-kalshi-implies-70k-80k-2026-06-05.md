---
signal_id: "CMSIG2026060502"
signal_slug: "october-2026-jobs-added-kalshi-implies-70k-80k-2026-06-05"
headline: "October 2026 jobs added: Kalshi implies 70K-80K"
semantic_title: "October payrolls consensus anchors in the 70K-80K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-05T12:35:00.000Z"
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
  - "Kalshi ladder pins October 2026 payroll additions in the 70K-80K implied range; 79% above zero, only 24% above 100K."
  - "May's 172,000 print is well above the market's forward implied range for October, suggesting the market expects some moderation ahead."
  - "The sharp drop from 54% at the 50K strike to 24% at 100K marks where the distribution thins, showing meaningful tail risk below 100K."
  - "Resolves via Bureau of Labor Statistics monthly Employment Situation release for October 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May 2026 payrolls came in at 172,000, beating the 105,000 consensus, sustaining a three-month streak of solid job gains."
    publisher: "cbsnews.com"
    published_at: "2026-06-05T12:35:00.000Z"
    source_url: "https://www.cbsnews.com/news/jobs-report-today-may-2026-economy-iran-bls/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/jobs-report-today-may-2026-economy-iran-bls/"
        retrieved_at: "2026-06-07T10:26:16+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution implies the market is not extrapolating May's strength into autumn, pricing a notably lower central tendency for October."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Employers added 172,000 jobs in May, surging past expectations as labo"
    url: "https://www.cbsnews.com/news/jobs-report-today-may-2026-economy-iran-bls/"
    published_at: "2026-06-05T12:35:00.000Z"
    retrieved_at: "2026-06-07T10:26:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
