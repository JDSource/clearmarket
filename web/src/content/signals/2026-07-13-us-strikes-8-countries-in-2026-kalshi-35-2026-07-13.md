---
signal_id: "CMSIG2026071303"
signal_slug: "us-strikes-8-countries-in-2026-kalshi-35-2026-07-13"
headline: "US strikes 8 countries in 2026: Kalshi 35%"
semantic_title: "US strikes 8-plus countries in 2026 prices below the threshold"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-13T00:00:00.000Z"
event_id: "CM-EVT-5855JBL478"
event_slug: "how-many-different-countries-will-the-us-strike-in-2026"
event_question: "market-implied level"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x713ab27f31c1d8080ea3b9c21c8a021609f8fcb7aad13a87b8b069265e7fdfda"
  question_raw: "Will the US strike 8 countries in 2026?"
  current_price: 0.352
  volume_24h_usd: 117.31988199999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Kalshi ladder puts only 35% on the US striking 8 or more countries in 2026, with probability falling sharply above that level."
  - "Iran attacking Gulf states including Oman raises the count of nations drawn into the conflict, but the market still prices 8-country US strike threshold as unlikely."
  - "The distribution drops to 31% at 9 countries and 13% at 10, showing the market sees current escalation as bounded, not a regional cascade."
  - "Resolves via Kalshi's named resolution source; the strike count methodology and what qualifies as a distinct country engagement will be the key settlement edge."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran expanded attacks on Gulf states after US strikes and declared the Strait of Hormuz closed, with Iran targeting Bahrain, Kuwait, Jordan, and Oman."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-07-13T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/international/world-news/iran-expands-attacks-on-gulf-states-after-us-strikes-says-strait-of-hormuz-closed/articleshow/132354201.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/news/international/world-news/iran-expands-attacks-on-gulf-states-after-us-strikes-says-strait-of-hormuz-closed/articleshow/132354201.cms"
        retrieved_at: "2026-07-13T10:56:18+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder at 35% on 8 countries in 2026 signals markets are absorbing the Gulf escalation without pricing a broad multi-country US strike campaign."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: Iran expands attacks on Gulf states after US strikes, says Strait of H"
    url: "https://economictimes.indiatimes.com/news/international/world-news/iran-expands-attacks-on-gulf-states-after-us-strikes-says-strait-of-hormuz-closed/articleshow/132354201.cms"
    published_at: "2026-07-13T00:00:00.000Z"
    retrieved_at: "2026-07-13T10:56:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
