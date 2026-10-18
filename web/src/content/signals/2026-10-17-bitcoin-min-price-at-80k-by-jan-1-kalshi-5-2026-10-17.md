---
signal_id: "CMSIG2026101707"
signal_slug: "bitcoin-min-price-at-80k-by-jan-1-kalshi-5-2026-10-17"
headline: "Bitcoin min price at $80K+ by Jan 1: Kalshi 5%"
semantic_title: "Bitcoin minimum price above $80K by year-end stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-17T00:00:00.000Z"
event_id: "CM-EVT-NHW1YL14S9"
event_slug: "kxbtcminy-27jan01"
event_question: "Bitcoin minimum price, January 1, 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMINY-27JAN01-40000.00"
  question_raw: "Will Bitcoin be below $40000.00 by Jan 1, 2027 at 12:00am ET?"
  current_price: 0.05
  volume_24h_usd: 0.3
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T05:00:00Z"
bullets:
  - "Kalshi prices only 5% odds that Bitcoin's minimum price stays at or above $80,000 through January 1, 2027, resolving via CF Benchmarks, with trading volume up 3,816% day-over-day."
  - "Bitcoin's dip below $80,000 this week is consistent with Kalshi's near-zero probability of the price floor holding at that level through year-end."
  - "The sharp volume surge on this contract signals fresh attention to the downside scenario following the week's price action and macro equity weakness."
  - "A companion Kalshi contract (CM-EVT-3CQP3GL0Y1) prices only 2% on Bitcoin above $250,000 by 2027, confirming the market sees no near-term upside breakout either."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin briefly fell below $80,000 this week before bouncing, with Ledger tightening reseller rules and MSCI considering exclusion of crypto treasury firms from its indices."
    publisher: "Lawrence Mondal"
    published_at: "2026-10-17T00:00:00.000Z"
    source_url: "https://crypto.news/weekly-crypto-recap-bitcoin-ledger-msci-oct-17-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lawrence Mondal"
        source_url: "https://crypto.news/weekly-crypto-recap-bitcoin-ledger-msci-oct-17-2026/"
        retrieved_at: "2026-10-18T07:47:28+00:00"
  - type: "pm_response"
    notes: "Kalshi hosts this contract resolving via CF Benchmarks; the minimum-price framing means any single sub-$80K close before January 1, 2027, resolves the contract as 'no'."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lawrence Mondal: Bitcoin falls below $80k, Ledger changes sales, MSCI rules | Weekly re"
    url: "https://crypto.news/weekly-crypto-recap-bitcoin-ledger-msci-oct-17-2026/"
    published_at: "2026-10-17T00:00:00.000Z"
    retrieved_at: "2026-10-18T07:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
