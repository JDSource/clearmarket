---
signal_id: "CMSIG2026102102"
signal_slug: "dem-senate-control-in-2026-polymarket-68-2026-10-21"
headline: "Dem Senate control in 2026: Polymarket 68%"
semantic_title: "Democrats stay favored to win Senate control in 2026"
telemetry: "Polymarket 68%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-21T21:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.68
  volume_24h_usd: 173645.0662
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a 68% probability that Democrats win Senate control in the 2026 midterms."
  - "Polling momentum toward Democrats is consistent with this pricing, though the 32% Republican tail reflects genuine Senate-map uncertainty."
  - "Kansas's Senate seat Kalshi contract sits at 61% for the Republican, a competitive race that the broader Senate-control odds partially depend on."
  - "The 91% House-flip price on Kalshi versus 68% Senate-flip on Polymarket shows markets treat the chambers as very different battles."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Polls show Trump approval falling and Democrats' generic ballot lead widening two weeks before the 2026 midterms, raising blue-wave talk."
    publisher: "Yahoo"
    published_at: "2026-10-21T21:00:00.000Z"
    source_url: "https://www.yahoo.com/news/politics/article/the-2026-midterms-are-less-than-2-weeks-away-which-party-has-a-better-chance-of-winning-heres-what-the-latest-polls-say-131448048.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yahoo"
        source_url: "https://www.yahoo.com/news/politics/article/the-2026-midterms-are-less-than-2-weeks-away-which-party-has-a-better-chance-of-winning-heres-what-the-latest-polls-say-131448048.html"
        retrieved_at: "2026-10-22T13:24:33+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle; the 68% price is the key cross-venue reference alongside Kalshi's House and chamber-control contracts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yahoo: The 2026 midterms are less than 2 weeks away. Which party has a better"
    url: "https://www.yahoo.com/news/politics/article/the-2026-midterms-are-less-than-2-weeks-away-which-party-has-a-better-chance-of-winning-heres-what-the-latest-polls-say-131448048.html"
    published_at: "2026-10-21T21:00:00.000Z"
    retrieved_at: "2026-10-22T13:24:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
