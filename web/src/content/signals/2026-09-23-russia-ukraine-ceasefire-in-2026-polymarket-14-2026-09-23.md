---
signal_id: "CMSIG2026092306"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-14-2026-09-23"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 14%"
semantic_title: "Russia-Ukraine ceasefire in 2026 remains a long shot"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T01:20:39.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.14
  volume_24h_usd: 1764.22345
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Russia and Ukraine reaching a ceasefire in 2026 sits at 14%, still a long shot."
  - "Zelenskyy's energy truce proposal and Trump's comment that both sides are ready represent positive signals, yet the market prices only a 14% chance of a full ceasefire."
  - "The gap between diplomatic noise and the 14% ceasefire probability reflects market skepticism that an energy truce converts to a broader peace deal this year."
  - "The Polymarket contract on Zelenskyy being out as Ukraine president by end of 2026 sits at 6%, suggesting the market does not see leadership change as a resolution path."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelenskyy announced Ukraine is ready for an energy truce with Russia following talks with US President Donald Trump on the sidelines of the UN General Assembly."
    publisher: "Al Jazeera Staff"
    published_at: "2026-09-23T01:20:39.000Z"
    source_url: "https://www.aljazeera.com/news/2026/9/23/zelenskyy-says-ukraine-ready-for-energy-truce-with-russia-after-trump-talks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/9/23/zelenskyy-says-ukraine-ready-for-energy-truce-with-russia-after-trump-talks"
        retrieved_at: "2026-09-23T07:47:29+00:00"
  - type: "pm_response"
    notes: "Polymarket prices a 2026 Russia-Ukraine ceasefire at 14% via uma_oracle, remaining a long shot despite the Zelenskyy-Trump UNGA meeting and energy truce signals."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Zelenskyy says Ukraine ready for energy truce with Russia after Trump"
    url: "https://www.aljazeera.com/news/2026/9/23/zelenskyy-says-ukraine-ready-for-energy-truce-with-russia-after-trump-talks"
    published_at: "2026-09-23T01:20:39.000Z"
    retrieved_at: "2026-09-23T07:47:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
