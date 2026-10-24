---
signal_id: "CMSIG2026102305"
signal_slug: "russia-ukraine-ceasefire-by-2026-polymarket-13-2026-10-23"
headline: "Russia-Ukraine ceasefire by 2026: Polymarket 13%"
semantic_title: "Russia-Ukraine ceasefire in 2026 stays a long shot at 13 percent"
telemetry: "Polymarket 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-23T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.13
  volume_24h_usd: 2751.413852
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices a Russia-Ukraine ceasefire in 2026 at only 13%, treating the event as a long shot."
  - "The Oleshky localized ceasefire is a narrow, city-level arrangement, Polymarket's 13% reflects limited confidence this translates to a broader agreement by year-end."
  - "A companion Polymarket contract (CM-EVT-LVRHCH4653) on a ceasefire by June 2026 sits at 20%, implying the market assigns slightly higher odds to the earlier deadline, an apparent data anomaly worth noting but not resolving here."
  - "Resolution is via uma_oracle on Polymarket; the multi-deadline series structure means each deadline settles independently."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The White House said Melania Trump brokered a localized ceasefire deal in the Ukrainian city of Oleshky, raising questions about broader peace progress."
    publisher: "PBS News Hour"
    published_at: "2026-10-23T00:00:00.000Z"
    source_url: "https://www.pbs.org/newshour/show/news-wrap-white-house-says-melania-trump-brokered-localized-ceasefire-deal-in-oleshky"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "PBS News Hour"
        source_url: "https://www.pbs.org/newshour/show/news-wrap-white-house-says-melania-trump-brokered-localized-ceasefire-deal-in-oleshky"
        retrieved_at: "2026-10-24T07:48:16+00:00"
  - type: "pm_response"
    notes: "Polymarket holds the 2026 ceasefire at 13%, treating the Oleshky development as insufficient evidence of a broader peace breakthrough."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "PBS News Hour: News Wrap: White House says Melania Trump brokered localized ceasefire"
    url: "https://www.pbs.org/newshour/show/news-wrap-white-house-says-melania-trump-brokered-localized-ceasefire-deal-in-oleshky"
    published_at: "2026-10-23T00:00:00.000Z"
    retrieved_at: "2026-10-24T07:48:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
