---
signal_id: "CMSIG2026110204"
signal_slug: "democrats-win-house-kalshi-94-2026-11-02"
headline: "Democrats win House: Kalshi 94%"
semantic_title: "Democrats heavily favored to win the House in market pricing"
telemetry: "Kalshi 94%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-02T10:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.939
  volume_24h_usd: 1165644.47
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract puts Democrats winning the US House at 94%, a near-certain market outcome as of election eve."
  - "News coverage flags the House as the decisive chamber for sector policy; Kalshi's 94% pricing is consistent with that framing."
  - "The Polymarket Senate control contract (CM-EVT-M9WJY06T90) prices Democrats winning the Senate at 73%, implying a sweep scenario is the modal outcome."
  - "A Democratic House plus Democratic Senate result would have significant implications for defense spending, crypto regulation, and AI oversight priorities discussed in the story."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CNBC analysis examines how the midterm outcome could reshape policy exposure for defense, healthcare, crypto, and AI stocks."
    publisher: "Luke Fountain"
    published_at: "2026-11-02T10:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/11/02/midterm-election-stocks-defense-healthcare-crypto-ai.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Luke Fountain"
        source_url: "https://www.cnbc.com/2026/11/02/midterm-election-stocks-defense-healthcare-crypto-ai.html"
        retrieved_at: "2026-11-02T17:44:20+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Library of Congress certification of House composition following the 2026 midterms."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Luke Fountain: Defense, healthcare, crypto and AI: How the midterm election could aff"
    url: "https://www.cnbc.com/2026/11/02/midterm-election-stocks-defense-healthcare-crypto-ai.html"
    published_at: "2026-11-02T10:00:00.000Z"
    retrieved_at: "2026-11-02T17:44:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
