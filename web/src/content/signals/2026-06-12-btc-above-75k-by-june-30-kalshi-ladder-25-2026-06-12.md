---
signal_id: "CMSIG2026061208"
signal_slug: "btc-above-75k-by-june-30-kalshi-ladder-25-2026-06-12"
headline: "BTC above $75K by June 30: Kalshi ladder 25%"
semantic_title: "Bitcoin above $75K by June 30 nears minority pricing at 25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T01:59:24.000Z"
event_id: "CM-EVT-3MXSH7KHK5"
event_slug: "kxbtcmaxmon-btc-26jun30"
event_question: "BTC trimmed mean by June 30, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26JUN30-7500000"
  question_raw: "Will BTC trimmed mean be above $75000.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.25
  volume_24h_usd: 4334.16
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi ladder prices only 25% on Bitcoin's trimmed mean finishing above $75K by June 30, with probability collapsing to 8% above $80K."
  - "Iran deal optimism is lifting spot crypto prices, but the sub-25% probability above $75K reflects the ETF outflow headwinds and the short time remaining in June."
  - "The companion below-ladder (CM-EVT-P48V448T55) pins the modal range at $62.5K-$65K, with 84% below $67.5K, the market sees Bitcoin consolidating well under $75K."
  - "Resolves via Kalshi using a trimmed mean price calculation through June 30, 2026 at 11:59 PM ET; the trimmed mean methodology reduces spike/wick distortion."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin and major cryptocurrencies jumped on Trump optimism around an Iran deal, even as the broader June crypto selloff saw Bitcoin ETFs shed $2.1 billion month-to-date."
    publisher: "Aniket Verma"
    published_at: "2026-06-12T01:59:24.000Z"
    source_url: "https://www.benzinga.com/crypto/cryptocurrency/26/06/53158839/bitcoin-ethereum-xrp-dogecoin-jump-on-iran-deal-optimism-spacex-ipo-tricky-for-markets"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Aniket Verma"
        source_url: "https://www.benzinga.com/crypto/cryptocurrency/26/06/53158839/bitcoin-ethereum-xrp-dogecoin-jump-on-iran-deal-optimism-spacex-ipo-tricky-for-markets"
        retrieved_at: "2026-06-12T11:42:07+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder's 25% above $75K versus 84% below $67.5K on the complementary ladder defines a tight modal range around current spot levels despite the Iran-deal pop."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Aniket Verma: Bitcoin, Ethereum, XRP, Dogecoin Jump After Trump Sparks Optimism On I"
    url: "https://www.benzinga.com/crypto/cryptocurrency/26/06/53158839/bitcoin-ethereum-xrp-dogecoin-jump-on-iran-deal-optimism-spacex-ipo-tricky-for-markets"
    published_at: "2026-06-12T01:59:24.000Z"
    retrieved_at: "2026-06-12T11:42:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
