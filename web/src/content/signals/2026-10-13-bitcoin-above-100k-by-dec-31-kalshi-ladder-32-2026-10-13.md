---
signal_id: "CMSIG2026101307"
signal_slug: "bitcoin-above-100k-by-dec-31-kalshi-ladder-32-2026-10-13"
headline: "Bitcoin above $100K by Dec 31: Kalshi ladder 32%"
semantic_title: "Bitcoin above $100K by year-end stays below 50 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $100K by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.32
  volume_24h_usd: 1137.49
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Kalshi ladder prices Bitcoin above $100K by December 31 at 32%, with only 12% above $110K and 7% above $120K."
  - "The whale movement of $378 million in long-dormant BTC is drawing attention, trading volume on this ladder surged 200x day over day, though current price near $83,000-$84,000 leaves a large gap to the $100K threshold."
  - "The sharp dropoff from 32% above $100K to 12% above $110K indicates the market sees $100K as a plausible ceiling rather than a floor if Bitcoin does break out."
  - "Resolves via CF Benchmarks pricing on December 31, 2026; the dormant whale's sell pressure, if realized, could weigh on the price trajectory needed to resolve YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A dormant Bitcoin whale moved approximately $378 million in BTC after six years of inactivity, coinciding with Bitcoin trading near $83,000-$84,000 amid macro uncertainty."
    publisher: "theblock.co"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://www.theblock.co/news/markets/2026-10-13-bitcoin-whale-moves-378-million-418383"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/news/markets/2026-10-13-bitcoin-whale-moves-378-million-418383"
        retrieved_at: "2026-10-13T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on Bitcoin above $100K by year-end saw volume surge 200x day over day alongside the whale movement news, with market-implied probability at 32%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: Bitcoin whale moves $378 million in BTC after six years of dormancy: o"
    url: "https://www.theblock.co/news/markets/2026-10-13-bitcoin-whale-moves-378-million-418383"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
