---
signal_id: "CMSIG2026102708"
signal_slug: "bitcoin-above-100k-by-dec-31-prediction-market-20-2026-10-27"
headline: "Bitcoin above $100K by Dec 31: prediction market 20%"
semantic_title: "Bitcoin above $100K by year-end draws fresh attention near 20 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "market-implied level"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.2
  volume_24h_usd: 1637.91
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "The prediction market ladder prices 20% on Bitcoin exceeding $99,999.99 by December 31, 2026, with trading volume up 5,925% day over day."
  - "Bitcoin's intraday rebound toward $81,000-$82,000 and the 60x volume surge in the year-end $100K contract signal that the rally is drawing fresh speculative positioning."
  - "The ladder shows probability collapsing sharply above $100K: 20% at the $100K threshold, 9% at $110K, and 5% at $120K, implying limited conviction in a sustained breakout."
  - "The Kalshi contract on Bitcoin's minimum price reaching a floor by January 1, 2027 (CM-EVT-NHW1YL14S9) at 5% provides a downside anchor for comparison against the $100K upside tail."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin has rebounded toward $82,000 with a tokenized fund launch on the XRP Ledger and improving ETF inflows supporting risk sentiment."
    publisher: "theblock.co"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-27-aviva-investors-ripple-xrp-ledger-more-crypto-news-431809"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-27-aviva-investors-ripple-xrp-ledger-more-crypto-news-431809"
        retrieved_at: "2026-10-28T14:49:33+00:00"
  - type: "pm_response"
    notes: "The 60x volume spike in the year-end $100K Bitcoin contract is the strongest single-day activity signal in today's crypto suite, coinciding with the BTC rebound and risk-on tone ahead of the Fed decision."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: Aviva Investors and Ripple launch tokenized share class of $29 billion"
    url: "https://www.theblock.co/newsletters/the-daily/2026-10-27-aviva-investors-ripple-xrp-ledger-more-crypto-news-431809"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-28T14:49:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
