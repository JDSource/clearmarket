---
signal_id: "CMSIG2026100404"
signal_slug: "us-recognizes-pahlavi-as-iran-leader-polymarket-4-2026-10-04"
headline: "US recognizes Pahlavi as Iran leader: Polymarket 4%"
semantic_title: "US recognition of Reza Pahlavi as Iran leader stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-04T00:00:00.000Z"
event_id: "CM-EVT-0SWQB28081"
event_slug: "us-recognizes-reza-pahlavi-as-leader-of-iran-in2026"
event_question: "Will the US recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0ac2141f45ac7ecb8477c64207db37f8f8efce800cbf705366771902e796e92a"
  question_raw: "US recognizes Reza Pahlavi as leader of Iran in 2026?"
  current_price: 0.037
  volume_24h_usd: 31.35
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 4% on the US recognizing Reza Pahlavi as Iran's leader before year-end, keeping regime-change recognition firmly in long-shot territory."
  - "Despite confirmed US strikes on dozens of Iranian targets and a US military buildup, prediction markets are not pricing in a near-term political resolution favorable to the exile leadership."
  - "The Strait of Hormuz reopening-by-year-end Polymarket contract sits at 19%, offering a related read on how far markets believe the conflict will be resolved in 2026."
  - "Resolution via UMA oracle requires an official US government statement of recognition, a high legal bar that explains the compressed pricing even amid active hostilities."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "As the US conducts heavy strikes on Iranian targets after Iranian forces attacked US troops in Jordan, Trump is weighing next steps on Iran amid a growing military buildup."
    publisher: "Peter Martin, Patrick Sykes, Fiona Macdonald, Samy Adghirni"
    published_at: "2026-10-04T00:00:00.000Z"
    source_url: "https://www.japantimes.co.jp/news/2026/10/04/world/pressure-iran-trump-us-military/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Peter Martin, Patrick Sykes, Fiona Macdonald, Samy Adghirni"
        source_url: "https://www.japantimes.co.jp/news/2026/10/04/world/pressure-iran-trump-us-military/"
        retrieved_at: "2026-10-04T07:47:36+00:00"
  - type: "pm_response"
    notes: "Polymarket covers both the Pahlavi recognition question at 4% and the Hormuz normalization question at 19%; the gap between them suggests markets see some commercial resolution as more likely than a political one."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Peter Martin, Patrick Sykes, Fiona Macdonald, Samy Adghirni: Pressure builds on Iran as Trump boosts U.S. military presence - The J"
    url: "https://www.japantimes.co.jp/news/2026/10/04/world/pressure-iran-trump-us-military/"
    published_at: "2026-10-04T00:00:00.000Z"
    retrieved_at: "2026-10-04T07:47:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
