---
signal_id: "CMSIG2026080405"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-58-2026-08-04"
headline: "Hormuz traffic normal by Dec 31: Polymarket 58%"
semantic_title: "Hormuz traffic back to normal by year-end near 50-50"
telemetry: "Polymarket 58%"
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
  current_price: 0.58
  volume_24h_usd: 121478.43618799999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices a 58% chance that Strait of Hormuz traffic returns to normal by December 31, 2026."
  - "Reported progress on an Iran-Oman deal is broadly consistent with the above-50% pricing, but the market's near-coin-flip read signals substantial remaining doubt about final execution."
  - "Iran's simultaneous threats of a Gulf 'blackout' over U.S. strikes (Story 28) and Trump's claim the strait is only 'sort of open' (Story 23) explain why the contract has not moved decisively higher."
  - "A companion prediction market ladder (CM-EVT-JR1WTQ5JH0) implies current weekly transit calls in the 50-60 range, well below pre-conflict norms, underscoring why the year-end resolution question remains genuinely open."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran and Oman made progress toward a deal to reopen the Strait of Hormuz, with officials describing negotiations as advancing."
    publisher: "apnews.com"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://apnews.com/article/iran-us-war-strait-hormuz-oman-diplomacy-6587f90f2ab5beec373ce5fabf637541"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-us-war-strait-hormuz-oman-diplomacy-6587f90f2ab5beec373ce5fabf637541"
        retrieved_at: "2026-08-07T08:53:43+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle based on Strait of Hormuz commercial shipping data by December 31, 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Officials report progress on a deal to reopen the Strait of Hormuz | A"
    url: "https://apnews.com/article/iran-us-war-strait-hormuz-oman-diplomacy-6587f90f2ab5beec373ce5fabf637541"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-07T08:53:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
