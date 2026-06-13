---
signal_id: "CMSIG2026061106"
signal_slug: "us-negative-gdp-in-2026-polymarket-10-2026-06-11"
headline: "US negative GDP in 2026: Polymarket 10%"
semantic_title: "US negative GDP growth in 2026 priced at low conviction level"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-11T12:30:32.000Z"
event_id: "CM-EVT-36YHF72CQ8"
event_slug: "negative-gdp-growth-in-2026"
event_question: "Will the United States experience negative GDP growth in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd8c1b0a73653b1fb4fb6e8d13d0063d25810870d7ddf83e61fffb4de4522edf1"
  question_raw: "Negative GDP growth in 2026?"
  current_price: 0.1
  arbitration_model: "uma_oracle"
  resolution_source: "bea.gov"
  resolves_at: "2027-01-29T00:00:00Z"
bullets:
  - "Polymarket prices US negative GDP growth in 2026 at just 10%, a low-conviction recession signal despite softening spending data."
  - "The soft spending figures are consistent with slowdown risk, but the market is not pricing a recession as a central scenario."
  - "Labor market resilience, jobless claims at historically low 229,000, is likely anchoring the low recession probability."
  - "Resolves via BEA GDP data at bea.gov; requires at least one calendar year 2026 GDP print to be negative."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Fed's Beige Book showed inflation-adjusted food and services spending fell 1.3% in May, raising recession questions."
    publisher: "Rich Duprey"
    published_at: "2026-06-11T12:30:32.000Z"
    source_url: "https://247wallst.com/investing/2026/06/11/the-fed-just-quietly-released-surprisingly-bad-economic-news-is-a-recession-already-starting/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rich Duprey"
        source_url: "https://247wallst.com/investing/2026/06/11/the-fed-just-quietly-released-surprisingly-bad-economic-news-is-a-recession-already-starting/"
        retrieved_at: "2026-06-13T10:25:37+00:00"
  - type: "pm_response"
    notes: "Polymarket's 10% recession probability sits well below the alarm threshold despite fresh softness in consumption data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rich Duprey: The Fed Just Quietly Released Surprisingly Bad Economic News. Is a Rec"
    url: "https://247wallst.com/investing/2026/06/11/the-fed-just-quietly-released-surprisingly-bad-economic-news-is-a-recession-already-starting/"
    published_at: "2026-06-11T12:30:32.000Z"
    retrieved_at: "2026-06-13T10:25:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
