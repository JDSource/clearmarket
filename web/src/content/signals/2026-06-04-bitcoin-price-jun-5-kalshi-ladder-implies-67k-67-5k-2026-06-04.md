---
signal_id: "CMSIG2026060407"
signal_slug: "bitcoin-price-jun-5-kalshi-ladder-implies-67k-67-5k-2026-06-04"
headline: "Bitcoin price Jun 5: Kalshi ladder implies ~$67K-$67.5K"
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
  - "Kalshi ladder market-implied Bitcoin price for Jun 5 sits near $67K-$67.5K: 51% above $67K, 39% above $67.5K."
  - "Bitcoin trading below $63K is sharply below the ladder's implied midpoint, suggesting the market had not fully priced in this leg lower."
  - "Only 25% probability sits above $75K on the Jun 30 BTC trimmed-mean contract (CM-EVT-3MXSH7KHK5), consistent with a subdued near-term recovery view."
  - "Resolves via the Kalshi Bitcoin price benchmark on Jun 5, 2026; the wide ladder distribution reflects high spot volatility."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell below $63,000 for the first time since February, continuing a multi-week selloff."
    publisher: "coindesk.com"
    published_at: "2026-06-04T01:30:53.000Z"
    source_url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
        retrieved_at: "2026-06-04T03:24:20+00:00"
  - type: "pm_response"
    notes: "Kalshi's Jun 5 ladder implied range of $67K-$67.5K is well above Bitcoin's current sub-$63K spot, highlighting market underestimation of the selloff."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: Bitcoin selloff continues as prices slide below $63,000 for the first"
    url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
    published_at: "2026-06-04T01:30:53.000Z"
    retrieved_at: "2026-06-04T03:24:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
