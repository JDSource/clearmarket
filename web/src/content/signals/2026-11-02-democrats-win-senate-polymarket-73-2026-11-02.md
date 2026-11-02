---
signal_id: "CMSIG2026110205"
signal_slug: "democrats-win-senate-polymarket-73-2026-11-02"
headline: "Democrats win Senate: Polymarket 73%"
semantic_title: "Democrats favored but not certain to take Senate control"
telemetry: "Polymarket 73%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-02T10:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.73
  volume_24h_usd: 955697.827816
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats winning Senate control at 73%, leaving meaningful 27% odds on Republicans retaining it."
  - "The Senate race is closer than the House call, and sector analysts in the story flag Senate composition as decisive for regulatory agendas."
  - "Kalshi's companion contract (CM-EVT-T5VXKJT451) at 74% on Republicans controlling at least one chamber captures the residual Republican Senate scenario."
  - "The four-seat Democratic gain threshold referenced in Story 24 maps to a contested landscape that the 73% Polymarket price reflects."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Sector analysts flag the Senate as the key variable for midterm-driven policy shifts in defense, healthcare, crypto, and AI."
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
    notes: "Polymarket contract resolves via uma_oracle based on certified Senate election results following the 2026 midterms."
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
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
