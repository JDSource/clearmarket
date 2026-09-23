---
signal_id: "CMSIG2026092208"
signal_slug: "bitcoin-above-100k-by-dec-31-kalshi-45-2026-09-22"
headline: "Bitcoin above $100K by Dec 31: Kalshi 45%"
semantic_title: "Bitcoin above $100K by year-end stays below 50%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-22T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "market-implied level"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.45
  volume_24h_usd: 2579.43
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Kalshi ladder prices Bitcoin above $99,999.99 by December 31, 2026 at 45%, just below an even chance."
  - "CME expanding crypto derivatives suite with new futures products is a structural positive for market access, consistent with the near-50% pricing of a six-figure Bitcoin."
  - "Above $110,000 the probability drops to 26%, and above $120,000 to 16%, showing the distribution skews but tails off sharply beyond $110K."
  - "Bitcoin trading near $87,000 as of today means a move to $100K requires roughly a 15% gain in about three months, which the market treats as a coin-flip."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CME Group announced Bitcoin Cash and Uniswap futures launching October 19, expanding its crypto derivatives suite as Bitcoin trades near $87,000."
    publisher: "CME Group"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.prnewswire.com/news-releases/cme-group-to-expand-crypto-derivatives-suite-with-bitcoin-cash-and-uniswap-futures-302886066.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CME Group"
        source_url: "https://www.prnewswire.com/news-releases/cme-group-to-expand-crypto-derivatives-suite-with-bitcoin-cash-and-uniswap-futures-302886066.html"
        retrieved_at: "2026-09-23T07:47:29+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder puts Bitcoin above $100K by year-end at 45%, with the distribution showing the market sees $100K-$110K as the most likely upside zone if the threshold is crossed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CME Group: CME Group to Expand Crypto Derivatives Suite with Bitcoin Cash and Uni"
    url: "https://www.prnewswire.com/news-releases/cme-group-to-expand-crypto-derivatives-suite-with-bitcoin-cash-and-uniswap-futures-302886066.html"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-23T07:47:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
