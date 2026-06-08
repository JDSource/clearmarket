---
signal_id: "CMSIG2026060503"
signal_slug: "unemployment-peak-above-5-before-2027-kalshi-24-2026-06-05"
headline: "Unemployment peak above 5% before 2027: Kalshi 24%"
semantic_title: "Unemployment spike above 5 percent remains a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-05T14:01:00.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak U.S. unemployment rate before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.242
  volume_24h_usd: 142.95
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices only 24% on unemployment exceeding 5% before 2027; above 6% collapses to 8%."
  - "The strong May print is consistent with the low-tail pricing, markets see a spike above 6-7% as a remote scenario at 7-8%."
  - "Tech layoff and white-collar layoff markets (CM-EVT-ZTGN9MPFL9 at 89%, CM-EVT-0QDTY1D1Y1 at 72%) suggest sectoral stress that has not yet moved the aggregate unemployment needle."
  - "Resolves via FRED/BLS unemployment data; contract covers any monthly reading above each threshold reported before January 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "172,000 jobs added in May showing labor market resilience even as the Iran war weighs on sentiment."
    publisher: "pbs.org"
    published_at: "2026-06-05T14:01:00.000Z"
    source_url: "https://www.pbs.org/newshour/economy/172000-jobs-added-in-may-showing-market-resilience-despite-iran-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/economy/172000-jobs-added-in-may-showing-market-resilience-despite-iran-war"
        retrieved_at: "2026-06-08T12:25:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via fred.stlouisfed.org; the wide gap between 24% at 5% and 8% at 6% reflects the current strong-labor-market baseline."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: 172,000 jobs added in May, showing market resilience despite Iran war"
    url: "https://www.pbs.org/newshour/economy/172000-jobs-added-in-may-showing-market-resilience-despite-iran-war"
    published_at: "2026-06-05T14:01:00.000Z"
    retrieved_at: "2026-06-08T12:25:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
