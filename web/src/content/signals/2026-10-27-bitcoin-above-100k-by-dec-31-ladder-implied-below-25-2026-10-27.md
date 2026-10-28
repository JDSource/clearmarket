---
signal_id: "CMSIG2026102708"
signal_slug: "bitcoin-above-100k-by-dec-31-ladder-implied-below-25-2026-10-27"
headline: "Bitcoin above $100K by Dec 31: Ladder implied below 25%"
semantic_title: "Bitcoin above $100K by year-end priced below 25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $100K by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.21
  volume_24h_usd: 1775.82
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "The prediction market ladder prices only 21% on Bitcoin exceeding $99,999.99 by December 31, 2026, with higher strikes at single-digit probabilities."
  - "Bitcoin near $81,000 is roughly 24% below the $100K threshold; the market treats a year-end surge past that level as possible but unlikely."
  - "Trading volume in this ladder is up 5,925% day-over-day, signaling a sharp surge in fresh attention on the year-end Bitcoin price question."
  - "The ladder collapses steeply above $100K: 9% at $110K, 5% at $120K, indicating the market sees a six-figure year-end as a fat-tail scenario, not a base case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin is trading near $80,000-$81,000 ahead of the Federal Reserve rate decision, with ETF inflows returning and risk appetite supported by tech earnings."
    publisher: "theblock.co"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-27-aviva-investors-ripple-xrp-ledger-more-crypto-news-431809"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-27-aviva-investors-ripple-xrp-ledger-more-crypto-news-431809"
        retrieved_at: "2026-10-28T07:49:08+00:00"
  - type: "pm_response"
    notes: "Volume on this ladder spiked roughly 60-fold day-over-day, making it the most active Bitcoin prediction market signal in today's data; resolves based on Bitcoin price at 11:59 PM ET on December 31, 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: Aviva Investors and Ripple launch tokenized share class of $29 billion"
    url: "https://www.theblock.co/newsletters/the-daily/2026-10-27-aviva-investors-ripple-xrp-ledger-more-crypto-news-431809"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-28T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
