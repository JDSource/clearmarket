---
signal_id: "CMSIG2026061705"
signal_slug: "any-ship-transit-strait-of-hormuz-by-june-30-polymarket-28-2026-06-17"
headline: "Any ship transit Strait of Hormuz by June 30: Polymarket 28%"
semantic_title: "Any Hormuz transit by June 30 holds at low single odds"
telemetry: "Polymarket 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-17T08:57:25.000Z"
event_id: "CM-EVT-VB1YHPRLZ3"
event_slug: "will-ships-transit-the-strait-of-hormuz-on-any-day-by-june-30"
event_question: "Will any ships transit the Strait of Hormuz by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc38b96e6fb12fc68d003ff326f2a11eb3c8f04c2fce7fcfc9d62f5e18131817c"
  question_raw: "Will 60 ships transit the Strait of Hormuz on any day by June 30, 2026?"
  current_price: 0.28
  volume_24h_usd: 18035.20589
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T16:00:00Z"
bullets:
  - "Polymarket prices any ship transiting the Strait of Hormuz by June 30 at just 28%, despite tanker repositioning news."
  - "Tankers exiting the blockade zone signals tentative movement but markets treat physical Strait transit as a materially higher bar than repositioning in the Gulf of Oman."
  - "The unrestricted shipping contract (Polymarket 31%) is priced nearly identically, suggesting markets see minimal probability of partial transit without full reopening."
  - "Resolves via portwatch.imf.org transit data; vessel tracking will be the settlement arbiter, not diplomatic statements."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iranian tankers exited the US blockade zone ahead of ceasefire talks, with cargo vessels observed repositioning in the Gulf of Oman."
    publisher: "Al Jazeera Staff"
    published_at: "2026-06-17T08:57:25.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/17/first-iranian-tankers-exit-us-blockade-zone-ahead-of-peace-talks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/6/17/first-iranian-tankers-exit-us-blockade-zone-ahead-of-peace-talks"
        retrieved_at: "2026-06-17T12:13:58+00:00"
  - type: "pm_response"
    notes: "Polymarket's 28% on any transit and 31% on unrestricted shipping by June 30 are nearly convergent, implying an all-or-nothing market read on Hormuz reopening."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Iranian tankers exit US blockade zone before talks to end war | US-Isr"
    url: "https://www.aljazeera.com/news/2026/6/17/first-iranian-tankers-exit-us-blockade-zone-ahead-of-peace-talks"
    published_at: "2026-06-17T08:57:25.000Z"
    retrieved_at: "2026-06-17T12:13:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
