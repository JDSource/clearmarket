---
signal_id: "CMSIG2026091506"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-14-2026-09-15"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 14%"
semantic_title: "Russia-Ukraine ceasefire in 2026 stays a long shot"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-15T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.14
  volume_24h_usd: 8917.263335
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Russia-Ukraine ceasefire in 2026 at 14%, resolving via UMA oracle."
  - "Zelenskyy's conditional stance, no ceasefire until Russia stops, is consistent with a market that prices resolution as unlikely: the news reinforces the low probability."
  - "Ukraine territory cession contract (CM-EVT-XP7FFT2MC9) sits at 8%, suggesting the market sees neither a ceasefire nor a territorial concession as probable this year."
  - "New US-mediated trilateral talks are reported for October (Story 23), but Polymarket's 14% shows the market is not pricing a breakthrough from the upcoming round."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Zelenskyy confirmed Ukraine will not implement an energy ceasefire unless Russia halts strikes first, complicating US-mediated peace efforts."
    publisher: "Warren Murray"
    published_at: "2026-09-15T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/sep/15/ukraine-war-briefing-no-energy-ceasefire-until-russia-stops-zelenskyy-confirms-after-trump-claim"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Warren Murray"
        source_url: "https://www.theguardian.com/world/2026/sep/15/ukraine-war-briefing-no-energy-ceasefire-until-russia-stops-zelenskyy-confirms-after-trump-claim"
        retrieved_at: "2026-09-15T13:05:57+00:00"
  - type: "pm_response"
    notes: "Polymarket's multi-deadline series resolves via UMA oracle; the 14% reflects accumulated talk-without-deal precedent, not a single news-driven reprice."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Warren Murray: Ukraine war briefing: No energy ceasefire until Russia stops, Zelensky"
    url: "https://www.theguardian.com/world/2026/sep/15/ukraine-war-briefing-no-energy-ceasefire-until-russia-stops-zelenskyy-confirms-after-trump-claim"
    published_at: "2026-09-15T00:00:00.000Z"
    retrieved_at: "2026-09-15T13:05:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
