---
signal_id: "CMSIG2026102406"
signal_slug: "trump-putin-zelensky-together-before-2027-polymarket-6-2026-10-24"
headline: "Trump-Putin-Zelensky together before 2027: Polymarket 6%"
semantic_title: "Odds on Trump-Putin-Zelensky summit before 2027 stay very low"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-24T00:00:00.000Z"
event_id: "CM-EVT-QP1YL1BSS0"
event_slug: "trump-putin-and-zelensky-seen-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky be seen together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa04dcb7b7f5a313d09e7728ca39835be4096da877ca5fbae5e3a36af239433c3"
  question_raw: "Trump, Putin, and Zelensky seen together before 2027?"
  current_price: 0.06
  volume_24h_usd: 1139.1
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market puts only 6% odds on Trump, Putin, and Zelensky appearing together before 2027."
  - "Zelensky's Abu Dhabi trilateral proposal is a concrete step, but Polymarket's 6% shows the market is not treating the offer as a near-certainty of physical co-presence."
  - "The Polymarket contract (CM-EVT-DCQYWYX424) on Ukraine signing a peace deal with Russia before 2027 sits at 14%, a wider spread suggesting markets see peace talks as more plausible than a summit photo op."
  - "Resolution is via uma_oracle on Polymarket; the contract likely requires documented, confirmed co-presence of all three leaders at the same event."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelensky said Ukraine is ready to hold a trilateral meeting with the United States and Russia next month in Abu Dhabi."
    publisher: "english.news.cn"
    published_at: "2026-10-24T00:00:00.000Z"
    source_url: "https://english.news.cn/20261024/e0b2fbf7f7324349973c6eb1bc463150/c.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "english.news.cn"
        source_url: "https://english.news.cn/20261024/e0b2fbf7f7324349973c6eb1bc463150/c.html"
        retrieved_at: "2026-10-24T07:48:16+00:00"
  - type: "pm_response"
    notes: "Polymarket assigns only 6% to the trilateral summit, pricing Zelensky's Abu Dhabi proposal as a diplomatic opening rather than a confirmed outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "english.news.cn: Daily World Briefing, Oct. 24-Xinhua"
    url: "https://english.news.cn/20261024/e0b2fbf7f7324349973c6eb1bc463150/c.html"
    published_at: "2026-10-24T00:00:00.000Z"
    retrieved_at: "2026-10-24T07:48:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
