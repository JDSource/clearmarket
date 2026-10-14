---
signal_id: "CMSIG2026101405"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-13-2026-10-14"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 13%"
semantic_title: "Hormuz traffic returning to normal by year-end stays near 13%"
telemetry: "Polymarket 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.13
  volume_24h_usd: 99114.485752
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices normalization of Strait of Hormuz traffic by December 31 at just 13%."
  - "Al Jazeera reports attacks are at their worst since the start of the US-Israel war on Iran, fully consistent with the market's heavy skepticism on a near-term reopening."
  - "A separate Kalshi contract puts only 2% on the US reopening its embassy in Iran, reinforcing the market's view that diplomatic normalization is far off."
  - "Resolves via uma_oracle; 'normal' traffic likely requires a sustained, verifiable return to pre-conflict transit volumes through the strait."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran has stepped up Strait of Hormuz surveillance, with attacks on shipping soaring and oil flows crashing again as part of the broader US-Israel conflict with Iran."
    publisher: "Priyanka Shankar"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/10/14/iran-steps-up-hormuz-surveillance-attacks-soar-oil-flows-crash-again"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Priyanka Shankar"
        source_url: "https://www.aljazeera.com/news/2026/10/14/iran-steps-up-hormuz-surveillance-attacks-soar-oil-flows-crash-again"
        retrieved_at: "2026-10-14T13:17:09+00:00"
  - type: "pm_response"
    notes: "Polymarket at 13% reflects escalating attack frequency and no visible diplomatic off-ramp reported in current news flow."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Priyanka Shankar: Iran steps up Hormuz surveillance: Attacks soar, oil flows crash again"
    url: "https://www.aljazeera.com/news/2026/10/14/iran-steps-up-hormuz-surveillance-attacks-soar-oil-flows-crash-again"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-14T13:17:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
