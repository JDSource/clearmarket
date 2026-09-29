---
signal_id: "CMSIG2026092904"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-21-2026-09-29"
headline: "Hormuz traffic normal by Dec 31: Polymarket 21%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-29T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.21
  volume_24h_usd: 118094.192405
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at only 21%."
  - "Iran's signals of more serious talks and Qatari mediation activity are positive news, yet the Polymarket contract stays well below 50%, showing skepticism about near-term resolution."
  - "A separate Kalshi contract puts only 4% odds on the US reopening its embassy in Iran, underlining how far markets are from pricing a full normalization."
  - "Resolves via Polymarket's UMA oracle based on documented evidence of normal Strait of Hormuz traffic by December 31, 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iranian Foreign Minister Abbas Araghchi says Qatari mediators will present the US with new ideas on Iran's conditions for reopening the Strait of Hormuz, with contacts described as more serious."
    publisher: "aa.com.tr"
    published_at: "2026-09-29T00:00:00.000Z"
    source_url: "https://www.aa.com.tr/en/middle-east/iran-says-qatar-to-present-us-with-new-ideas-aimed-at-reopening-strait-of-hormuz/4072093"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/middle-east/iran-says-qatar-to-present-us-with-new-ideas-aimed-at-reopening-strait-of-hormuz/4072093"
        retrieved_at: "2026-09-29T14:34:30+00:00"
  - type: "pm_response"
    notes: "Polymarket contract on Strait of Hormuz normalization by December 31; current 21% price reflects persistent doubt despite active diplomatic signals."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: Iran says Qatar to present US with new ideas aimed at reopening Strait"
    url: "https://www.aa.com.tr/en/middle-east/iran-says-qatar-to-present-us-with-new-ideas-aimed-at-reopening-strait-of-hormuz/4072093"
    published_at: "2026-09-29T00:00:00.000Z"
    retrieved_at: "2026-09-29T14:34:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
