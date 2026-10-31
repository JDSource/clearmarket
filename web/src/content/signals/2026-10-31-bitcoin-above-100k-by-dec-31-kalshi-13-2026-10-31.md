---
signal_id: "CMSIG2026103107"
signal_slug: "bitcoin-above-100k-by-dec-31-kalshi-13-2026-10-31"
headline: "Bitcoin above $100K by Dec 31: Kalshi 13%"
semantic_title: "Bitcoin above $100K by year-end slips to long-shot odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-31T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $99,999.99 by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.13
  volume_24h_usd: 2388.24
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Kalshi's ladder puts Bitcoin above $100K by December 31 at just 13%, with volume up 19,555% day-over-day, a 196.6x surge in trading activity."
  - "Bitcoin fell below $77,000 following the Binance hack; the ladder's distribution collapses sharply above $100K, with $110K at 6% and $120K at 3%."
  - "The 196.6x volume spike is the strongest signal in this batch that the hack triggered a decisive repricing of year-end Bitcoin upside targets."
  - "A companion Polymarket contract (CM-EVT-TKKW1QZRK9) on Bitcoin outperforming gold in 2026 sits at 42%, the Binance shock is putting that thesis under pressure."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Binance set aside $6.34 billion to cover losses from a $6.3 billion hack, the largest crypto theft in history, sending Bitcoin below $77,000."
    publisher: "theblock.co"
    published_at: "2026-10-31T00:00:00.000Z"
    source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-31-binance-hack-more-crypto-news-432243"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-31-binance-hack-more-crypto-news-432243"
        retrieved_at: "2026-10-31T07:48:23+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder, with a near-200x volume surge, reflects the market treating the Binance hack as a material threat to year-end Bitcoin price targets."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: Binance sets aside $6.34 billion after hack, and more"
    url: "https://www.theblock.co/newsletters/the-daily/2026-10-31-binance-hack-more-crypto-news-432243"
    published_at: "2026-10-31T00:00:00.000Z"
    retrieved_at: "2026-10-31T07:48:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
