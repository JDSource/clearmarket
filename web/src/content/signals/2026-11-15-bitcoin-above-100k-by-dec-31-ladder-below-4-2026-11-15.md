---
signal_id: "CMSIG2026111508"
signal_slug: "bitcoin-above-100k-by-dec-31-ladder-below-4-2026-11-15"
headline: "Bitcoin above $100K by Dec 31: ladder below 4%"
semantic_title: "Bitcoin above $100K by year-end stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-15T11:30:16.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $100K by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.04
  volume_24h_usd: 135.51
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Ladder puts only 4% odds on Bitcoin exceeding $100,000 by December 31, 2026, with 3% above $110K and 2% above $120K."
  - "Bitcoin's slide to around $64,000-$65,000 amid $1.6 billion in liquidations is fully consistent with the ladder's deep-tail pricing for a year-end $100K scenario."
  - "The ladder implies the market sees no near-term catalyst to close the roughly 55% gap between current spot and the $100K strike before year-end."
  - "Kalshi's Solana above $500 by year-end contract (CM-EVT-1TG94NXKV4) sits at 3%, suggesting broad crypto market pessimism extends beyond Bitcoin alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell below $68,000 this week as crypto liquidations hit $1.6 billion and ETF outflows persisted, pushing BTC to a four-month low near $64,000-$65,000."
    publisher: "Alex Richardson"
    published_at: "2026-11-15T11:30:16.000Z"
    source_url: "https://news.bitcoin.com/featured/bitcoin-falls-dtcc-chooses-solana-for-tokenization-expansion-and-more-weekly-recap/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alex Richardson"
        source_url: "https://news.bitcoin.com/featured/bitcoin-falls-dtcc-chooses-solana-for-tokenization-expansion-and-more-weekly-recap/"
        retrieved_at: "2026-11-16T07:48:02+00:00"
  - type: "pm_response"
    notes: "Ladder resolves via CF Benchmarks Bitcoin reference rate at December 31, 2026; current spot near $64,000-$65,000 makes the $100K threshold a deep out-of-the-money scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alex Richardson: Bitcoin Falls, DTCC Chooses Solana for Tokenization Expansion, and Mor"
    url: "https://news.bitcoin.com/featured/bitcoin-falls-dtcc-chooses-solana-for-tokenization-expansion-and-more-weekly-recap/"
    published_at: "2026-11-15T11:30:16.000Z"
    retrieved_at: "2026-11-16T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
