---
signal_id: "CMSIG2026072208"
signal_slug: "bitcoin-above-100k-again-kalshi-17-2026-07-22"
headline: "Bitcoin above $100K again: Kalshi 17%"
semantic_title: "Bitcoin crossing $100K again stays a long shot below 25%"
telemetry: "Kalshi 17%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-ZPMYBGJP99"
event_slug: "kxbtcmax100-26"
event_question: "Will Bitcoin cross $100,000 again?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAX100-26-DEC"
  question_raw: "Will Bitcoin be above $100000.00 by Jan 1, 2027 at 12:00AM ET?"
  current_price: 0.17
  volume_24h_usd: 425.41
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T05:00:00Z"
bullets:
  - "Kalshi prices 17% on Bitcoin crossing $100,000 again."
  - "Bitcoin holding near $66,000 leaves a roughly 50% move required to hit the strike, which the market treats as unlikely this cycle."
  - "The Kalshi ladder implies Bitcoin stays below $100,000 by year-end with roughly 84% confidence, consistent with the 17% cross reading."
  - "Resolves via CF Benchmarks Bitcoin reference rate; the contract requires a confirmed print above $100,000, not a brief wick."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin held above $66,000 with altcoins including Ondo and GRAM leading a broader crypto market rebound amid easing bearish momentum."
    publisher: "fxstreet.com"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://www.fxstreet.com/cryptocurrencies/news/crypto-market-overview-bitcoin-holds-firm-as-ondo-and-gram-lead-rally-202607220400"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxstreet.com"
        source_url: "https://www.fxstreet.com/cryptocurrencies/news/crypto-market-overview-bitcoin-holds-firm-as-ondo-and-gram-lead-rally-202607220400"
        retrieved_at: "2026-07-22T10:22:09+00:00"
  - type: "pm_response"
    notes: "Kalshi at 17% on a return to six-figure Bitcoin reflects market skepticism that the current $66K consolidation develops into a full breakout run."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxstreet.com: Crypto Market Overview: Bitcoin holds firm as ONDO and GRAM lead rally"
    url: "https://www.fxstreet.com/cryptocurrencies/news/crypto-market-overview-bitcoin-holds-firm-as-ondo-and-gram-lead-rally-202607220400"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-22T10:22:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
