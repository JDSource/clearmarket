---
signal_id: "CMSIG2026092306"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-14-2026-09-23"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 14%"
semantic_title: "Russia-Ukraine ceasefire in 2026 stays a long shot at 14%"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.14
  volume_24h_usd: 3416.286308
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 14% on a Russia-Ukraine ceasefire in 2026, keeping the outcome a long shot despite Zelenskyy's energy truce offer."
  - "Zelenskyy's readiness for an energy ceasefire and trilateral summit call is a diplomatic step, but markets are not moving from a strongly skeptical baseline."
  - "A companion Polymarket contract puts the odds of Trump, Putin, and Zelenskyy being seen together before 2027 at just 8%, reinforcing that the trilateral meeting itself is seen as unlikely."
  - "A separate Polymarket contract prices Zelenskyy being removed as Ukraine president by end of 2026 at 6%, so the market sees continuity of leadership as far more likely than a ceasefire deal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelenskyy declared Ukraine ready for an energy ceasefire with Russia and called for a trilateral meeting with Putin and Trump following talks with the US."
    publisher: "Al Jazeera Staff"
    published_at: "2026-09-23T00:00:00.000Z"
    source_url: "https://1-e8259.azureedge.net/news/2026/9/23/zelenskyy-says-ukraine-ready-for-energy-truce-with-russia-after-trump-talks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://1-e8259.azureedge.net/news/2026/9/23/zelenskyy-says-ukraine-ready-for-energy-truce-with-russia-after-trump-talks"
        retrieved_at: "2026-09-23T13:17:11+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 14%, resolved via UMA oracle; the 8% trilateral meeting contract suggests markets view a structured peace process as structurally constrained, not just delayed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Zelenskyy says Ukraine ready for energy truce with Russia after Trump"
    url: "https://1-e8259.azureedge.net/news/2026/9/23/zelenskyy-says-ukraine-ready-for-energy-truce-with-russia-after-trump-talks"
    published_at: "2026-09-23T00:00:00.000Z"
    retrieved_at: "2026-09-23T13:17:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
