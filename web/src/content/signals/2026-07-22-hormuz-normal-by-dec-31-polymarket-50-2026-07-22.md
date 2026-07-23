---
signal_id: "CMSIG2026072201"
signal_slug: "hormuz-normal-by-dec-31-polymarket-50-2026-07-22"
headline: "Hormuz normal by Dec 31: Polymarket 50%"
semantic_title: "Hormuz back to normal by year-end stays near 50%"
telemetry: "Polymarket 50%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.5
  volume_24h_usd: 93513.47425799999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts exactly 50% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Active US-Iran strikes and mutual threats to civilian infrastructure are consistent with maximum uncertainty, the market is essentially a coin flip on year-end resolution."
  - "The companion Polymarket contract on Hormuz normalization by July 31 sits at just 1%, confirming markets see no near-term off-ramp."
  - "Resolves via UMA oracle; 'normal traffic' definition and measurement methodology are the key settlement edges to watch."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US and Iranian forces exchanged strikes as both sides threatened civilian infrastructure, with the Strait of Hormuz remaining a focal point of the conflict."
    publisher: "apnews.com"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-22-2026-42ff3de8d135ad72ff3ba4d94cc0921d"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-22-2026-42ff3de8d135ad72ff3ba4d94cc0921d"
        retrieved_at: "2026-07-23T10:16:46+00:00"
  - type: "pm_response"
    notes: "Polymarket at 50% on December resolution, versus 1% on July 31, captures stark timeline divergence in the same waterway question."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: US and Iran attacks rage across Middle East | AP News"
    url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-22-2026-42ff3de8d135ad72ff3ba4d94cc0921d"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-23T10:16:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
