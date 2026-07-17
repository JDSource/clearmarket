---
signal_id: "CMSIG2026071608"
signal_slug: "bitcoin-crosses-100k-again-kalshi-11-2026-07-16"
headline: "Bitcoin crosses $100K again: Kalshi 11%"
semantic_title: "Bitcoin above $100K consensus wavers under geopolitical weight"
telemetry: "Kalshi 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T09:51:29.000Z"
event_id: "CM-EVT-ZPMYBGJP99"
event_slug: "kxbtcmax100-26"
event_question: "Will Bitcoin cross $100,000 again?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAX100-26-DEC"
  question_raw: "Will Bitcoin be above $100000.00 by Jan 1, 2027 at 12:00AM ET?"
  current_price: 0.11
  volume_24h_usd: 171.06
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T05:00:00Z"
bullets:
  - "Kalshi prices only 11% on Bitcoin crossing $100,000 again, with Bitcoin currently trading near $63,000-$64,000 amid US-Iran conflict."
  - "Institutional asset managers expanding crypto product lines are not translating into market-implied bullish momentum on the price level contract."
  - "Kalshi at 26% on Bitcoin's minimum price exceeding a threshold on January 1, 2027 suggests the market sees meaningful downside risk remaining."
  - "Resolves via CF Benchmarks; the contract requires Bitcoin to trade above $100,000 at some point, with the specific timeframe and benchmark methodology governing settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "BlackRock earned $82 million in fees while its crypto funds saw $30 billion in value erased, yet the firm is pursuing further expansion into client wallets."
    publisher: "Oluwapelumi Adejumo"
    published_at: "2026-07-16T09:51:29.000Z"
    source_url: "https://cryptoslate.com/blackrock-made-82-million-as-crypto-erased-30-billion-from-its-funds-now-it-wants-inside-your-wallet/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Oluwapelumi Adejumo"
        source_url: "https://cryptoslate.com/blackrock-made-82-million-as-crypto-erased-30-billion-from-its-funds-now-it-wants-inside-your-wallet/"
        retrieved_at: "2026-07-17T09:53:11+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via CF Benchmarks pricing; the 11% level reflects geopolitical risk-off pressure alongside limited institutional momentum at current spot prices."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Oluwapelumi Adejumo: BlackRock earned $82M while its crypto funds erased $30B, now it want"
    url: "https://cryptoslate.com/blackrock-made-82-million-as-crypto-erased-30-billion-from-its-funds-now-it-wants-inside-your-wallet/"
    published_at: "2026-07-16T09:51:29.000Z"
    retrieved_at: "2026-07-17T09:53:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
