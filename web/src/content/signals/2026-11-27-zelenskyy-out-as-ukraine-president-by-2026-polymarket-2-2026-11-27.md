---
signal_id: "CMSIG2026112704"
signal_slug: "zelenskyy-out-as-ukraine-president-by-2026-polymarket-2-2026-11-27"
headline: "Zelenskyy out as Ukraine president by 2026: Polymarket 2%"
semantic_title: "Zelenskyy staying as Ukraine president remains heavily favored"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-27T02:14:25.000Z"
event_id: "CM-EVT-355Q75KD17"
event_slug: "zelenskyy-out-as-ukraine-president-before-2027"
event_question: "Will Zelenskyy be out as Ukraine president by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x51f624dbbf14f9edb575fef1be6f7a303751de70783fa144fce27b957452c803"
  question_raw: "Zelenskyy out as Ukraine president by end of 2026?"
  current_price: 0.022
  volume_24h_usd: 15608.696539999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 2% chance Zelenskyy leaves the Ukrainian presidency by end of 2026, via UMA oracle."
  - "Zelenskyy's public warning of a major Russian strike and continued diplomatic engagement with Trump align with a leadership-continuity read."
  - "Companion Polymarket contract CM-EVT-5WJSMVBVS7 also sits at 2% for Putin leaving office by year-end, both leaders priced as highly stable."
  - "Resolution requires Zelenskyy to no longer hold the Ukrainian presidency before December 31, 2026, per UMA oracle criteria."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelenskyy warned of a major incoming Russian attack while Trump urged Russian President Vladimir Putin to pull back military aggression."
    publisher: "Al Jazeera Staff"
    published_at: "2026-11-27T02:14:25.000Z"
    source_url: "https://www.aljazeera.com/news/2026/11/27/zelenskyy-warns-of-major-russian-attack-as-trump-urges-putin-to-pull-back"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/11/27/zelenskyy-warns-of-major-russian-attack-as-trump-urges-putin-to-pull-back"
        retrieved_at: "2026-11-27T07:47:43+00:00"
  - type: "pm_response"
    notes: "Polymarket holds both leadership-change contracts at 2%, consistent across the Russia-Ukraine conflict narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Zelenskyy warns of major Russian attack as Trump urges Putin to ‘pull"
    url: "https://www.aljazeera.com/news/2026/11/27/zelenskyy-warns-of-major-russian-attack-as-trump-urges-putin-to-pull-back"
    published_at: "2026-11-27T02:14:25.000Z"
    retrieved_at: "2026-11-27T07:47:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
