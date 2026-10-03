---
signal_id: "CMSIG2026093002"
signal_slug: "negative-us-gdp-2026-polymarket-2-2026-09-30"
headline: "Negative US GDP 2026: Polymarket 2%"
semantic_title: "Negative US GDP in 2026 remains a long shot at 2 percent"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-36YHF72CQ8"
event_slug: "negative-gdp-growth-in-2026"
event_question: "Will there be negative GDP growth in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd8c1b0a73653b1fb4fb6e8d13d0063d25810870d7ddf83e61fffb4de4522edf1"
  question_raw: "Negative GDP growth in 2026?"
  current_price: 0.02
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-29T00:00:00Z"
bullets:
  - "Polymarket puts only 2% on negative US GDP growth in 2026, via UMA oracle resolution."
  - "The Q2 upward revision to 2.2% is consistent with the near-zero probability the prediction market assigns to a full-year contraction."
  - "The September jobs miss of 29,000 is a Q4 headwind but does not materially shift the annual contraction calculus given the strong Q2 base."
  - "Companion Polymarket contract on Republican winning Oklahoma 3rd CD at 97% shares the UMA oracle resolver but carries no macro relevance as a cross-check."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Commerce Department revised Q2 2026 GDP growth up to 2.2% from 1.5%, with inflation steady and private payrolls holding firm."
    publisher: "Asad HASHIM"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://finance.yahoo.com/economy/articles/us-reports-firm-q2-economic-134553724.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Asad HASHIM"
        source_url: "https://finance.yahoo.com/economy/articles/us-reports-firm-q2-economic-134553724.html"
        retrieved_at: "2026-10-03T07:47:35+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 2% pricing leaves almost no room for macro deterioration to shift the annual verdict."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Asad HASHIM: US reports firm Q2 economic growth, inflation steady"
    url: "https://finance.yahoo.com/economy/articles/us-reports-firm-q2-economic-134553724.html"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-10-03T07:47:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
