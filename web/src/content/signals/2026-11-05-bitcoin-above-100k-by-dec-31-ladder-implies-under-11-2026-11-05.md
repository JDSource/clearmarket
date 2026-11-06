---
signal_id: "CMSIG2026110508"
signal_slug: "bitcoin-above-100k-by-dec-31-ladder-implies-under-11-2026-11-05"
headline: "Bitcoin above $100K by Dec 31: ladder implies under 11%"
semantic_title: "Bitcoin above $100K by year-end stays a long shot after selloff"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-11-05T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price by December 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.11
  volume_24h_usd: 2736.7
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Ladder prices only 11% above $100K, 4% above $110K, and 2% above $120K or higher, placing the year-end $100K threshold firmly in long-shot territory."
  - "Bitcoin's drop from above $80K to near $75.5K as reported is directionally consistent with the ladder's low probability on a $100K year-end outcome."
  - "Volume on the ladder surged 201.9x day over day, the second-largest spike in this dataset, reflecting heavy repositioning after the crypto liquidation event."
  - "Kalshi (CM-EVT-NHW1YL14S9) prices only 5% on Bitcoin setting a minimum price of $1 at or above its current level by January 1, 2027, suggesting year-end floor risk is also being priced."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin erased its post-midterm election gains, falling below $76,000 as a broader Wall Street selloff triggered over $1 billion in crypto liquidations."
    publisher: "theblock.co"
    published_at: "2026-11-05T00:00:00.000Z"
    source_url: "https://www.theblock.co/news/markets/2026-11-05-bitcoin-erases-post-election-gains-wall-street-selloff-liquidations-435434"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/news/markets/2026-11-05-bitcoin-erases-post-election-gains-wall-street-selloff-liquidations-435434"
        retrieved_at: "2026-11-06T07:48:14+00:00"
  - type: "pm_response"
    notes: "Ladder volume up 201.9x day over day; resolution is based on Bitcoin price versus $99,999.99 by December 31, 2026 at 11:59 PM ET."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: Bitcoin erases post-election gains as Wall Street selloff triggers ove"
    url: "https://www.theblock.co/news/markets/2026-11-05-bitcoin-erases-post-election-gains-wall-street-selloff-liquidations-435434"
    published_at: "2026-11-05T00:00:00.000Z"
    retrieved_at: "2026-11-06T07:48:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
