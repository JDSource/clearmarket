---
signal_id: "CMSIG2026112504"
signal_slug: "us-nonfarm-productivity-3-yoy-in-2026-kalshi-31-2026-11-25"
headline: "US nonfarm productivity >3% YoY in 2026: Kalshi 31%"
semantic_title: "US productivity topping 3 percent in 2026 stays below 50 percent"
telemetry: "Kalshi 31%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-25T22:17:28.000Z"
event_id: "CM-EVT-99JZRM47M6"
event_slug: "kxnfprod-27mar04"
event_question: "Will U.S. nonfarm productivity year-over-year growth exceed 3% in any quarter of 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNFPROD-27MAR04-T3"
  question_raw: "Will U.S. nonfarm productivity YoY in any quarter for 2026 be above 3%?"
  current_price: 0.31
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics- Employment Situation"
  resolves_at: "2027-06-02T15:30:00Z"
bullets:
  - "Kalshi prices a 31% chance that US nonfarm productivity year-over-year growth exceeds 3% in any quarter of 2026, resolved via the Bureau of Labor Statistics Employment Situation."
  - "Mixed Fed signals, cool CPI/PPI versus hot PCE and strong GDP, leave productivity's trajectory uncertain; the market is below 50%, reflecting that doubt."
  - "Strong AI-driven GDP growth (Stories 4 and 7) is the bull case for productivity clearing 3%; the market is not yet convinced it materializes consistently."
  - "Resolution requires BLS Employment Situation data to show a single quarter above 3% YoY, a one-shot structure that keeps the probability meaningful even with odds below even."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve is receiving conflicting signals, with cooler CPI and PPI readings but continued strong economic growth and rising demand pushing inflation higher."
    publisher: "bankoftexas.com"
    published_at: "2026-11-25T22:17:28.000Z"
    source_url: "https://www.bankoftexas.com/insights/articles/by-the-numbers_081426"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bankoftexas.com"
        source_url: "https://www.bankoftexas.com/insights/articles/by-the-numbers_081426"
        retrieved_at: "2026-11-28T07:47:57+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Bureau of Labor Statistics Employment Situation reports; at 31%, markets see the AI productivity boom as plausible but not the base case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bankoftexas.com: By the Numbers: Fed receiving conflicting inflation and job market sig"
    url: "https://www.bankoftexas.com/insights/articles/by-the-numbers_081426"
    published_at: "2026-11-25T22:17:28.000Z"
    retrieved_at: "2026-11-28T07:47:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
