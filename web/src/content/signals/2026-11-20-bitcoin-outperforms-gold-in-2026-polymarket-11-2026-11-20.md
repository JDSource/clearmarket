---
signal_id: "CMSIG2026112008"
signal_slug: "bitcoin-outperforms-gold-in-2026-polymarket-11-2026-11-20"
headline: "Bitcoin outperforms gold in 2026: Polymarket 11%"
semantic_title: "Bitcoin outperforming gold in 2026 stays below 25 percent"
telemetry: "Polymarket 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-20T15:03:25.000Z"
event_id: "CM-EVT-TKKW1QZRK9"
event_slug: "will-bitcoin-outperform-gold-in-2026"
event_question: "Will Bitcoin outperform Gold in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdcae9573d5680a2c958cca4676ed28df7a06861572124f3396cc60ab6b92b9c2"
  question_raw: "Will Bitcoin outperform Gold in 2026?"
  current_price: 0.11
  volume_24h_usd: 783.64
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices only an 11% chance Bitcoin outperforms gold in 2026, well below the 25% threshold."
  - "Bitcoin's renewed correlation with risk assets during the week's tech-led sell-off is consistent with the market's low-odds stance on the digital gold narrative."
  - "The companion Kalshi contract on Bitcoin outperforming gold also sits at 11%, showing cross-venue agreement with no meaningful spread."
  - "Resolves via UMA oracle at year-end; Bitcoin would need to significantly outpace gold's 2026 return from current levels to settle Yes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Bitcoin's sell-off alongside equities renewed debate over whether the asset functions as 'digital gold' or simply as a risk asset."
    publisher: "Cheryl Winokur Munk"
    published_at: "2026-11-20T15:03:25.000Z"
    source_url: "https://www.cnbc.com/2026/11/20/bitcoin-price-gold-market-hedge.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Cheryl Winokur Munk"
        source_url: "https://www.cnbc.com/2026/11/20/bitcoin-price-gold-market-hedge.html"
        retrieved_at: "2026-11-22T07:47:40+00:00"
  - type: "pm_response"
    notes: "Polymarket and Kalshi both at 11%; rare cross-venue alignment strengthens the signal that the digital gold thesis is priced out for 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Cheryl Winokur Munk: Bitcoin sell-off: Crypto is failing the 'digital gold' test again"
    url: "https://www.cnbc.com/2026/11/20/bitcoin-price-gold-market-hedge.html"
    published_at: "2026-11-20T15:03:25.000Z"
    retrieved_at: "2026-11-22T07:47:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
