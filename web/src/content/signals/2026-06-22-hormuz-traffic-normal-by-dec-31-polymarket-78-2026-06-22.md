---
signal_id: "CMSIG2026062208"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-78-2026-06-22"
headline: "Hormuz traffic normal by Dec 31: Polymarket 78%"
semantic_title: "Hormuz year-end normalization holds wide market consensus"
telemetry: "Polymarket 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-22T09:12:59.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.78
  volume_24h_usd: 289674.7514719999
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at 78%, the dominant consensus across all three Hormuz deadlines."
  - "Progress in US-Iran talks supports the year-end contract; the 60-day deal roadmap agreed in Switzerland points to an August resolution timeframe."
  - "The June 30 near-term contract at 18% and the July 31 contract at 47% confirm the market sees a drawn-out rather than sudden reopening."
  - "Resolves via portwatch.imf.org shipping traffic data; normalization is measured against historical throughput benchmarks, not a political declaration."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US jobs report showed rising rate hike expectations alongside uneven job growth, and a separate story reported progress toward a deal to reopen the Strait of Hormuz."
    publisher: "mattandnancy.org"
    published_at: "2026-06-22T09:12:59.000Z"
    source_url: "https://mattandnancy.org/article/us-jobs-report-rate-hike-chances-rise-but-uneven-job-growth-persists"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "mattandnancy.org"
        source_url: "https://mattandnancy.org/article/us-jobs-report-rate-hike-chances-rise-but-uneven-job-growth-persists"
        retrieved_at: "2026-06-22T13:32:28+00:00"
  - type: "pm_response"
    notes: "Polymarket's 78% on December 31 reopening reflects a durable consensus that diplomacy will eventually succeed, even as near-term deadlines remain low-probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "mattandnancy.org: US Jobs Report: Rate Hike Chances Rise, But Uneven Job Growth Persists"
    url: "https://mattandnancy.org/article/us-jobs-report-rate-hike-chances-rise-but-uneven-job-growth-persists"
    published_at: "2026-06-22T09:12:59.000Z"
    retrieved_at: "2026-06-22T13:32:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
