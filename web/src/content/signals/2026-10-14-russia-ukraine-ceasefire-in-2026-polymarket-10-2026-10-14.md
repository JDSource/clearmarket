---
signal_id: "CMSIG2026101404"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-10-2026-10-14"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 10%"
semantic_title: "Russia-Ukraine ceasefire in 2026 stays a long shot at 10%"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T07:32:17.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.1
  volume_24h_usd: 18841.91
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 10% on Russia and Ukraine reaching a ceasefire in 2026."
  - "Active Russian strikes on energy sites covered by Trump's announced ceasefire are consistent with the market's skeptical pricing, the ceasefire is being violated in real time."
  - "A companion Polymarket contract at 6% on Ukraine ceding territory to Russia by 2026 suggests markets see neither peace nor territorial concession as likely this year."
  - "Resolves via uma_oracle; a formal, publicly announced ceasefire agreement between the two parties would be required, partial or unilateral declarations likely would not qualify."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Zelenskyy voiced outrage as Russia continued striking Ukrainian energy infrastructure despite a Trump-announced energy ceasefire, with allies reportedly giving no warning of incoming ballistic missiles."
    publisher: "Hanna Arhirova and Samya Kullab"
    published_at: "2026-10-14T07:32:17.000Z"
    source_url: "https://apnews.com/article/russia-ukraine-war-zelenskyy-burnham-trump-putin-9fe44ec1bb361f19d46dfafb58da46f6"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Hanna Arhirova and Samya Kullab"
        source_url: "https://apnews.com/article/russia-ukraine-war-zelenskyy-burnham-trump-putin-9fe44ec1bb361f19d46dfafb58da46f6"
        retrieved_at: "2026-10-14T13:17:09+00:00"
  - type: "pm_response"
    notes: "Polymarket at 10% is consistent with the on-the-ground reporting: active strikes and no diplomatic framework in place."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Hanna Arhirova and Samya Kullab: Zelenskyy says Russia keeps striking Ukraine’s energy sites despite Tr"
    url: "https://apnews.com/article/russia-ukraine-war-zelenskyy-burnham-trump-putin-9fe44ec1bb361f19d46dfafb58da46f6"
    published_at: "2026-10-14T07:32:17.000Z"
    retrieved_at: "2026-10-14T13:17:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
