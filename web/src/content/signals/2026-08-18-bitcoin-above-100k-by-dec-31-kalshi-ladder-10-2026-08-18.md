---
signal_id: "CMSIG2026081808"
signal_slug: "bitcoin-above-100k-by-dec-31-kalshi-ladder-10-2026-08-18"
headline: "Bitcoin above $100K by Dec 31: Kalshi ladder 10%"
semantic_title: "Bitcoin above $100K by year-end stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-18T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin year-end 2026 price ceiling"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.1
  volume_24h_usd: 298.08
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Kalshi ladder prices only 10% on Bitcoin exceeding $100,000 by December 31, 2026, with probability falling further to 7% at $110K and below 5% beyond that."
  - "The news narrative of low volatility and traders fleeing Bitcoin for higher-beta plays is consistent with the market's skeptical pricing of a major year-end rally."
  - "Companion contracts at 2-3% on Bitcoin above $200K-$250K by 2027 confirm the market sees the current $65K range as closer to a ceiling than a launchpad."
  - "Resolves via CF Benchmarks pricing at the defined date and time; settlement depends on the specific benchmark methodology used."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin's volatility has collapsed to a cycle low near $64,000-$65,000, with traders chasing higher-risk alternatives for bigger returns."
    publisher: "coindesk.com"
    published_at: "2026-08-18T00:00:00.000Z"
    source_url: "https://www.coindesk.com/markets/2026/08/18/bitcoin-has-gone-quiet-as-traders-chase-5x-or-10x-payoffs-elsewhere"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/08/18/bitcoin-has-gone-quiet-as-traders-chase-5x-or-10x-payoffs-elsewhere"
        retrieved_at: "2026-08-19T08:31:28+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder at 10% for Bitcoin above $100K confirms the market's muted outlook matches the volatility collapse reported in the news."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: Bitcoin's volatility collapse has traders look elsewhere as ‘nothing r"
    url: "https://www.coindesk.com/markets/2026/08/18/bitcoin-has-gone-quiet-as-traders-chase-5x-or-10x-payoffs-elsewhere"
    published_at: "2026-08-18T00:00:00.000Z"
    retrieved_at: "2026-08-19T08:31:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
