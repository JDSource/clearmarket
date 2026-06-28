---
signal_id: "CMSIG2026062808"
signal_slug: "bitcoin-above-100k-by-dec-31-kalshi-15-2026-06-28"
headline: "Bitcoin above $100K by Dec 31: Kalshi 15%"
semantic_title: "Bitcoin above $100K by year-end fractures as capitulation signals mount"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-28T02:51:04.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.15
  volume_24h_usd: 22.2
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-01T04:59:00Z"
bullets:
  - "Kalshi ladder prices Bitcoin above $100K by Dec 31 at 15%; the market-implied level sits well below $100K given only 15% above that strike."
  - "Record supply in loss and UTXO capitulation signals are consistent with bearish on-chain data; the market reflects this with an 85% implied probability of staying below $100K."
  - "Trading volume on this Kalshi contract is up 10,835% day over day, indicating a sharp surge in fresh positioning around the capitulation narrative."
  - "A near-term Kalshi contract (CM-EVT-3MXSH7KHK5) prices Bitcoin above $75K by June 30 at only 2%, showing the short-end distribution is also deeply bearish."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin UTXO data signals capitulation underway, with supply in loss at an all-time high of 10.83 million BTC and prices trading near $60K."
    publisher: "tradingview.com"
    published_at: "2026-06-28T02:51:04.000Z"
    source_url: "https://www.tradingview.com/news/cointelegraph:9ce2da0c8094b:0-bitcoin-unspent-transaction-outputs-signal-capitulation-underway-analyst/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradingview.com"
        source_url: "https://www.tradingview.com/news/cointelegraph:9ce2da0c8094b:0-bitcoin-unspent-transaction-outputs-signal-capitulation-underway-analyst/"
        retrieved_at: "2026-06-28T10:24:59+00:00"
  - type: "pm_response"
    notes: "Kalshi at 15% above $100K, with a 109x volume spike, signals the market is actively repricing the year-end Bitcoin outlook amid capitulation data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradingview.com: Bitcoin unspent transaction outputs signal capitulation underway: anal"
    url: "https://www.tradingview.com/news/cointelegraph:9ce2da0c8094b:0-bitcoin-unspent-transaction-outputs-signal-capitulation-underway-analyst/"
    published_at: "2026-06-28T02:51:04.000Z"
    retrieved_at: "2026-06-28T10:24:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
