---
signal_id: "CMSIG2026082306"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-33-2026-08-23"
headline: "Hormuz traffic normal by Dec 31: Polymarket 33%"
semantic_title: "Strait of Hormuz return to normal by year-end holds near 33 percent"
telemetry: "Polymarket 33%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-23T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.33
  volume_24h_usd: 90906.823548
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 33% on Strait of Hormuz traffic returning to normal by December 31, resolves via UMA oracle."
  - "Iran's 'act of war' warning over new sanctions is consistent with the sub-50% pricing; markets are not expecting a near-term resolution."
  - "Pakistan's army chief traveling to Tehran as mediator introduces a non-zero diplomatic path, but the 33% price shows the market assigns it limited weight."
  - "The Kalshi contract on the US reopening its embassy in Iran (CM-EVT-34SYT4T2T1) sits at just 5%, signaling the market sees no imminent normalization on any front."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's new security chief warned that support for new U.S. sanctions would be treated as an act of war, deepening the diplomatic impasse."
    publisher: "apnews.com"
    published_at: "2026-08-23T00:00:00.000Z"
    source_url: "https://apnews.com/article/middle-east-iran-israel-west-bank-august-23-2026-a3fff9eba47a5510060e8014b82d794f"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/middle-east-iran-israel-west-bank-august-23-2026-a3fff9eba47a5510060e8014b82d794f"
        retrieved_at: "2026-08-24T08:42:17+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on whether commercial shipping volumes through the Strait of Hormuz return to pre-disruption norms by December 31."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Iran’s president says US memorandum is best path out of stalled war |"
    url: "https://apnews.com/article/middle-east-iran-israel-west-bank-august-23-2026-a3fff9eba47a5510060e8014b82d794f"
    published_at: "2026-08-23T00:00:00.000Z"
    retrieved_at: "2026-08-24T08:42:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
