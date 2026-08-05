---
signal_id: "CMSIG2026080508"
signal_slug: "bitcoin-above-100k-by-dec-31-ladder-implied-12-2026-08-05"
headline: "Bitcoin above $100K by Dec 31: ladder-implied 12%"
semantic_title: "Bitcoin above $100K by year-end stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-05T06:27:49.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.12
  volume_24h_usd: 145.01
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "The ladder prices only 12% odds on Bitcoin exceeding $100K by December 31, 2026, with probability falling to 7% above $110K and 4% above $150K."
  - "Arthur Hayes's $1M thesis is a dramatic outlier versus the ladder's distribution, which places the mode well below $100K, the market is not endorsing the bull case."
  - "BTC is quoted in price data at approximately $64K today, consistent with the ladder's implied range anchored below $100K."
  - "Kalshi's longer-dated contract (CM-EVT-3CQP3GL0Y1) puts just 2% on Bitcoin above $250K by 2027, showing the extreme bull scenario is priced as a near-impossibility across timeframes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Arthur Hayes argued an AI sector bust could redirect capital into Bitcoin and drive prices above $1 million."
    publisher: "regional-front.cointelegraph.com"
    published_at: "2026-08-05T06:27:49.000Z"
    source_url: "https://regional-front.cointelegraph.com/markets/arthur-hayes-ai-credit-crisis-bitcoin-1-million"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "regional-front.cointelegraph.com"
        source_url: "https://regional-front.cointelegraph.com/markets/arthur-hayes-ai-credit-crisis-bitcoin-1-million"
        retrieved_at: "2026-08-05T10:30:51+00:00"
  - type: "pm_response"
    notes: "Ladder distribution shows a steep probability cliff above $100K; the Hayes thesis finds essentially no support in the current prediction market pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "regional-front.cointelegraph.com: AI Bust Could Send Bitcoin Above $1M, Arthur Hayes says"
    url: "https://regional-front.cointelegraph.com/markets/arthur-hayes-ai-credit-crisis-bitcoin-1-million"
    published_at: "2026-08-05T06:27:49.000Z"
    retrieved_at: "2026-08-05T10:30:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
