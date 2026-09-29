---
signal_id: "CMSIG2026092906"
signal_slug: "hormuz-back-to-normal-by-dec-31-polymarket-21-2026-09-29"
headline: "Hormuz back to normal by Dec 31: Polymarket 21%"
semantic_title: "Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-29T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.21
  volume_24h_usd: 128944.96464500001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 21% that Strait of Hormuz traffic returns to normal by December 31, putting long odds against a near-term resolution despite active mediation."
  - "Iran's description of contacts as 'more serious' and Qatar's mediator role are real diplomatic developments, but the prediction market is not pricing a breakthrough."
  - "A separate Kalshi contract puts just 4% on the US reopening its embassy in Iran, signaling prediction markets see broader normalization as a long-horizon tail event."
  - "Resolves via Polymarket UMA oracle based on observable shipping and traffic data; the December 31 deadline compresses the window for a deal to materialize."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran says Qatar will present the US with new ideas to reopen the Strait of Hormuz, with Iranian foreign minister describing contacts as more serious following Tehran's latest proposal."
    publisher: "aa.com.tr"
    published_at: "2026-09-29T00:00:00.000Z"
    source_url: "https://www.aa.com.tr/en/middle-east/iran-says-qatar-to-present-us-with-new-ideas-aimed-at-reopening-strait-of-hormuz/4072093"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/middle-east/iran-says-qatar-to-present-us-with-new-ideas-aimed-at-reopening-strait-of-hormuz/4072093"
        retrieved_at: "2026-09-29T07:47:25+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 21% via UMA oracle resolution; Kalshi US embassy in Iran contract at 4% provides a correlated normalization-track cross-check."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: Iran says Qatar to present US with new ideas aimed at reopening Strait"
    url: "https://www.aa.com.tr/en/middle-east/iran-says-qatar-to-present-us-with-new-ideas-aimed-at-reopening-strait-of-hormuz/4072093"
    published_at: "2026-09-29T00:00:00.000Z"
    retrieved_at: "2026-09-29T07:47:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
