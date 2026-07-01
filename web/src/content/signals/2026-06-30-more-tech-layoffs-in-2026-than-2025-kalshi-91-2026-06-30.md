---
signal_id: "CMSIG2026063004"
signal_slug: "more-tech-layoffs-in-2026-than-2025-kalshi-91-2026-06-30"
headline: "More tech layoffs in 2026 than 2025: Kalshi 91%"
semantic_title: "Tech layoffs outpacing 2025 levels solidifies near full pricing"
telemetry: "Kalshi 91%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-30T16:30:02.000Z"
event_id: "CM-EVT-ZTGN9MPFL9"
event_slug: "kxlayoffsyinfo-26"
event_question: "Will there be more tech layoffs in 2026 than in 2025?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLAYOFFSYINFO-26-494000"
  question_raw: "More tech layoffs in 2026 than in 2025?"
  current_price: 0.907
  volume_24h_usd: 799.96
  arbitration_model: "kalshi_staff"
  resolution_source: "FRED"
  resolves_at: "2027-03-01T15:00:00Z"
bullets:
  - "Kalshi prediction market prices 91% probability that 2026 tech layoffs will exceed the 2025 total."
  - "Rising job openings coexist with deep public pessimism, consistent with a market pricing continued tech-sector displacement even as aggregate demand holds."
  - "The 91% reading leaves little room for upward revision; the market is near fully committed to a worse-than-2025 tech layoff year."
  - "Resolves via FRED data tracking layoff and discharge rates in the technology sector for the full calendar year 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Hard labor data shows job openings at a two-year high in May, but consumer confidence in the job market sank to its lowest, reflecting a widening perception gap."
    publisher: "AOL"
    published_at: "2026-06-30T16:30:02.000Z"
    source_url: "https://www.aol.com/articles/labor-market-improving-public-still-163002000.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/articles/labor-market-improving-public-still-163002000.html"
        retrieved_at: "2026-07-01T11:20:57+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 91% on FRED resolution; high conviction with limited two-way pricing implied."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: Data Shows the Labor Market is Improving. So Why Are Americans Having"
    url: "https://www.aol.com/articles/labor-market-improving-public-still-163002000.html"
    published_at: "2026-06-30T16:30:02.000Z"
    retrieved_at: "2026-07-01T11:20:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
