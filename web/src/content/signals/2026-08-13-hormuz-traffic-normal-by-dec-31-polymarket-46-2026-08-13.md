---
signal_id: "CMSIG2026081306"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-46-2026-08-13"
headline: "Hormuz traffic normal by Dec 31: Polymarket 46%"
semantic_title: "Hormuz traffic back to normal by year-end holds near 50%"
telemetry: "Polymarket 46%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-13T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.46
  volume_24h_usd: 74010.616951
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 46% on Strait of Hormuz traffic returning to normal by December 31, essentially a coin flip despite active military conflict."
  - "US-Iran competing control claims and the Houthi attack killing six in the Bab el-Mandeb Strait are consistent with a market that sees resolution as genuinely uncertain, not remote."
  - "Iran's demand for US war-damage payment before reopening (Story 24) is a concrete obstacle; the 46% pricing implies markets assign meaningful probability to a deal or de-facto normalization despite that demand."
  - "Resolves via UMA oracle; 'normal' traffic levels will need a defined benchmark, the settlement edge case is whether partial resumption qualifies."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US and Iran exchanged competing claims over Strait of Hormuz control as active military incidents continued in the waterway."
    publisher: "Alex Milan Durie,Ali Mustafa"
    published_at: "2026-08-13T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/liveblog/2026/8/13/iran-war-live-us-and-iran-exchange-opposing-claims-over-hormuz-control?traffic_source=rss"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alex Milan Durie,Ali Mustafa"
        source_url: "https://www.aljazeera.com/news/liveblog/2026/8/13/iran-war-live-us-and-iran-exchange-opposing-claims-over-hormuz-control?traffic_source=rss"
        retrieved_at: "2026-08-13T09:07:47+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 46%; paired with the 14% Iran enrichment-deal contract, the spread suggests the market sees Hormuz normalization as more achievable than a formal nuclear agreement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alex Milan Durie,Ali Mustafa: Iran war live: US, Tehran exchange opposing claims over Hormuz control"
    url: "https://www.aljazeera.com/news/liveblog/2026/8/13/iran-war-live-us-and-iran-exchange-opposing-claims-over-hormuz-control?traffic_source=rss"
    published_at: "2026-08-13T00:00:00.000Z"
    retrieved_at: "2026-08-13T09:07:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
