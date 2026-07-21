---
signal_id: "CMSIG2026072006"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-56-2026-07-20"
headline: "Hormuz traffic normal by Dec 31: Polymarket 56%"
semantic_title: "Hormuz traffic returning to normal by year-end holds near even odds"
telemetry: "Polymarket 56%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-20T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.56
  volume_24h_usd: 48705.607779
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 56% probability that Strait of Hormuz traffic returns to normal by December 31, 2026."
  - "Ten consecutive nights of US strikes and active IRGC tanker attacks have not pushed the contract below 50%; the market leans toward eventual resolution."
  - "The 56% reading implies the market is treating current escalation as a path toward negotiated reopening rather than permanent disruption, though conviction is limited."
  - "Resolves via Polymarket UMA oracle; 'normal' traffic must be verifiable; the Iran enrichment deal contract at 21% (Story 20) highlights the gap between tactical and diplomatic resolution odds."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US military bombed Iran for a tenth consecutive night in a renewed push to reopen the Strait of Hormuz after IRGC attacks on oil tankers."
    publisher: "theglobeandmail.com"
    published_at: "2026-07-20T00:00:00.000Z"
    source_url: "https://www.theglobeandmail.com/world/article-us-and-iran-trade-fire/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theglobeandmail.com"
        source_url: "https://www.theglobeandmail.com/world/article-us-and-iran-trade-fire/"
        retrieved_at: "2026-07-21T10:22:25+00:00"
  - type: "pm_response"
    notes: "Polymarket at 56% for Hormuz normalization; the contract sits near even odds despite ten nights of strikes, signaling deep uncertainty on the conflict timeline."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theglobeandmail.com: U.S. military bombs Iran for 10th consecutive night in renewed push to"
    url: "https://www.theglobeandmail.com/world/article-us-and-iran-trade-fire/"
    published_at: "2026-07-20T00:00:00.000Z"
    retrieved_at: "2026-07-21T10:22:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
