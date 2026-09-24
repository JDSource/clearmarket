---
signal_id: "CMSIG2026092408"
signal_slug: "trump-putin-zelensky-joint-appearance-polymarket-9-2026-09-24"
headline: "Trump-Putin-Zelensky joint appearance: Polymarket 9%"
semantic_title: "Trump, Putin, and Zelensky seen together before 2027 stays a long shot"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-24T00:00:00.000Z"
event_id: "CM-EVT-QP1YL1BSS0"
event_slug: "trump-putin-and-zelensky-seen-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky be seen together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa04dcb7b7f5a313d09e7728ca39835be4096da877ca5fbae5e3a36af239433c3"
  question_raw: "Trump, Putin, and Zelensky seen together before 2027?"
  current_price: 0.09
  volume_24h_usd: 113.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Trump, Putin, and Zelensky being seen together before 2027 prices at 9%."
  - "Ongoing Russian strikes and Zelensky's public pressure campaign are consistent with a low-probability reading on any three-way summit materializing this year."
  - "Companion Polymarket contract on Putin no longer being President of Russia by end of 2026 sits at 4%, suggesting the market sees the current conflict dynamic as stable if grim."
  - "Resolves via Polymarket's UMA oracle, requiring documented evidence of all three leaders appearing together before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia launched deadly missile and drone attacks across Ukraine, killing at least eight civilians, while Ukrainian President Volodymyr Zelensky called for increased international pressure on President Vladimir Putin."
    publisher: "RFE/RL's Ukrainian Service"
    published_at: "2026-09-24T00:00:00.000Z"
    source_url: "https://www.rferl.org/a/ukraine-russia-attacks-diplomacy-un-sanctions/33863366.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "RFE/RL's Ukrainian Service"
        source_url: "https://www.rferl.org/a/ukraine-russia-attacks-diplomacy-un-sanctions/33863366.html"
        retrieved_at: "2026-09-24T13:07:56+00:00"
  - type: "pm_response"
    notes: "Polymarket's 9% three-way summit contract and 4% Putin-exit contract together frame the market's view: no near-term peace breakthrough and no leadership change expected."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "RFE/RL's Ukrainian Service: Russia Launches Deadly Attacks On Ukraine; Zelenskyy Calls For Pressur"
    url: "https://www.rferl.org/a/ukraine-russia-attacks-diplomacy-un-sanctions/33863366.html"
    published_at: "2026-09-24T00:00:00.000Z"
    retrieved_at: "2026-09-24T13:07:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
