---
signal_id: "CMSIG2026101306"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-10-2026-10-13"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 10%"
semantic_title: "Russia-Ukraine ceasefire by year-end stays a long shot at 10%"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.1
  volume_24h_usd: 21266.076348999995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 10% odds Russia and Ukraine reach a ceasefire in 2026 under a multi-deadline series, resolving via uma_oracle."
  - "Russia's continuation of city strikes, even while sparing energy targets, is consistent with the market's skeptical pricing on a full ceasefire materializing."
  - "A companion Polymarket contract on Ukraine signing a peace deal before 2027 sits at 8%, and a 2026 peace agreement contract is at 5%, all clustering near long-shot territory."
  - "The partial energy-target restraint creates ambiguity for resolution: the market appears to treat an energy pause as distinct from a ceasefire, keeping odds low."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia struck Ukrainian cities overnight while appearing to spare energy infrastructure for the first time since the Trump-brokered energy ceasefire announcement."
    publisher: "By: FRANCE 24"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://www.france24.com/en/europe/20261013-russia-pounds-ukrainian-cities-spares-energy-targets-for-first-time-since-trump-ceasefire"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "By: FRANCE 24"
        source_url: "https://www.france24.com/en/europe/20261013-russia-pounds-ukrainian-cities-spares-energy-targets-for-first-time-since-trump-ceasefire"
        retrieved_at: "2026-10-13T15:32:34+00:00"
  - type: "pm_response"
    notes: "Polymarket holds the Russia-Ukraine 2026 ceasefire at 10%, with peace deal and territory-cession contracts all pricing 5%-8%, reflecting broad market skepticism."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "By: FRANCE 24: Russia pounds Ukrainian cities, spares energy targets for first time s"
    url: "https://www.france24.com/en/europe/20261013-russia-pounds-ukrainian-cities-spares-energy-targets-for-first-time-since-trump-ceasefire"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T15:32:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
