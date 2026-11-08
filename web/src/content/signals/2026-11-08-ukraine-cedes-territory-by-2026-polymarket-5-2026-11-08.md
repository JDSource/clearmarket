---
signal_id: "CMSIG2026110805"
signal_slug: "ukraine-cedes-territory-by-2026-polymarket-5-2026-11-08"
headline: "Ukraine cedes territory by 2026: Polymarket 5%"
semantic_title: "Ukraine territory cession by 2026 stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-08T12:58:58.000Z"
event_id: "CM-EVT-XP7FFT2MC9"
event_slug: "will-ukraine-agree-to-cede-territory-to-russia-before-2027"
event_question: "Will Ukraine agree to cede territory to Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21bf9a7dae81b6bd51acae73185686ab8997b81b1401e4be10e114d472599c26"
  question_raw: "Will Ukraine agree to cede territory to Russia before 2027?"
  current_price: 0.047
  volume_24h_usd: 212.10999999999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 5% on Ukraine agreeing to cede territory to Russia by 2026."
  - "Russia joining multi-party talks is diplomatically significant, but markets are not moving toward a concession scenario."
  - "Cross-read: Polymarket at 7% on a full peace deal by 2027 and 4% on a 2026 peace agreement show consistent long-shot odds across the peace spectrum."
  - "Polymarket resolves via uma_oracle; the low price implies markets require a formal cession agreement, not just talks, to settle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Reuters reports Russian diplomats and military officials will join talks with the U.S. and Ukraine next week, raising ceasefire speculation."
    publisher: "Reuters"
    published_at: "2026-11-08T12:58:58.000Z"
    source_url: "https://www.devdiscourse.com/article/international/4003504-reuters-world-news-summary"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://www.devdiscourse.com/article/international/4003504-reuters-world-news-summary"
        retrieved_at: "2026-11-08T14:44:20+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; the 5% price is consistent with companion contracts and reflects deep market skepticism about territorial concessions this year."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: Reuters World News Summary | International"
    url: "https://www.devdiscourse.com/article/international/4003504-reuters-world-news-summary"
    published_at: "2026-11-08T12:58:58.000Z"
    retrieved_at: "2026-11-08T14:44:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
