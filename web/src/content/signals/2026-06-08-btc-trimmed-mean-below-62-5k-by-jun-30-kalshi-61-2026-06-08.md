---
signal_id: "CMSIG2026060807"
signal_slug: "btc-trimmed-mean-below-62-5k-by-jun-30-kalshi-61-2026-06-08"
headline: "BTC trimmed mean below $62.5K by Jun 30: Kalshi 61%"
semantic_title: "BTC below $62.5K by June 30 consensus firms near even"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T14:44:57.000Z"
event_id: "CM-EVT-P48V448T55"
event_slug: "kxbtcminmon-btc-26jun30"
event_question: "BTC trimmed mean price by June 30, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMINMON-BTC-26JUN30-5250000"
  question_raw: "Will BTC trimmed mean be below $52500.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.1
  volume_24h_usd: 1639.31
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi ladder implies BTC trimmed mean near $62.5K by June 30: 61% below $62.5K, 39% below $60K."
  - "Bitcoin near $63.5K is at the market-implied distribution midpoint; current spot is essentially at-the-money relative to the ladder."
  - "The above-$75K ladder (Story 36 candidate) prices only 25% probability, pointing to a heavily right-skewed distribution against a recovery."
  - "Resolves via trimmed mean price calculation at 11:59 PM ET on June 30, 2026; the settlement source is the Kalshi staff methodology."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin steadied near $62,000-$63,500 after a 50% decline from its October 2025 high, with RSI hitting 25 and $5 billion in ETF outflows coinciding with the May jobs shock."
    publisher: "crypto-economy.com"
    published_at: "2026-06-08T14:44:57.000Z"
    source_url: "https://crypto-economy.com/cme-open-the-door-to-bitcoin-volatility-trading/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "crypto-economy.com"
        source_url: "https://crypto-economy.com/cme-open-the-door-to-bitcoin-volatility-trading/"
        retrieved_at: "2026-06-09T10:57:53+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder straddles current spot price, reflecting genuine uncertainty with a modest downside lean driven by macro and ETF outflow pressure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "crypto-economy.com: CME Opens the Door to Bitcoin Volatility Trading With First Futures Be"
    url: "https://crypto-economy.com/cme-open-the-door-to-bitcoin-volatility-trading/"
    published_at: "2026-06-08T14:44:57.000Z"
    retrieved_at: "2026-06-09T10:57:53+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
