---
signal_id: "CMSIG2026060807"
signal_slug: "btc-below-62-5k-by-jun-30-kalshi-ladder-39-2026-06-08"
headline: "BTC below $62.5K by Jun 30: Kalshi ladder 39%"
semantic_title: "Bitcoin end-June floor pricing firms around $62.5-65K"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T07:31:57.000Z"
event_id: "CM-EVT-P48V448T55"
event_slug: "kxbtcminmon-btc-26jun30"
event_question: "BTC trimmed mean price by Jun 30, 2026"
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
  - "Ladder prices 39% on BTC finishing below $62.5K by June 30, but only 10% below $52.5K, implied floor centered near $62.5-65K."
  - "BTC rebounding to $63,000 after the $60K breach is consistent with the ladder's distribution clustering around the $62.5-65K zone."
  - "The upside ladder (CM-EVT-3MXSH7KHK5) prices only 25% above $75K by June 30, confirming a near-term range-bound consensus, not a recovery to new highs."
  - "Resolves via trimmed mean BTC price by 11:59 PM ET on June 30, 2026; CME vol futures launch adds an institutional hedging tool but does not alter the directional pricing here."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CME launched Bitcoin Volatility Index futures as BTC rebounded to $63,000 after breaching $60,000 for the first time since the 2024 election."
    publisher: "financefeeds.com"
    published_at: "2026-06-08T07:31:57.000Z"
    source_url: "https://financefeeds.com/cme-launches-bitcoin-volatility-futures-as-crypto-derivatives-markets-mature/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "financefeeds.com"
        source_url: "https://financefeeds.com/cme-launches-bitcoin-volatility-futures-as-crypto-derivatives-markets-mature/"
        retrieved_at: "2026-06-08T12:25:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via trimmed mean BTC price at month-end; the 61% probability of finishing above $62.5K reflects the partial post-selloff recovery."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "financefeeds.com: CME Launches Bitcoin Volatility Futures As Crypto Derivatives Markets"
    url: "https://financefeeds.com/cme-launches-bitcoin-volatility-futures-as-crypto-derivatives-markets-mature/"
    published_at: "2026-06-08T07:31:57.000Z"
    retrieved_at: "2026-06-08T12:25:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
