---
signal_id: "CMSIG2026061903"
signal_slug: "btc-trimmed-mean-below-57-5k-by-jun-30-kalshi-27-2026-06-19"
headline: "BTC trimmed mean below $57.5K by Jun 30: Kalshi 27%"
semantic_title: "BTC end-June floor pricing wavers below $57.5K implied range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-19T07:53:40.000Z"
event_id: "CM-EVT-P48V448T55"
event_slug: "kxbtcminmon-btc-26jun30"
event_question: "BTC trimmed mean floor by Jun 30 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMINMON-BTC-26JUN30-5250000"
  question_raw: "Will BTC trimmed mean be below $52500.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.08
  volume_24h_usd: 637.72
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi's BTC ladder prices 27% on a trimmed mean below $57,500 and 14% below $55,000 by June 30, with the implied floor near $55-57.5K."
  - "Bitcoin's drop below $64K aligns with the ladder's bearish tail, with traders loading put options as low as $52,000 per CoinDesk."
  - "The above-$75K contract (CM-EVT-CM-EVT-3MXSH7KHK5) prices only 8%, confirming the market sees no recovery to prior highs this month."
  - "Resolution uses trimmed-mean methodology at 11:59 PM ET on June 30; extreme intraday wicks would not determine outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell below $64K on June 19, driven by Fed hawkishness under Warsh and a surge in bearish options positioning down to $52,000."
    publisher: "Alex Ioannou"
    published_at: "2026-06-19T07:53:40.000Z"
    source_url: "https://99bitcoins.com/news/bitcoin-btc/crypto-news-today-june-19-btc-crashes-below-64k-kalshi-ipo-rumors-begin-and-g7-leaders-target-north-korean-crypto-hackers/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alex Ioannou"
        source_url: "https://99bitcoins.com/news/bitcoin-btc/crypto-news-today-june-19-btc-crashes-below-64k-kalshi-ipo-rumors-begin-and-g7-leaders-target-north-korean-crypto-hackers/"
        retrieved_at: "2026-06-19T12:03:18+00:00"
  - type: "pm_response"
    notes: "The Kalshi BTC trimmed-mean ladder provides a distribution read; current pricing puts the June-end floor firmly below $60K with a 27% chance of sub-$57.5K."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alex Ioannou: Crypto News Today (June 19): BTC Crashes Below $64K, Kalshi IPO Rumors"
    url: "https://99bitcoins.com/news/bitcoin-btc/crypto-news-today-june-19-btc-crashes-below-64k-kalshi-ipo-rumors-begin-and-g7-leaders-target-north-korean-crypto-hackers/"
    published_at: "2026-06-19T07:53:40.000Z"
    retrieved_at: "2026-06-19T12:03:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
