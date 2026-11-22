---
signal_id: "CMSIG2026111906"
signal_slug: "ukraine-cedes-territory-by-2026-polymarket-2-2026-11-19"
headline: "Ukraine cedes territory by 2026: Polymarket 2%"
semantic_title: "Ukraine ceding territory to Russia by year-end stays near zero"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-19T17:13:23.000Z"
event_id: "CM-EVT-XP7FFT2MC9"
event_slug: "will-ukraine-agree-to-cede-territory-to-russia-before-2027"
event_question: "Will Ukraine agree to cede territory to Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21bf9a7dae81b6bd51acae73185686ab8997b81b1401e4be10e114d472599c26"
  question_raw: "Will Ukraine agree to cede territory to Russia before 2027?"
  current_price: 0.023
  volume_24h_usd: 442.5436
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 2% chance Ukraine agrees to cede territory to Russia by end of 2026."
  - "The trilateral summit produced a declaration that explicitly omitted Ukraine, consistent with markets pricing out a rapid territorial settlement."
  - "Ukraine's allies warned the 'Yalta format' talks would not bring peace, and the Polymarket contract on Trump, Putin, and Zelensky meeting together sits at just 5%."
  - "Resolves via UMA oracle; a ceasefire contract (5% on Polymarket via Story 28) implies modest but slightly higher odds of a freeze versus a formal territorial transfer."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump, Putin, and Xi wrapped historic trilateral talks in China and agreed a peace declaration that made no mention of the Ukraine or Iran wars."
    publisher: "Rebecca Bailey"
    published_at: "2026-11-19T17:13:23.000Z"
    source_url: "https://www.theguardian.com/world/2026/nov/19/china-russia-us-agree-peace-statement-no-mention-ukraine-iran-wars"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rebecca Bailey"
        source_url: "https://www.theguardian.com/world/2026/nov/19/china-russia-us-agree-peace-statement-no-mention-ukraine-iran-wars"
        retrieved_at: "2026-11-22T07:47:40+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; 2% on territorial cession versus 5% on a ceasefire reveals the market's hierarchy of peace-scenario probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rebecca Bailey: China, Russia and US agree peace declaration with no mention of Ukrain"
    url: "https://www.theguardian.com/world/2026/nov/19/china-russia-us-agree-peace-statement-no-mention-ukraine-iran-wars"
    published_at: "2026-11-19T17:13:23.000Z"
    retrieved_at: "2026-11-22T07:47:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
