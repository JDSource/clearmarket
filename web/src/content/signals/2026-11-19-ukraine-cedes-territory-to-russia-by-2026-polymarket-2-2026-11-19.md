---
signal_id: "CMSIG2026111906"
signal_slug: "ukraine-cedes-territory-to-russia-by-2026-polymarket-2-2026-11-19"
headline: "Ukraine cedes territory to Russia by 2026: Polymarket 2%"
semantic_title: "Ukraine ceding territory to Russia by 2026 stays near zero"
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
  current_price: 0.025
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 2% on Ukraine agreeing to cede territory to Russia before the end of 2026."
  - "The summit declaration's silence on Ukraine is consistent with the market treating a formal territorial concession this year as near-impossible."
  - "A companion Polymarket contract (CM-EVT-S5MX1GCV08) prices 2% on Ukraine agreeing not to join NATO before 2027, showing both concession tracks are equally discounted."
  - "Resolves via UMA oracle; requires a verifiable Ukrainian agreement to transfer territory, a substantially higher bar than a trilateral communique."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Trump-Xi-Putin peace declaration at the APEC-adjacent trilateral summit omitted any mention of Ukraine or Iran conflicts, leaving no concrete territorial resolution."
    publisher: "Rebecca Bailey"
    published_at: "2026-11-19T17:13:23.000Z"
    source_url: "https://www.theguardian.com/world/2026/nov/19/china-russia-us-agree-peace-statement-no-mention-ukraine-iran-wars"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rebecca Bailey"
        source_url: "https://www.theguardian.com/world/2026/nov/19/china-russia-us-agree-peace-statement-no-mention-ukraine-iran-wars"
        retrieved_at: "2026-11-20T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket holds at 2%; the market is not moved by summit optics absent any Ukraine peace framework."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rebecca Bailey: China, Russia and US agree peace declaration with no mention of Ukrain"
    url: "https://www.theguardian.com/world/2026/nov/19/china-russia-us-agree-peace-statement-no-mention-ukraine-iran-wars"
    published_at: "2026-11-19T17:13:23.000Z"
    retrieved_at: "2026-11-20T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
