---
signal_id: "CMSIG2026062407"
signal_slug: "btc-above-100k-by-dec-31-kalshi-ladder-below-18-2026-06-24"
headline: "BTC above $100K by Dec 31: Kalshi ladder below 18%"
semantic_title: "Bitcoin above $100K by year-end pricing fractures below 20 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T04:33:03.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $99,999 by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.18
  volume_24h_usd: 490.69
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-01T04:59:00Z"
bullets:
  - "Kalshi ladder puts only 18% on Bitcoin exceeding $100K by year-end, with odds falling sharply to 4% above $150K."
  - "Bitcoin trading near $62K amid a chip-stock-driven risk-off move is consistent with the market pricing a large gap to the $100K threshold."
  - "The end-of-June BTC above $75K ladder (CM-EVT-3MXSH7KHK5) shows just 8% probability, confirming near-term weakness feeds the year-end discount."
  - "Resolves via Kalshi at 11:59 PM ET on Dec 31, 2026; a sustained recovery through $100K from current levels would require roughly a 60% rally."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin dropped toward $62,000 as a semiconductor stock selloff deepened risk-off sentiment across crypto markets."
    publisher: "coindesk.com"
    published_at: "2026-06-24T04:33:03.000Z"
    source_url: "https://www.coindesk.com/markets/2026/06/24/bitcoin-drops-toward-usd62-000-as-the-chip-selloff-deepens-for-a-second-day"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/06/24/bitcoin-drops-toward-usd62-000-as-the-chip-selloff-deepens-for-a-second-day"
        retrieved_at: "2026-06-24T10:45:49+00:00"
  - type: "pm_response"
    notes: "Kalshi's year-end ladder and the end-of-June above-$75K contract (8%) jointly anchor Bitcoin well below the $100K level, consistent with the current spot selloff."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: BTC price news: Bitcoin drops to $62,000 as the chip selloff deepens f"
    url: "https://www.coindesk.com/markets/2026/06/24/bitcoin-drops-toward-usd62-000-as-the-chip-selloff-deepens-for-a-second-day"
    published_at: "2026-06-24T04:33:03.000Z"
    retrieved_at: "2026-06-24T10:45:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
