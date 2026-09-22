---
signal_id: "CMSIG2026092205"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-23-2026-09-22"
headline: "Hormuz traffic normal by Dec 31: Polymarket 23%"
semantic_title: "Hormuz traffic returning to normal by year-end stays below 25%"
telemetry: "Polymarket 23%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-22T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.23
  volume_24h_usd: 197210.6180530001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at 23%, keeping it a long shot."
  - "G7 condemnation of Houthi strikes and ongoing Saudi-Houthi exchanges are consistent with the market's skeptical read on a near-term normalization."
  - "Iran's separate offer to reopen Hormuz within seven days if the US eases pressure is a partial upside catalyst but is not yet reflected in a repricing above 23%."
  - "Resolution via uma oracle on Polymarket; the contract's year-end horizon means any diplomatic breakthrough at UNGA this week would be the clearest near-term test."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "G7 nations condemned Houthi strikes on Saudi Arabia as Houthi-Saudi exchanges intensify, adding pressure to an already disrupted Middle East shipping corridor."
    publisher: "france24.com"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.france24.com/en/live-news/20260922-g7-leaders-condemn-houthi-strikes-on-saudi-arabia"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/live-news/20260922-g7-leaders-condemn-houthi-strikes-on-saudi-arabia"
        retrieved_at: "2026-09-22T13:03:08+00:00"
  - type: "pm_response"
    notes: "Polymarket at 23% on Hormuz normalization by year-end reflects persistent skepticism despite Iran's conditional reopening offer reported the same day."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: G7 leaders condemn Houthi strikes on Saudi Arabia"
    url: "https://www.france24.com/en/live-news/20260922-g7-leaders-condemn-houthi-strikes-on-saudi-arabia"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-22T13:03:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
