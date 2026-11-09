---
signal_id: "CMSIG2026110604"
signal_slug: "us-ai-safety-bill-by-2027-polymarket-8-2026-11-06"
headline: "US AI safety bill by 2027: Polymarket 8%"
semantic_title: "US AI safety bill before 2027 stays a long shot"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T10:00:00.000Z"
event_id: "CM-EVT-WMMFP7Y6G5"
event_slug: "us-enacts-ai-safety-bill-before-2027"
event_question: "Will the U.S. enact an AI safety bill before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcdbf64cb434d132ae3eba2c6d4aa8123dde9f90bd8641a5cd31ceddee6d935b8"
  question_raw: "U.S. enacts AI safety bill before 2027?"
  current_price: 0.08
  volume_24h_usd: 52.85
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices only an 8% chance the US enacts an AI safety bill before 2027."
  - "Despite AI safety advocates claiming a political win in the midterms, the market is not pricing a near-term legislative breakthrough."
  - "Democrats winning Congress changes the composition but not the short-term timeline; the 8% pricing implies the market sees 2026 legislation as very unlikely."
  - "Resolution via UMA oracle; the question resolves on enactment before January 1, 2027, leaving very little calendar runway."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Politico reports that AI safety advocates, populists, and child-safety groups united in the 2026 midterms, handing Democrats a potential 2028 legislative issue."
    publisher: "Calder McHugh, Alec Hernandez"
    published_at: "2026-11-06T10:00:00.000Z"
    source_url: "https://www.politico.com/news/magazine/2026/11/06/ai-big-tech-2026-midterms-anthropic-openai-01152312"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Calder McHugh, Alec Hernandez"
        source_url: "https://www.politico.com/news/magazine/2026/11/06/ai-big-tech-2026-midterms-anthropic-openai-01152312"
        retrieved_at: "2026-11-09T07:47:40+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; the market is fading the narrative that a midterm shift translates into immediate AI legislation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Calder McHugh, Alec Hernandez: The AI Doomers Won 2026"
    url: "https://www.politico.com/news/magazine/2026/11/06/ai-big-tech-2026-midterms-anthropic-openai-01152312"
    published_at: "2026-11-06T10:00:00.000Z"
    retrieved_at: "2026-11-09T07:47:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
