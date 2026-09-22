---
signal_id: "CMSIG2026092206"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-19-2026-09-22"
headline: "Hormuz traffic normal by Dec 31: Polymarket 19%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 19%"
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
  current_price: 0.19
  volume_24h_usd: 32920.324821
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market puts just 19% odds on Strait of Hormuz traffic returning to normal by December 31."
  - "G7 condemnation of Houthi strikes and ongoing Iran war diplomacy at the UN show active pressure for resolution, but Polymarket prices this as a long shot rather than an imminent outcome."
  - "The market at 19% implies the disruption is expected to persist well into year-end despite diplomatic activity, consistent with Iran's foreign minister declaring a continued state of war."
  - "Resolves via Polymarket's uma_oracle based on documented evidence of normalized commercial shipping through the strait."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "G7 nations condemned Houthi strikes on Saudi Arabia as diplomatic pressure to restore Strait of Hormuz shipping intensified at the UN."
    publisher: "france24.com"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.france24.com/en/live-news/20260922-g7-leaders-condemn-houthi-strikes-on-saudi-arabia"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/live-news/20260922-g7-leaders-condemn-houthi-strikes-on-saudi-arabia"
        retrieved_at: "2026-09-22T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket at 19% reflects deep skepticism that regional diplomacy at the UN will translate into restored Hormuz shipping before year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: G7 leaders condemn Houthi strikes on Saudi Arabia"
    url: "https://www.france24.com/en/live-news/20260922-g7-leaders-condemn-houthi-strikes-on-saudi-arabia"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-22T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
