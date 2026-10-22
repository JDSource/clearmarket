---
signal_id: "CMSIG2026102206"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-22"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Hormuz traffic return to normal by year-end stays a long shot"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 17925.777383
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prediction market prices only 12% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Seven tankers damaged in a single overnight period directly supports the market's heavy discounting of a near-term normalization."
  - "Treasury yields fell and oil-linked risk assets moved Thursday partly on Hormuz escalation, the 12% contract price reflects that geopolitical premium."
  - "Polymarket resolves via uma_oracle; with roughly 10 weeks to year-end and no ceasefire signal, the low probability appears consistent with ground conditions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's state television reported seven oil tankers were struck or hit mines in the Strait of Hormuz overnight, possibly the largest single-day incident count since the Iran war."
    publisher: "The Associated Press"
    published_at: "2026-10-22T00:00:00.000Z"
    source_url: "https://apnews.com/article/mideast-yemen-saudi-israel-october-22-2026-dde5b98a8bf961224514994b02babce9"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://apnews.com/article/mideast-yemen-saudi-israel-october-22-2026-dde5b98a8bf961224514994b02babce9"
        retrieved_at: "2026-10-22T13:24:33+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; the 12% price implies markets see Hormuz disruption as likely to persist through 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: Iran says 7 tankers were damaged in the Strait of Hormuz, and other Mi"
    url: "https://apnews.com/article/mideast-yemen-saudi-israel-october-22-2026-dde5b98a8bf961224514994b02babce9"
    published_at: "2026-10-22T00:00:00.000Z"
    retrieved_at: "2026-10-22T13:24:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
