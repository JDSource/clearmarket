---
signal_id: "CMSIG2026080404"
signal_slug: "hormuz-back-to-normal-by-dec-31-polymarket-61-2026-08-04"
headline: "Hormuz back to normal by Dec 31: Polymarket 61%"
semantic_title: "Hormuz traffic returning to normal by year-end stays below even"
telemetry: "Polymarket 61%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.61
  volume_24h_usd: 79313.408312
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 61% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Iran-Oman progress reports and Rubio's positive characterization align directionally with the above-50% probability, but the market stops well short of high confidence."
  - "Trump's simultaneous 'last chance' warning to Iran and a cargo ship attack reported in Story 21 illustrate the fragility of negotiations, keeping the market from pricing a deal as near-certain."
  - "Kalshi prices only 5% on the U.S. reopening its embassy in Iran (CM-EVT-34SYT4T2T1), indicating the market sees a narrow shipping deal as far more plausible than broader normalization."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran and Oman reported progress toward a deal to reopen the Strait of Hormuz, with U.S. Secretary of State Marco Rubio calling talks positive."
    publisher: "apnews.com"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://apnews.com/article/iran-us-war-strait-hormuz-oman-diplomacy-6587f90f2ab5beec373ce5fabf637541"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-us-war-strait-hormuz-oman-diplomacy-6587f90f2ab5beec373ce5fabf637541"
        retrieved_at: "2026-08-06T10:35:15+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; the 61% price reflects diplomatic progress tempered by ongoing conflict risk and Trump's public pressure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Officials report progress on a deal to reopen the Strait of Hormuz | A"
    url: "https://apnews.com/article/iran-us-war-strait-hormuz-oman-diplomacy-6587f90f2ab5beec373ce5fabf637541"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-06T10:35:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
