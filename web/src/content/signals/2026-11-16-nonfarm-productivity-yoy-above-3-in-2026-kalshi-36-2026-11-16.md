---
signal_id: "CMSIG2026111602"
signal_slug: "nonfarm-productivity-yoy-above-3-in-2026-kalshi-36-2026-11-16"
headline: "Nonfarm productivity YoY above 3% in 2026: Kalshi 36%"
semantic_title: "US productivity above 3 percent in 2026 stays a long shot"
telemetry: "Kalshi 36%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-16T00:00:00.000Z"
event_id: "CM-EVT-99JZRM47M6"
event_slug: "kxnfprod-27mar04"
event_question: "Will U.S. nonfarm productivity year-over-year growth exceed 3% in any quarter of 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNFPROD-27MAR04-T3"
  question_raw: "Will U.S. nonfarm productivity YoY in any quarter for 2026 be above 3%?"
  current_price: 0.36
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics- Employment Situation"
  resolves_at: "2027-06-02T15:30:00Z"
bullets:
  - "Kalshi puts only 36% odds that US nonfarm productivity year-over-year growth exceeds 3% in any quarter of 2026, resolved by the Bureau of Labor Statistics Employment Situation."
  - "A 3.6% annualized Q3 reading that beat forecasts of 2.8% is a strong single-quarter print but the Kalshi contract suggests markets are not yet convinced it converts to a sustained year-over-year figure."
  - "The gap between the strong annualized print and the 36% contract probability reflects that year-over-year smoothing requires multiple strong quarters, not just one beat."
  - "Resolution is via Bureau of Labor Statistics Employment Situation data; a single quarter above 3% annualized does not guarantee the year-over-year threshold is met."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US labor productivity surged at a 3.6% annualized rate in Q3 2026, well above forecasts, raising questions about whether annual year-over-year growth can clear 3%."
    publisher: "Sam Kem Senior Economic Research Analyst"
    published_at: "2026-11-16T00:00:00.000Z"
    source_url: "https://www.utilitycapital.coop/content/solutions/en/stories/economy/Eyes-on-the-Economy-productivity-hiring-inflation.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sam Kem Senior Economic Research Analyst"
        source_url: "https://www.utilitycapital.coop/content/solutions/en/stories/economy/Eyes-on-the-Economy-productivity-hiring-inflation.html"
        retrieved_at: "2026-11-18T07:48:08+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 36% is at odds with the headline Q3 beat, suggesting the market is discounting one quarter as insufficient evidence for a sustained trend."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sam Kem Senior Economic Research Analyst: Eyes on the Economy: Productivity, Hiring, Inflation | CFC Solutions C"
    url: "https://www.utilitycapital.coop/content/solutions/en/stories/economy/Eyes-on-the-Economy-productivity-hiring-inflation.html"
    published_at: "2026-11-16T00:00:00.000Z"
    retrieved_at: "2026-11-18T07:48:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
