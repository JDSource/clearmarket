---
signal_id: "CMSIG2026092807"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-7-2026-09-28"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 7%"
semantic_title: "Ukraine peace deal with Russia before 2027 stays a long shot"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.07
  volume_24h_usd: 4922.395755
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Ukraine-Russia peace deal before 2027 at just 7%, a deeply pessimistic read despite ongoing diplomatic activity."
  - "Continued Russian bombardment killing civilians is consistent with the market's near-dismissal of a near-term deal."
  - "The separate Polymarket contract on Ukraine ceding territory by 2026 (CM-EVT-XP7FFT2MC9) sits at 6%, showing the market sees neither peace nor major concessions as likely."
  - "Resolves via uma_oracle; the definition of a signed peace deal versus a ceasefire is the key settlement ambiguity."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russian strikes killed at least seven people in Ukraine, including at Kyiv's National Academy of Sciences, amid continued bombardment."
    publisher: "cbsnews.com"
    published_at: "2026-09-28T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/russia-ukraine-war-kyiv-strikes-national-academy-sciences/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/russia-ukraine-war-kyiv-strikes-national-academy-sciences/"
        retrieved_at: "2026-09-28T16:24:04+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 7% on a Ukraine-Russia peace deal before 2027 resolves via uma_oracle; pricing consistent across correlated ceasefire and territory contracts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Russian strikes on Ukraine kill at least 7, including woman at Kyiv's"
    url: "https://www.cbsnews.com/news/russia-ukraine-war-kyiv-strikes-national-academy-sciences/"
    published_at: "2026-09-28T00:00:00.000Z"
    retrieved_at: "2026-09-28T16:24:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
