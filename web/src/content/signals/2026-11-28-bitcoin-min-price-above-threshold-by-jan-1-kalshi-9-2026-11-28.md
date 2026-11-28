---
signal_id: "CMSIG2026112807"
signal_slug: "bitcoin-min-price-above-threshold-by-jan-1-kalshi-9-2026-11-28"
headline: "Bitcoin min price above threshold by Jan 1: Kalshi 9%"
semantic_title: "Bitcoin minimum price holding above zero by Jan 2027 priced in; $60K floor stays unlikely"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-28T05:56:50.000Z"
event_id: "CM-EVT-NHW1YL14S9"
event_slug: "kxbtcminy-27jan01"
event_question: "Bitcoin minimum price, January 1, 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMINY-27JAN01-40000.00"
  question_raw: "Will Bitcoin be below $40000.00 by Jan 1, 2027 at 12:00am ET?"
  current_price: 0.09
  volume_24h_usd: 1710.57
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T05:00:00Z"
bullets:
  - "Kalshi prices a 9% probability on the Bitcoin minimum price contract resolving favorably by January 1, 2027, via CF Benchmarks."
  - "Bitcoin trading below $60,000 is consistent with the market's low probability reading, the price action and the contract are aligned."
  - "A companion Polymarket contract on the US establishing a national Bitcoin reserve before 2027 sits at 4% (Story 35), and the Strategic Bitcoin Reserve bill advancing to the House floor has not lifted either contract."
  - "Resolves via CF Benchmarks; the minimum-price structure means a single sustained dip below the threshold resets the contract, a tail risk that keeps YES odds suppressed."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell back below $60,000 as ETF outflows mounted and derivatives pressure weighed on the asset, even as whales bought the dip."
    publisher: "Simon Mugo"
    published_at: "2026-11-28T05:56:50.000Z"
    source_url: "https://www.investing.com/news/cryptocurrency-news/bitcoin-price-today-falls-below-60k-as-whales-buy-dip-etf-outflows-mount-5054180"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Simon Mugo"
        source_url: "https://www.investing.com/news/cryptocurrency-news/bitcoin-price-today-falls-below-60k-as-whales-buy-dip-etf-outflows-mount-5054180"
        retrieved_at: "2026-11-28T07:47:57+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via CF Benchmarks on January 1, 2027; at 9%, markets are skeptical Bitcoin holds above key levels through year-end given current sell pressure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Simon Mugo: Bitcoin price falls below $60,000 as whales buy dip, ETF outflows moun"
    url: "https://www.investing.com/news/cryptocurrency-news/bitcoin-price-today-falls-below-60k-as-whales-buy-dip-etf-outflows-mount-5054180"
    published_at: "2026-11-28T05:56:50.000Z"
    retrieved_at: "2026-11-28T07:47:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
