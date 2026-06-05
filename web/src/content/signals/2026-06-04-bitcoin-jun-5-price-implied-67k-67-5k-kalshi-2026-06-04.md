---
signal_id: "CMSIG2026060405"
signal_slug: "bitcoin-jun-5-price-implied-67k-67-5k-kalshi-2026-06-04"
headline: "Bitcoin Jun 5 price implied $67K-$67.5K: Kalshi"
semantic_title: "Bitcoin Jun 5 pricing fractures below $67K-$67.5K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-06-04T01:30:53.000Z"
event_id: "CM-EVT-9VZL96QM32"
event_slug: "kxbtcd-26jun0517"
event_question: "Bitcoin price on Jun 5, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCD-26JUN0517-T67499.99"
  question_raw: "Bitcoin price on Jun 5, 2026?"
  current_price: 0.39
  volume_24h_usd: 21275.91
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-06-05T21:05:00Z"
bullets:
  - "Kalshi's Jun 5 Bitcoin ladder implies a modal range of $67K-$67.5K: 51% above $67K but only 39% above $67.5K."
  - "News of Bitcoin trading near $62K-$63K is well below the Kalshi modal range, meaning the market-implied distribution is currently above realized spot."
  - "The $63K-$64K region shows 85-86% above on the ladder, suggesting the contract still assigns high probability to a recovery above recent spot by settlement."
  - "A companion Kalshi contract (CM-EVT-JCHVD3PD84) puts 51% on Bitcoin above $66K on June 6, reflecting ongoing uncertainty about whether the selloff persists through the weekend."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin sold off below $63,000 for the first time since February, with the selloff deepening amid Gulf war tensions and Strategy's BTC sale."
    publisher: "coindesk.com"
    published_at: "2026-06-04T01:30:53.000Z"
    source_url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
        retrieved_at: "2026-06-05T11:24:05+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via observed Bitcoin spot price on June 5, 2026; settlement source and exact time-of-day snapshot methodology determine the final outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: Bitcoin selloff continues as prices slide below $63,000 for the first"
    url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
    published_at: "2026-06-04T01:30:53.000Z"
    retrieved_at: "2026-06-05T11:24:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
