---
signal_id: "CMSIG2026111904"
signal_slug: "trump-putin-zelensky-together-by-2027-polymarket-4-2026-11-19"
headline: "Trump, Putin, Zelensky together by 2027: Polymarket 4%"
semantic_title: "Trump-Putin-Zelensky meeting before 2027 stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-19T01:00:19.000Z"
event_id: "CM-EVT-QP1YL1BSS0"
event_slug: "trump-putin-and-zelensky-seen-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky be seen together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa04dcb7b7f5a313d09e7728ca39835be4096da877ca5fbae5e3a36af239433c3"
  question_raw: "Trump, Putin, and Zelensky seen together before 2027?"
  current_price: 0.042
  volume_24h_usd: 310.812387
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Trump, Putin, and Zelensky being seen together before 2027 sits at 4%, a heavy long-shot read."
  - "The Shenzhen trilateral confirms Trump-Putin face time is now real, but Ukrainian President Volodymyr Zelensky's absence keeps the three-way contract far from pricing in."
  - "The parallel Polymarket contract asking the same question (CM-EVT-FNBRJ6KY59) also prices at 4%, showing no cross-venue gap."
  - "Resolves via UMA oracle; the question specifically requires all three leaders to be seen together, not just Trump and Putin bilaterally."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Trump met with China's Xi Jinping and Russia's Vladimir Putin in a historic trilateral at the APEC summit in Shenzhen, with nuclear arms and the Ukraine war topping the agenda."
    publisher: "Josh Boak, Michelle L. Price and E. Eduardo Castillo"
    published_at: "2026-11-19T01:00:19.000Z"
    source_url: "https://apnews.com/article/trump-xi-putin-nuclear-ukraine-iran-a04dc76ed8e786b087e2c1ea9598783a"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Josh Boak, Michelle L. Price and E. Eduardo Castillo"
        source_url: "https://apnews.com/article/trump-xi-putin-nuclear-ukraine-iran-a04dc76ed8e786b087e2c1ea9598783a"
        retrieved_at: "2026-11-19T07:47:42+00:00"
  - type: "pm_response"
    notes: "Polymarket prices the Trump-Putin-Zelensky trilateral at 4% despite the confirmed Trump-Putin bilateral at APEC; Zelensky's absence is the key gap."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Josh Boak, Michelle L. Price and E. Eduardo Castillo: Nuclear arms and ending wars in Iran and Ukraine will top the agenda a"
    url: "https://apnews.com/article/trump-xi-putin-nuclear-ukraine-iran-a04dc76ed8e786b087e2c1ea9598783a"
    published_at: "2026-11-19T01:00:19.000Z"
    retrieved_at: "2026-11-19T07:47:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
