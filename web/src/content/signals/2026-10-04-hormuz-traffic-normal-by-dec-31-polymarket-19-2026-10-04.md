---
signal_id: "CMSIG2026100406"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-19-2026-10-04"
headline: "Hormuz traffic normal by Dec 31: Polymarket 19%"
semantic_title: "Hormuz traffic back to normal by year-end stays long shot"
telemetry: "Polymarket 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-04T08:22:07.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.19
  volume_24h_usd: 70638.4053
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 19% on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Iran's explicit conditionality statement is consistent with the market's skeptical pricing, resolution before year-end looks unlikely."
  - "With roughly three months remaining and no diplomatic framework visible, the 19% reflects tail-risk scenario odds only."
  - "Companion Kalshi contract CM-EVT-34SYT4T2T1 (US reopens embassy in Iran) sits at 4%, suggesting the market sees full normalization as even more remote."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran declared the Strait of Hormuz will not reopen until its conditions are met, as Trump signaled decisions on Iran are imminent."
    publisher: "The National"
    published_at: "2026-10-04T08:22:07.000Z"
    source_url: "https://www.thenationalnews.com/news/gulf/2026/10/04/iran-says-strait-of-hormuz-will-not-reopen-until-its-conditions-are-met/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The National"
        source_url: "https://www.thenationalnews.com/news/gulf/2026/10/04/iran-says-strait-of-hormuz-will-not-reopen-until-its-conditions-are-met/"
        retrieved_at: "2026-10-04T13:39:12+00:00"
  - type: "pm_response"
    notes: "Resolves via Polymarket UMA oracle; Iran's stated conditions create a high bar for the normal-traffic definition."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The National: Iran says Strait of Hormuz will not reopen until its conditions are me"
    url: "https://www.thenationalnews.com/news/gulf/2026/10/04/iran-says-strait-of-hormuz-will-not-reopen-until-its-conditions-are-met/"
    published_at: "2026-10-04T08:22:07.000Z"
    retrieved_at: "2026-10-04T13:39:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
