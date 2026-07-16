---
signal_id: "CMSIG2026071603"
signal_slug: "fed-hikes-benchmark-rate-in-2026-polymarket-51-2026-07-16"
headline: "Fed hikes benchmark rate in 2026: Polymarket 51%"
semantic_title: "Fed rate hike in 2026 consensus fractures near coin-flip"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T09:21:50.000Z"
event_id: "CM-EVT-87QV1G78C4"
event_slug: "fed-rate-hike-in-2026"
event_question: "Will the Federal Reserve raise its benchmark interest rate in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x80b3af88cb991980e8da1ce86b9794a0957f96ec98c29319dd7ba65e9744d82b"
  question_raw: "Fed rate hike in 2026?"
  current_price: 0.51
  volume_24h_usd: 20444.483323
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "Polymarket prices a 51% chance the Federal Reserve raises its benchmark interest rate in 2026."
  - "Rising Treasury yields driven by geopolitical risk premium and oil price pressure are consistent with a market nearly split on Fed action."
  - "Kalshi separately prices only 8% on a cut greater than 25 basis points this year, reinforcing that dovish pivot odds are low."
  - "A separate Kalshi ladder prices the Fed funds upper bound firmly in the 3.50-3.75% range, anchoring the near-term policy path well below current market rates."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Treasury yields rose as oil prices climbed on mounting US-Iran tensions, with the 10-year yield moving above 4.57%."
    publisher: "Sarah Min,Joseph Wilkins"
    published_at: "2026-07-16T09:21:50.000Z"
    source_url: "https://www.cnbc.com/2026/07/16/us-treasury-yields-wall-street-inflation-employment-data.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sarah Min,Joseph Wilkins"
        source_url: "https://www.cnbc.com/2026/07/16/us-treasury-yields-wall-street-inflation-employment-data.html"
        retrieved_at: "2026-07-16T17:20:43+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; definition of 'raise' relative to current effective funds rate is the key settlement question."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sarah Min,Joseph Wilkins: Treasury yields rise, as oil resumes climb on mounting U.S.-Iran tensi"
    url: "https://www.cnbc.com/2026/07/16/us-treasury-yields-wall-street-inflation-employment-data.html"
    published_at: "2026-07-16T09:21:50.000Z"
    retrieved_at: "2026-07-16T17:20:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
