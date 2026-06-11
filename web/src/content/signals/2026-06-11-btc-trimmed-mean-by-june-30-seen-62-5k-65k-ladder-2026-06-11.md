---
signal_id: "CMSIG2026061107"
signal_slug: "btc-trimmed-mean-by-june-30-seen-62-5k-65k-ladder-2026-06-11"
headline: "BTC trimmed mean by June 30 seen $62.5K-$65K: ladder"
semantic_title: "BTC June 30 trimmed mean pricing centered in 62500 to 65000 band"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-11T01:37:28.000Z"
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
  - "BTC June 30 trimmed mean ladder implies a central range of $62,500-$65,000: 61% above $62,500 but only 39% above $60,000 on the downside."
  - "Bitcoin trading near $60,000 amid Iran-triggered risk-off and $1.72B weekly ETF outflows sits at the lower tail of the distribution, where the market prices 39% probability of the trimmed mean breaching $60,000."
  - "The upside ladder prices only 25% above $75,000 by June 30, showing the market sees limited near-term recovery potential given the macro and geopolitical headwinds."
  - "Resolves via Coingecko trimmed mean methodology; the 'trimmed mean' calculation excludes outlier exchange prices, so flash crashes on thin venues would not distort settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin declined toward $60,000 amid growing short-term holder losses, weak ETF demand, and a broader risk-off move triggered by US-Iran geopolitical escalation."
    publisher: "fxstreet.com"
    published_at: "2026-06-11T01:37:28.000Z"
    source_url: "https://www.fxstreet.com/cryptocurrencies/news/bitcoin-faces-further-downside-risk-amid-growing-short-term-holder-losses-weak-etf-demand-202606110137"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxstreet.com"
        source_url: "https://www.fxstreet.com/cryptocurrencies/news/bitcoin-faces-further-downside-risk-amid-growing-short-term-holder-losses-weak-etf-demand-202606110137"
        retrieved_at: "2026-06-11T12:08:11+00:00"
  - type: "pm_response"
    notes: "The BTC June 30 ladder distribution centers near $62,500-$65,000, with current spot prices near $60,000 sitting in the lower 39th percentile of the market's implied range, reflecting but not fully pricing the bearish newsflow."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxstreet.com: Bitcoin faces further downside risk amid growing short-term holder los"
    url: "https://www.fxstreet.com/cryptocurrencies/news/bitcoin-faces-further-downside-risk-amid-growing-short-term-holder-losses-weak-etf-demand-202606110137"
    published_at: "2026-06-11T01:37:28.000Z"
    retrieved_at: "2026-06-11T12:08:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
