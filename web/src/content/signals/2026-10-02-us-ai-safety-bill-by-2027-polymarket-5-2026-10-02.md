---
signal_id: "CMSIG2026100205"
signal_slug: "us-ai-safety-bill-by-2027-polymarket-5-2026-10-02"
headline: "US AI safety bill by 2027: Polymarket 5%"
semantic_title: "US AI safety bill before 2027 stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-02T00:00:00.000Z"
event_id: "CM-EVT-WMMFP7Y6G5"
event_slug: "us-enacts-ai-safety-bill-before-2027"
event_question: "Will the U.S. enact an AI safety bill before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcdbf64cb434d132ae3eba2c6d4aa8123dde9f90bd8641a5cd31ceddee6d935b8"
  question_raw: "U.S. enacts AI safety bill before 2027?"
  current_price: 0.05
  volume_24h_usd: 1739.61
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on the U.S. enacting an AI safety bill before 2027 prices at just 5%, placing it firmly in long-shot territory."
  - "Hawley's hearing generated legislative momentum in principle, but the Polymarket contract's 5% indicates the market is not treating the hearing as a meaningful step toward passage."
  - "A companion Polymarket contract on AI being charged with a crime before 2027 sits at 8%, similarly low, the market broadly discounts near-term AI legal or regulatory action."
  - "Resolves via UMA oracle; the bill would need to pass both chambers and be signed before year-end 2026, a very compressed timeline given the current 5% pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Senator Josh Hawley held a September hearing on rogue AI agents and is pushing for AI legislation, even as prospects for any bill passing dim."
    publisher: "John Hendel"
    published_at: "2026-10-02T00:00:00.000Z"
    source_url: "https://www.politico.com/news/2026/10/02/hawley-tests-trumps-hands-off-approach-to-ai-01104288"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "John Hendel"
        source_url: "https://www.politico.com/news/2026/10/02/hawley-tests-trumps-hands-off-approach-to-ai-01104288"
        retrieved_at: "2026-10-02T14:25:25+00:00"
  - type: "pm_response"
    notes: "Polymarket prices the AI safety bill at 5%, unchanged from pre-hearing levels, indicating the market is not pricing Hawley's push as a credible near-term legislative catalyst."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "John Hendel: Hawley tests Trump’s hands-off approach to AI - POLITICO"
    url: "https://www.politico.com/news/2026/10/02/hawley-tests-trumps-hands-off-approach-to-ai-01104288"
    published_at: "2026-10-02T00:00:00.000Z"
    retrieved_at: "2026-10-02T14:25:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
