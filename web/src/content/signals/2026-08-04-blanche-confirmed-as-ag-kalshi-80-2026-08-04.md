---
signal_id: "CMSIG2026080405"
signal_slug: "blanche-confirmed-as-ag-kalshi-80-2026-08-04"
headline: "Blanche confirmed as AG: Kalshi 80%"
semantic_title: "Todd Blanche confirmation stays heavily favored at 80%"
telemetry: "Kalshi 80%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-NY76DC3G68"
event_slug: "kxagconf-26"
event_question: "Will Todd Blanche be confirmed?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAGCONF-26JUN05-SEP01"
  question_raw: "Will Trump's first announced Attorney General pick be confirmed as Attorney General before Sep 1, 2026?"
  current_price: 0.8
  volume_24h_usd: 11660.1
  arbitration_model: "kalshi_staff"
  resolution_source: "U.S. Senate"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "Kalshi puts 80% odds on Todd Blanche being confirmed as U.S. Attorney General."
  - "Blanche's committee advancement is consistent with the 80% probability; the market had already assigned him heavy-favorite status ahead of the vote."
  - "The Kalshi vote-count ladder (CM-EVT-GMWVVJJ4S2) implies a final tally in the 50-51 senator range: 56% above 50, but only 14% above 51, indicating a narrow confirmation margin."
  - "Blanche's formal rescission of a prior position on Trump's tax audit immunity, reported in Story 16, appears to have been part of the deal to secure marginal Republican votes consistent with the implied thin margin."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Acting Attorney General Todd Blanche advanced out of the Senate Judiciary Committee, clearing a key procedural hurdle toward full Senate confirmation."
    publisher: "Hannah Rabinowitz"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/08/04/politics/todd-blanches-confirmation-expected-revitalize-doj-investigations"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Hannah Rabinowitz"
        source_url: "https://www.cnn.com/2026/08/04/politics/todd-blanches-confirmation-expected-revitalize-doj-investigations"
        retrieved_at: "2026-08-06T10:35:15+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via U.S. Senate; the vote-count ladder pinpoints a likely 50-51 confirmation, suggesting virtually no Democratic crossover support."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Hannah Rabinowitz: Todd Blanche advances toward confirmation, paving way for reenergized"
    url: "https://www.cnn.com/2026/08/04/politics/todd-blanches-confirmation-expected-revitalize-doj-investigations"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-06T10:35:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
