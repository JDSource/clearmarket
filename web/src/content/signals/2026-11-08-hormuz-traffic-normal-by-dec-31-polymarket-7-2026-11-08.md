---
signal_id: "CMSIG2026110806"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-7-2026-11-08"
headline: "Hormuz traffic normal by Dec 31: Polymarket 7%"
semantic_title: "Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-08T22:19:04.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.07
  volume_24h_usd: 110164.46631399999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices only a 7% chance Strait of Hormuz traffic returns to normal by December 31, 2026."
  - "Trump's diplomatic signaling is not moving the market meaningfully; the 7% read suggests traders see the timeline as too tight for a resolution."
  - "Qatar diplomacy and upcoming Abu Dhabi security talks add optionality, but the market is not pricing a near-term breakthrough."
  - "Resolution via UMA oracle; 'normal' Hormuz transit levels would need to be verifiably restored before year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump signaled openness to an Iran deal and said further strikes were unlikely if negotiations progressed, amid renewed Hormuz tensions."
    publisher: "Iran International"
    published_at: "2026-11-08T22:19:04.000Z"
    source_url: "https://www.iranintl.com/en/202611086475"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Iran International"
        source_url: "https://www.iranintl.com/en/202611086475"
        retrieved_at: "2026-11-09T07:47:40+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; the market is pricing deep skepticism that diplomacy closes fast enough for a 2026 Hormuz normalization."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Iran International: Trump signals openness to Iran deal amid renewed Hormuz tensions"
    url: "https://www.iranintl.com/en/202611086475"
    published_at: "2026-11-08T22:19:04.000Z"
    retrieved_at: "2026-11-09T07:47:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
