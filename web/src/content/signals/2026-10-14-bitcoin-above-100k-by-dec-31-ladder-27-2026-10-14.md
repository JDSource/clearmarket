---
signal_id: "CMSIG2026101408"
signal_slug: "bitcoin-above-100k-by-dec-31-ladder-27-2026-10-14"
headline: "Bitcoin above $100K by Dec 31: ladder 27%"
semantic_title: "Bitcoin above $100K by year-end stays below 30% odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $100K by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.27
  volume_24h_usd: 1782.94
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Prediction market ladder prices only 27% probability that Bitcoin exceeds $100,000 by December 31, 2026, with 10% above $110,000 and 7% above $120,000."
  - "Bitcoin's drop below $82,000 on hot core CPI is directionally consistent with the ladder's sub-30% odds on a year-end breakout above $100,000."
  - "The Kalshi contract on a Fed cut before 2027 (CM-EVT-X2TT2M9D02) at 6% reinforces the macro headwind; a sustained Bitcoin rally to $100K would likely require monetary easing."
  - "Resolves via CF Benchmarks price data at December 31, 2026 market close; the current spot price near $81,000 would require roughly a 23% rally to hit the $100K strike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell below $82,000 after hotter-than-expected core CPI revived concerns about a Federal Reserve rate hike."
    publisher: "theblock.co"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://www.theblock.co/news/markets/2026-10-14-bitcoin-falls-below-82000-core-inflation-fed-rate-hike-418582"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/news/markets/2026-10-14-bitcoin-falls-below-82000-core-inflation-fed-rate-hike-418582"
        retrieved_at: "2026-10-15T07:47:47+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder on Bitcoin's year-end price reflects the macro headwind from sticky inflation, with the $100K strike at only 27% probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: Bitcoin falls below $82,000 as hotter core CPI revives Fed hike concer"
    url: "https://www.theblock.co/news/markets/2026-10-14-bitcoin-falls-below-82000-core-inflation-fed-rate-hike-418582"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-15T07:47:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
