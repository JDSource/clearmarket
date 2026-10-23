---
signal_id: "CMSIG2026102102"
signal_slug: "oct-payrolls-implied-70k-80k-kalshi-ladder-2026-10-21"
headline: "Oct payrolls implied 70K-80K: Kalshi ladder"
semantic_title: "October nonfarm payrolls consensus clusters near 70-80K"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-21T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.4
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder implies October payrolls in the 70,000-80,000 range, with 51% above 70,000 but only 40% above 80,000."
  - "Claims at a 3-month low support the positive payrolls read; at 85% above zero, the market firmly rejects outright job losses."
  - "The sharp drop-off above 100,000 (30%) suggests the market does not expect a blowout print despite the low claims reading."
  - "Resolves via the Bureau of Labor Statistics Employment Situation release; benchmark revisions and seasonal factors could shift the outcome materially."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Initial jobless claims hit 194,000, a three-month low, reinforcing expectations of continued positive but moderate job growth."
    publisher: "investing.com"
    published_at: "2026-10-21T00:00:00.000Z"
    source_url: "https://www.investing.com/news/stock-market-news/initial-jobless-claims-highlight-thursdays-economic-calendar-93CH-4963797"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/news/stock-market-news/initial-jobless-claims-highlight-thursdays-economic-calendar-93CH-4963797"
        retrieved_at: "2026-10-23T13:03:13+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder concentrates probability between 60,000 and 90,000 jobs, broadly aligned with the tight claims data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Initial jobless claims highlight Thursday’s economic calendar By Inves"
    url: "https://www.investing.com/news/stock-market-news/initial-jobless-claims-highlight-thursdays-economic-calendar-93CH-4963797"
    published_at: "2026-10-21T00:00:00.000Z"
    retrieved_at: "2026-10-23T13:03:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
