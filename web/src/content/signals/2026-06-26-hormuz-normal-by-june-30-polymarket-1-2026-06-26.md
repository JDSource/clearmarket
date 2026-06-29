---
signal_id: "CMSIG2026062601"
signal_slug: "hormuz-normal-by-june-30-polymarket-1-2026-06-26"
headline: "Hormuz normal by June 30: Polymarket 1%"
semantic_title: "Hormuz normal traffic by June 30 near-fully priced out"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T20:45:05.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Will traffic through the Strait of Hormuz return to normal by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.009
  volume_24h_usd: 789141.1360469994
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices only 1% on Hormuz traffic returning to normal by June 30, resolving via portwatch.imf.org."
  - "US strikes on Iran following a cargo ship attack are consistent with the market's near-zero probability of June normalization."
  - "With Qatar-hosted Hormuz talks not scheduled until Tuesday and strikes ongoing, the two-day window makes resolution nearly impossible."
  - "A companion Kalshi contract asks whether the US will invade Iran before 2027; Polymarket prices that at 14%, signaling markets see prolonged tension but not full invasion."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US military struck Iranian targets after Iran attacked a cargo ship in the Strait of Hormuz, reigniting conflict along the critical oil shipping lane."
    publisher: "bbc.co.uk"
    published_at: "2026-06-26T20:45:05.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/ckg590wqxwpo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/ckg590wqxwpo"
        retrieved_at: "2026-06-29T01:46:24+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via IMF PortWatch data; current 1% pricing reflects active conflict conditions with no plausible June 30 reopening path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: US strikes Iran after attack on cargo ship - BBC News"
    url: "https://www.bbc.co.uk/news/articles/ckg590wqxwpo"
    published_at: "2026-06-26T20:45:05.000Z"
    retrieved_at: "2026-06-29T01:46:24+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
