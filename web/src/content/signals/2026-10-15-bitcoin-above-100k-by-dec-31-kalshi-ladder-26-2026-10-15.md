---
signal_id: "CMSIG2026101508"
signal_slug: "bitcoin-above-100k-by-dec-31-kalshi-ladder-26-2026-10-15"
headline: "Bitcoin above $100K by Dec 31: Kalshi ladder 26%"
semantic_title: "Bitcoin above $100K by year-end stays below 25 percent odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T04:50:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin end-of-year price level"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.26
  volume_24h_usd: 1712.04
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Kalshi ladder prices Bitcoin above $100K by December 31 at 26%, with the $110K tier collapsing to 10% and higher strikes in low single digits."
  - "The hot CPI print and surge in rate hike expectations are consistent with current pricing showing Bitcoin well under the $100K threshold."
  - "The companion Kalshi contract on a Bitcoin minimum price by January 1, 2027 (CM-EVT-NHW1YL14S9) sits at 5%, suggesting material downside is also priced."
  - "From spot near $81K, a 23%-plus rally by December 31 is needed to breach $100K; the ladder implies that is a minority outcome at current macro conditions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell toward $80,000 as hotter-than-expected September CPI data spurred rate hike bets, triggering nearly $1 billion in crypto liquidations."
    publisher: "theblock.co"
    published_at: "2026-10-15T04:50:00.000Z"
    source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-15-the-daily-coinbase-outlines-priorities-for-bitcoins-post-quantum-migration-and-more-418619"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-15-the-daily-coinbase-outlines-priorities-for-bitcoins-post-quantum-migration-and-more-418619"
        retrieved_at: "2026-10-15T13:02:56+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via CF Benchmarks; the distribution from $100K to $200K collapses rapidly, showing end-of-year upside scenarios are heavily discounted."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: The Daily: Coinbase outlines priorities for Bitcoin's post-quantum mig"
    url: "https://www.theblock.co/newsletters/the-daily/2026-10-15-the-daily-coinbase-outlines-priorities-for-bitcoins-post-quantum-migration-and-more-418619"
    published_at: "2026-10-15T04:50:00.000Z"
    retrieved_at: "2026-10-15T13:02:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
