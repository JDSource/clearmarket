---
signal_id: "CMSIG2026112007"
signal_slug: "bitcoin-above-99-999-by-dec-31-kalshi-ladder-2-2026-11-20"
headline: "Bitcoin above $99,999 by Dec 31: Kalshi ladder 2%"
semantic_title: "Bitcoin above $100K by year-end stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-20T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $99,999 by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.02
  volume_24h_usd: 48.38
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Kalshi ladder prices only 2% on Bitcoin exceeding $99,999 by December 31, with no meaningful probability at any higher strike."
  - "Bitcoin trading near $59,000, roughly 40% below the $100K threshold, aligns with the ladder's near-zero end-of-year pricing."
  - "The $1.8 billion liquidation wave and record $541 million BlackRock ETF outflow (Story 35) reinforce the bearish near-term setup embedded in the distribution."
  - "Resolves via Kalshi at year-end; the Polymarket contract on Bitcoin outperforming gold in 2026 (11%) implies some residual bull case but not enough to move the $100K ladder."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "JPMorgan flagged that Bitcoin's price drop is pressuring miners, with the coin trading near $59,000 and hitting multi-year lows."
    publisher: "theblock.co"
    published_at: "2026-11-20T00:00:00.000Z"
    source_url: "https://www.theblock.co/newsletters/the-daily/2026-11-20-jpmorgan-bitcoin-price-drop-miners-senate-passes-death-bets-act-more-crypto-news-444786"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/newsletters/the-daily/2026-11-20-jpmorgan-bitcoin-price-drop-miners-senate-passes-death-bets-act-more-crypto-news-444786"
        retrieved_at: "2026-11-22T07:47:40+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; distribution shows no probability support above $100K, consistent with spot price near $59K."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: JPMorgan says bitcoin's price drop pressures miners, Senate passes 'De"
    url: "https://www.theblock.co/newsletters/the-daily/2026-11-20-jpmorgan-bitcoin-price-drop-miners-senate-passes-death-bets-act-more-crypto-news-444786"
    published_at: "2026-11-20T00:00:00.000Z"
    retrieved_at: "2026-11-22T07:47:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
