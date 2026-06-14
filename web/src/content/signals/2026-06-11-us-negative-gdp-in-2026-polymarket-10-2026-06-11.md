---
signal_id: "CMSIG2026061106"
signal_slug: "us-negative-gdp-in-2026-polymarket-10-2026-06-11"
headline: "US negative GDP in 2026: Polymarket 10%"
semantic_title: "US negative GDP growth in 2026 anchors at low-probability despite soft data"
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
  - "Polymarket prices US negative GDP growth in 2026 at just 10%, despite the May real spending contraction."
  - "The weak spending data is not consistent with a market that prices recession as a low-probability tail event."
  - "The US unemployment ladder implies a rate near 4.2-4.3%, with jobless claims historically low, offering the labor market as an offset to the soft spending signal."
  - "Resolution is via BEA full-year 2026 GDP data; a single quarter of negative growth does not necessarily satisfy the annual negative growth condition."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Fed released data showing inflation-adjusted food and services spending fell 1.3% in May, reviving recession concerns."
    publisher: "Rich Duprey"
    published_at: "2026-06-11T12:30:32.000Z"
    source_url: "https://247wallst.com/investing/2026/06/11/the-fed-just-quietly-released-surprisingly-bad-economic-news-is-a-recession-already-starting/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rich Duprey"
        source_url: "https://247wallst.com/investing/2026/06/11/the-fed-just-quietly-released-surprisingly-bad-economic-news-is-a-recession-already-starting/"
        retrieved_at: "2026-06-14T10:47:32+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via bea.gov annual GDP figure; the 10% price reflects that one month of soft spending data has not shifted the macro consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rich Duprey: The Fed Just Quietly Released Surprisingly Bad Economic News. Is a Rec"
    url: "https://247wallst.com/investing/2026/06/11/the-fed-just-quietly-released-surprisingly-bad-economic-news-is-a-recession-already-starting/"
    published_at: "2026-06-11T12:30:32.000Z"
    retrieved_at: "2026-06-14T10:47:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
