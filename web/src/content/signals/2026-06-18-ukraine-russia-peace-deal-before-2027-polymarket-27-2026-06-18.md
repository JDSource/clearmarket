---
signal_id: "CMSIG2026061807"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-27-2026-06-18"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 27%"
semantic_title: "Ukraine-Russia peace deal before 2027 holds below 30 percent"
telemetry: "Polymarket 27%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-18T08:11:58.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.27
  volume_24h_usd: 2915.3355289999995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices only 27% on Ukraine signing a peace deal with Russia before 2027."
  - "A major Ukrainian drone strike on Moscow's Kapotnya refinery, one of the war's largest, is consistent with a market that sees durable peace as unlikely before year-end."
  - "The near-term June 30 peace deal contract (CM-EVT-91B1JBJW33) sits at just 2%, reflecting near-zero probability of imminent resolution despite ongoing diplomacy."
  - "The Putin-Zelenskyy meeting by June 30 contract (CM-EVT-2DR1P4YZ13) is priced at 1%, signaling the market sees no credible near-term leadership engagement either."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian drones struck the Moscow oil refinery in one of the largest drone attacks of the war, even as Zelenskyy sought Trump's support to end the conflict."
    publisher: "Al Jazeera Staff"
    published_at: "2026-06-18T08:11:58.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/18/ukraine-hits-moscow-refinery-as-zelenskyy-seeks-trump-support-to-end-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/6/18/ukraine-hits-moscow-refinery-as-zelenskyy-seeks-trump-support-to-end-war"
        retrieved_at: "2026-06-18T11:48:44+00:00"
  - type: "pm_response"
    notes: "The Polymarket contract resolves via uma_oracle; a formal signed peace agreement, not a ceasefire or MoU, is the likely resolution standard."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Ukraine hits Moscow refinery as Zelenskyy seeks Trump support to end w"
    url: "https://www.aljazeera.com/news/2026/6/18/ukraine-hits-moscow-refinery-as-zelenskyy-seeks-trump-support-to-end-war"
    published_at: "2026-06-18T08:11:58.000Z"
    retrieved_at: "2026-06-18T11:48:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
