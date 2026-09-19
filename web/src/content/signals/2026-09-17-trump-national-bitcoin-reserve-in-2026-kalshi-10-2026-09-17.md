---
signal_id: "CMSIG2026091706"
signal_slug: "trump-national-bitcoin-reserve-in-2026-kalshi-10-2026-09-17"
headline: "Trump National Bitcoin Reserve in 2026: Kalshi 10%"
semantic_title: "National Bitcoin Reserve becoming law stays a long shot"
telemetry: "Kalshi 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-17T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.095
  volume_24h_usd: 41.05
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts 10% odds on Trump creating a National Bitcoin Reserve in 2026, with trading volume up more than 10,000 times day-over-day, a sharp signal of fresh market attention."
  - "The House committee passage is a meaningful legislative step, but the market's 10% reading shows strong skepticism that the full legislative process will clear before year-end."
  - "The companion Polymarket contract on the US establishing a national Bitcoin reserve before 2027 sits at 7%, consistent with Kalshi's cautious pricing across venues."
  - "Resolution via The New York Times reporting; the contract likely requires formal law, not merely the existing executive order, explaining the gap between news momentum and price."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A US House committee advanced a bill that would codify Trump's Strategic Bitcoin Reserve executive order into law, locking up Bitcoin acquired through forfeitures."
    publisher: "cointelegraph.com"
    published_at: "2026-09-17T00:00:00.000Z"
    source_url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cointelegraph.com"
        source_url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
        retrieved_at: "2026-09-19T12:14:43+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via New York Times; the extraordinary volume surge alongside a still-low 10% price indicates the news is drawing significant attention without convincing the market of near-term passage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cointelegraph.com: US Bitcoin reserve bill passes House Committee"
    url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
    published_at: "2026-09-17T00:00:00.000Z"
    retrieved_at: "2026-09-19T12:14:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
