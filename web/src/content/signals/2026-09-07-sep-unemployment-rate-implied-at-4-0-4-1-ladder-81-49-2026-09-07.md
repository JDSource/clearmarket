---
signal_id: "CMSIG2026090703"
signal_slug: "sep-unemployment-rate-implied-at-4-0-4-1-ladder-81-49-2026-09-07"
headline: "Sep unemployment rate implied at 4.0-4.1%: ladder 81%/49%"
semantic_title: "September unemployment rate seen near 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "September 2026 unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.1"
  question_raw: "Will the unemployment rate (U-3) be above 4.1% in September?"
  current_price: 0.49
  volume_24h_usd: 58.8
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Ladder implies September U-3 unemployment in the 4.0-4.1% range: 81% above 4.0% but only 49% above 4.1%."
  - "Strong August hiring is consistent with unemployment staying anchored near 4.0%, not rising, the ladder reflects that signal."
  - "The near-coin-flip at the 4.1% strike shows genuine uncertainty about whether jobs strength compresses unemployment below the prior trend."
  - "A companion ladder (CM-EVT-RBY62SKLC0) prices only 16% on unemployment reaching 4.5% before 2027, suggesting the market sees no near-term spike risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "August NFP crushed forecasts at 162,000 jobs added, reigniting debate about labor market resilience and the unemployment rate trajectory."
    publisher: "fxstreet.com"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://www.fxstreet.com/news/united-states-dollar-index-strengthens-above-9900-as-robust-us-jobs-data-boosts-fed-rate-hike-bets-202609070225"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxstreet.com"
        source_url: "https://www.fxstreet.com/news/united-states-dollar-index-strengthens-above-9900-as-robust-us-jobs-data-boosts-fed-rate-hike-bets-202609070225"
        retrieved_at: "2026-09-07T13:54:18+00:00"
  - type: "pm_response"
    notes: "Ladder resolves against the BLS Employment Situation release for September 2026; the tight 4.0-4.1% implied range reflects the post-NFP recalibration."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxstreet.com: United States Dollar Index strengthens above 99.00 as robust US jobs d"
    url: "https://www.fxstreet.com/news/united-states-dollar-index-strengthens-above-9900-as-robust-us-jobs-data-boosts-fed-rate-hike-bets-202609070225"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-07T13:54:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
