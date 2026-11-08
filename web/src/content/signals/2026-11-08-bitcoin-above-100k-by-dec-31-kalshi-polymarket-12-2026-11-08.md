---
signal_id: "CMSIG2026110807"
signal_slug: "bitcoin-above-100k-by-dec-31-kalshi-polymarket-12-2026-11-08"
headline: "Bitcoin above $100K by Dec 31: Kalshi/Polymarket 12%"
semantic_title: "Bitcoin above $100K by year-end stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-08T06:00:07.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.12
  volume_24h_usd: 76.42
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "The ladder implies Bitcoin below $100K by year-end is the base case: only 12% above $100K, 5% above $110K, collapsing to 1-2% above $130K."
  - "Bitcoin trading near $76K is consistent with the low probability assigned to a year-end rally above $100K."
  - "Binance EU closures and $1.28 billion in ETF outflows cited in the week's crypto recap reinforce bearish near-term sentiment that aligns with the ladder distribution."
  - "A companion Kalshi contract shows only 5% on Bitcoin reaching a minimum price of $100K by January 1, 2027, corroborating the ladder's long-shot read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin held below $76,000 as Binance European Union closures and regulatory pressure added to post-election crypto market stress."
    publisher: "Simon Mugo"
    published_at: "2026-11-08T06:00:07.000Z"
    source_url: "https://www.investing.com/news/cryptocurrency-news/bitcoin-holds-below-76k-as-binance-eu-closures-add-to-crypto-market-pressure-5010133"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Simon Mugo"
        source_url: "https://www.investing.com/news/cryptocurrency-news/bitcoin-holds-below-76k-as-binance-eu-closures-add-to-crypto-market-pressure-5010133"
        retrieved_at: "2026-11-08T14:44:20+00:00"
  - type: "pm_response"
    notes: "Ladder distribution across multiple strikes shows a sharp probability collapse above $110K; the year-end base case is Bitcoin remaining below $100K."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Simon Mugo: Bitcoin holds below $76K as Binance EU closures add to crypto market p"
    url: "https://www.investing.com/news/cryptocurrency-news/bitcoin-holds-below-76k-as-binance-eu-closures-add-to-crypto-market-pressure-5010133"
    published_at: "2026-11-08T06:00:07.000Z"
    retrieved_at: "2026-11-08T14:44:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
