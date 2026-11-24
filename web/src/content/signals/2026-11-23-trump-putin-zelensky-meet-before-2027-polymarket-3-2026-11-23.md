---
signal_id: "CMSIG2026112305"
signal_slug: "trump-putin-zelensky-meet-before-2027-polymarket-3-2026-11-23"
headline: "Trump, Putin, Zelensky meet before 2027: Polymarket 3%"
semantic_title: "Trump-Putin-Zelensky joint meeting remains a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T06:53:00.000Z"
event_id: "CM-EVT-FNBRJ6KY59"
event_slug: "trump-putin-and-zelensky-meet-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky meet together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe96fd18679de58fa286f10b49d93f46829243cd105d74ce5d18eae0dd973b204"
  question_raw: "Trump, Putin, and Zelensky meet together before 2027?"
  current_price: 0.032
  volume_24h_usd: 51.54
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices only 3% on Trump, Putin, and Zelensky meeting together before 2027, resolving via UMA oracle."
  - "Despite the intelligence chief's framing of Trump-Putin ties as appropriate, markets assign near-zero odds to a trilateral summit, treating the diplomatic warmth as far short of a breakthrough."
  - "The companion Polymarket contract on the three leaders being seen together (CM-EVT-QP1YL1BSS0) prices 5%, a small premium over the stricter meeting definition, reflecting modest optionality on informal or photo-op contact."
  - "Resolves via UMA oracle on documented evidence of a joint Trump-Putin-Zelensky meeting; informal sideline contact or separate bilateral meetings would not satisfy resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US intelligence chief endorsed Trump describing Vladimir Putin as a friend, underscoring the administration's unusual warmth toward Moscow."
    publisher: "Bridget Brown"
    published_at: "2026-11-23T06:53:00.000Z"
    source_url: "https://apnews.com/live/donald-trump-politics-news-updates-11-23-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bridget Brown"
        source_url: "https://apnews.com/live/donald-trump-politics-news-updates-11-23-2026"
        retrieved_at: "2026-11-24T07:47:50+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 2-percentage-point gap between being seen together (5%) and an actual meeting (3%) is the market's estimate of informal contact probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bridget Brown: Live updates: Trump’s calling Putin a ‘friend’ is ‘entirely appropriat"
    url: "https://apnews.com/live/donald-trump-politics-news-updates-11-23-2026"
    published_at: "2026-11-23T06:53:00.000Z"
    retrieved_at: "2026-11-24T07:47:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
