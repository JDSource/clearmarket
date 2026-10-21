---
signal_id: "CMSIG2026102107"
signal_slug: "trump-meets-putin-by-2026-polymarket-84-2026-10-21"
headline: "Trump meets Putin by 2026: Polymarket 84%"
semantic_title: "Trump meeting Putin by year-end stays heavily favored"
telemetry: "Polymarket 84%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-21T00:00:00.000Z"
event_id: "CM-EVT-TK9WNXXYF6"
event_slug: "trump-meets-with-putin-by"
event_question: "Will Trump meet with Putin by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x15ddba100cf49043ada06a98d63ac221cdca86da873485dcca72c174cb9cc300"
  question_raw: "Trump meets with Putin by December 31?"
  current_price: 0.84
  volume_24h_usd: 5751.815882999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices an 84% probability that US President Donald Trump will meet Putin by end of 2026, resolved via uma_oracle."
  - "Witkoff's scheduled Russia visit and the Oslo intelligence-sharing restoration both point toward active diplomatic contact, consistent with the high Polymarket probability on a Trump-Putin meeting."
  - "The related Polymarket contract on a three-way Trump-Putin-Zelensky meeting (CM-EVT-FNBRJ6KY59) sits at only 9%, showing the market sees bilateral US-Russia contact as far more likely than a trilateral summit."
  - "Resolution via uma_oracle requires documented evidence of an in-person Trump-Putin meeting before January 1, 2027; the 75-percentage-point gap between bilateral and trilateral meeting odds captures the market's skepticism on Ukraine's seat at the table."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Zelensky confirmed US intelligence sharing was restored following talks in Oslo, while US envoy Steve Witkoff is scheduled to meet Russian President Vladimir Putin in Russia."
    publisher: "Shweta Sharma"
    published_at: "2026-10-21T00:00:00.000Z"
    source_url: "https://www.the-independent.com/news/world/europe/ukraine-russia-war-live-trump-zelensky-putin-starlink-oslo-peace-talks-b3070403.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shweta Sharma"
        source_url: "https://www.the-independent.com/news/world/europe/ukraine-russia-war-live-trump-zelensky-putin-starlink-oslo-peace-talks-b3070403.html"
        retrieved_at: "2026-10-21T07:48:07+00:00"
  - type: "pm_response"
    notes: "Polymarket at 84% on a Trump-Putin bilateral meeting, versus only 9% on a trilateral summit including Zelensky, is the key diplomatic term-structure signal in today's Ukraine coverage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shweta Sharma: Ukraine-Russia war latest: Zelensky says Trump has restored intel shar"
    url: "https://www.the-independent.com/news/world/europe/ukraine-russia-war-live-trump-zelensky-putin-starlink-oslo-peace-talks-b3070403.html"
    published_at: "2026-10-21T00:00:00.000Z"
    retrieved_at: "2026-10-21T07:48:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
