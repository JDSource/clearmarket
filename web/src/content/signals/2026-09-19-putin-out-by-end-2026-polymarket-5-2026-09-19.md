---
signal_id: "CMSIG2026091904"
signal_slug: "putin-out-by-end-2026-polymarket-5-2026-09-19"
headline: "Putin out by end-2026: Polymarket 5%"
semantic_title: "Putin leaving power by year-end stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-19T00:00:00.000Z"
event_id: "CM-EVT-5WJSMVBVS7"
event_slug: "putin-out-before-2027"
event_question: "Will Vladimir Putin no longer be President of Russia by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6bd56627aa21311850825edb27e53434a0e17a4f782be0086bc07f71eee00d0d"
  question_raw: "Putin out as President of Russia by December 31, 2026?"
  current_price: 0.05
  volume_24h_usd: 22861.064985000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T18:30:00Z"
bullets:
  - "Polymarket puts only 5% odds on Vladimir Putin no longer serving as President of Russia by end of 2026."
  - "The Russia sanctions bill becoming law represents a significant escalation of Western pressure, yet the market treats it as insufficient to threaten Putin's grip on power."
  - "A companion Polymarket contract on a Russia-Ukraine peace deal by 2026 sits at 6%, suggesting markets see the sanctions as prolonging conflict rather than forcing a resolution."
  - "Resolution via uma_oracle; the contract would resolve YES only on confirmed departure from the presidency, a bar the market sees as highly unlikely regardless of sanctions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump signed legislation authorizing sweeping new sanctions against Russia, designed to pressure Moscow over its ongoing war in Ukraine."
    publisher: "afp.com"
    published_at: "2026-09-19T00:00:00.000Z"
    source_url: "https://www.afp.com/en/trump-signs-bill-authorizing-sweeping-russia-sanctions"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "afp.com"
        source_url: "https://www.afp.com/en/trump-signs-bill-authorizing-sweeping-russia-sanctions"
        retrieved_at: "2026-09-19T12:14:43+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle; at 5%, the contract prices the sanctions law as a non-event for Putin's political survival."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "afp.com: Trump signs bill authorizing sweeping Russia sanctions | AFP.com"
    url: "https://www.afp.com/en/trump-signs-bill-authorizing-sweeping-russia-sanctions"
    published_at: "2026-09-19T00:00:00.000Z"
    retrieved_at: "2026-09-19T12:14:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
