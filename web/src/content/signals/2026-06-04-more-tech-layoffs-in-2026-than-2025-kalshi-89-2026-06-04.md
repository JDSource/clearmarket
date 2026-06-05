---
signal_id: "CMSIG2026060403"
signal_slug: "more-tech-layoffs-in-2026-than-2025-kalshi-89-2026-06-04"
headline: "More tech layoffs in 2026 than 2025: Kalshi 89%"
semantic_title: "Tech layoff consensus solidifies above 2025 levels"
telemetry: "Kalshi 89%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-06-04T09:30:35.000Z"
event_id: "CM-EVT-ZTGN9MPFL9"
event_slug: "kxlayoffsyinfo-26"
event_question: "Will there be more tech layoffs in 2026 than in 2025?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLAYOFFSYINFO-26-494000"
  question_raw: "More tech layoffs in 2026 than in 2025?"
  current_price: 0.889
  volume_24h_usd: 1614.78
  arbitration_model: "kalshi_staff"
  resolution_source: "fred.stlouisfed.org"
  resolves_at: "2027-03-01T15:00:00Z"
bullets:
  - "Kalshi places 89% odds that 2026 tech layoffs exceed 2025 totals, resolving via FRED data."
  - "The Challenger report showing tech cuts at their highest since 2023 is consistent with this elevated probability."
  - "AI-driven displacement is now the stated primary reason for cuts three months running, reinforcing the structural rather than cyclical read."
  - "A companion Kalshi contract on white-collar layoffs broadly (CM-EVT-0QDTY1D1Y1) sits at 72%, showing markets view tech as the hardest-hit segment within a wider white-collar trend."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Challenger, Gray and Christmas reported May job cuts rose 16% from April, with tech cuts at their highest since 2023 and AI cited as the lead reason for a third straight month."
    publisher: "Nicole Lobdell"
    published_at: "2026-06-04T09:30:35.000Z"
    source_url: "https://www.challengergray.com/blog/challenger-report-may-job-cuts-rise-16-from-april-highest-may-total-since-2020/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Nicole Lobdell"
        source_url: "https://www.challengergray.com/blog/challenger-report-may-job-cuts-rise-16-from-april-highest-may-total-since-2020/"
        retrieved_at: "2026-06-05T11:24:05+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via fred.stlouisfed.org annual layoff data; full-year comparison requires waiting until the 2026 calendar year closes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Nicole Lobdell: Challenger Report: May Job Cuts Rise 16% from April; Highest May Total"
    url: "https://www.challengergray.com/blog/challenger-report-may-job-cuts-rise-16-from-april-highest-may-total-since-2020/"
    published_at: "2026-06-04T09:30:35.000Z"
    retrieved_at: "2026-06-05T11:24:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
