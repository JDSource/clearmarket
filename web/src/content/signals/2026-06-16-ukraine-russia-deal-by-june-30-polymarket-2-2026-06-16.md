---
signal_id: "CMSIG2026061605"
signal_slug: "ukraine-russia-deal-by-june-30-polymarket-2-2026-06-16"
headline: "Ukraine-Russia deal by June 30: Polymarket 2%"
semantic_title: "Ukraine-Russia peace deal by June 30 priced near zero"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-16T09:02:00.000Z"
event_id: "CM-EVT-91B1JBJW33"
event_slug: "ukraine-signs-peace-deal-with-russia-by-june-30"
event_question: "Will Ukraine sign a peace deal with Russia by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa57a027158ce73973cdd13eed901c6e767a1b9e2f88c665dab8757a65b60d203"
  question_raw: "Ukraine signs peace deal with Russia by June 30?"
  current_price: 0.024
  volume_24h_usd: 1056.587497
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices only 2% probability Ukraine signs a peace deal with Russia by June 30."
  - "Trump's optimistic G7 rhetoric is sharply at odds with the near-zero pricing: markets see no formal deal as imminent despite diplomatic signals."
  - "The broader year-end contract (CM-EVT-DCQYWYX424) sits at 27%, meaning markets assign some probability of a deal in 2026 but not in the next two weeks."
  - "A Putin-Zelenskyy direct meeting by June 30 (CM-EVT-2DR1P4YZ13) prices just 1%, confirming markets see the diplomatic process as still in early stages."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump said Russia should make a peace deal after a G7 meeting with Zelenskyy, calling both sides open to talks."
    publisher: "channelnewsasia.com"
    published_at: "2026-06-16T09:02:00.000Z"
    source_url: "https://www.channelnewsasia.com/world/g7-summit-zelenskyy-trump-ukraine-war-russia-6186861"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "channelnewsasia.com"
        source_url: "https://www.channelnewsasia.com/world/g7-summit-zelenskyy-trump-ukraine-war-russia-6186861"
        retrieved_at: "2026-06-16T12:50:14+00:00"
  - type: "pm_response"
    notes: "Polymarket's June 30 and full-year Ukraine deal contracts together show markets treat Trump's G7 optimism as aspirational, not actionable in the near term."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "channelnewsasia.com: Russia should make peace deal, Trump says after 'very good' Zelenskyy"
    url: "https://www.channelnewsasia.com/world/g7-summit-zelenskyy-trump-ukraine-war-russia-6186861"
    published_at: "2026-06-16T09:02:00.000Z"
    retrieved_at: "2026-06-16T12:50:14+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
