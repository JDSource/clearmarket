---
signal_id: "CMSIG2026092207"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-14-2026-09-22"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 14%"
semantic_title: "Russia-Ukraine ceasefire in 2026 remains a long shot at 14 percent"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-22T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.14
  volume_24h_usd: 2934.081216
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices a Russia-Ukraine ceasefire in 2026 at 14%, a clear long-shot despite active diplomacy."
  - "Zelensky's push for an energy truce in talks with Trump shows diplomatic momentum, but Polymarket at 14% signals the market does not expect a formal ceasefire to materialize this year."
  - "The companion Polymarket contract on Trump, Putin, and Zelensky being seen together before 2027 sits at only 8%, suggesting the market doubts even a summit, let alone a peace deal."
  - "Resolves via Polymarket's uma_oracle upon confirmation of a formally agreed ceasefire between Russia and Ukraine."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelensky arrived in New York for a high-stakes meeting with Trump at the UN, pushing for an energy infrastructure truce with Russia."
    publisher: "Tom Balmforth"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/europe/zelenskiy-meet-trump-un-push-energy-truce-with-russia-2026-09-22/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tom Balmforth"
        source_url: "https://www.reuters.com/world/europe/zelenskiy-meet-trump-un-push-energy-truce-with-russia-2026-09-22/"
        retrieved_at: "2026-09-22T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket at 14% reflects a market that sees Zelensky's UN push as insufficient to bridge the gap to a full ceasefire within 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tom Balmforth: Zelenskiy to meet Trump at UN in push for energy truce with Russia | R"
    url: "https://www.reuters.com/world/europe/zelenskiy-meet-trump-un-push-energy-truce-with-russia-2026-09-22/"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-22T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
