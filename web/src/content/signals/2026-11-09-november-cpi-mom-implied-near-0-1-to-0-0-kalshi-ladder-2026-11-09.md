---
signal_id: "CMSIG2026110903"
signal_slug: "november-cpi-mom-implied-near-0-1-to-0-0-kalshi-ladder-2026-11-09"
headline: "November CPI MoM implied near -0.1 to 0.0%: Kalshi ladder"
semantic_title: "Month-over-month CPI seen flat to slightly negative"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-09T00:00:00.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "CPI month-over-month change (November 2026)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T0.0"
  question_raw: "Will CPI rise more than 0.0% in November 2026?"
  current_price: 0.29
  volume_24h_usd: 1078.73
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "Kalshi ladder implies November CPI month-over-month in the -0.1 to 0.0% range: 56% at -0.1%, 29% at 0.0%, only 16% at 0.1% or above."
  - "Trading volume on this contract rose 6,389% day-over-day, confirming the CPI release is drawing the largest fresh prediction-market attention of the cycle."
  - "The implied flat-to-negative monthly reading sits at odds with the 'persistent inflation' narrative in analyst commentary, suggesting the market is not fully pricing in shelter stickiness."
  - "Resolution depends on the Bureau of Labor Statistics monthly CPI release; a reading at or below zero would validate the modal Kalshi pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The NY Fed's October consumer survey showed stable inflation expectations even as labor market sentiment deteriorated."
    publisher: "newyorkfed.org"
    published_at: "2026-11-09T00:00:00.000Z"
    source_url: "https://www.newyorkfed.org/newsevents/news/research/2026/20261109"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newyorkfed.org"
        source_url: "https://www.newyorkfed.org/newsevents/news/research/2026/20261109"
        retrieved_at: "2026-11-10T07:47:48+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; volume up 64.9x day-over-day is the strongest flow signal in today's data set."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newyorkfed.org: Inflation Expectations Stable; Labor Market Expectations Mixed - FEDER"
    url: "https://www.newyorkfed.org/newsevents/news/research/2026/20261109"
    published_at: "2026-11-09T00:00:00.000Z"
    retrieved_at: "2026-11-10T07:47:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
