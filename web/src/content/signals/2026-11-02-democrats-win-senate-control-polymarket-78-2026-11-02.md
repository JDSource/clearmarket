---
signal_id: "CMSIG2026110204"
signal_slug: "democrats-win-senate-control-polymarket-78-2026-11-02"
headline: "Democrats win Senate control: Polymarket 78%"
semantic_title: "Democrats favored to win Senate control after midterm vote"
telemetry: "Polymarket 78%"
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
  current_price: 0.78
  volume_24h_usd: 1184745.461261
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democratic Senate control at 78%, making it a clear favorite heading into Election Day results."
  - "Voter economic discontent reported by Reuters and NYT polling is consistent with a Democratic lean, though the market is not pricing a certainty."
  - "Kalshi contract on Republicans controlling at least one chamber sits at 75%, implying markets assign meaningful probability to a split-chamber outcome."
  - "Resolution via Polymarket UMA oracle; delayed state certifications or runoffs could push final settlement well past Election Night."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Midterm Election Day arrives with control of both chambers at stake and economy-focused voters expressing sour sentiment toward Republicans."
    publisher: "Luke Fountain"
    published_at: "2026-11-02T10:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/11/02/midterm-election-stocks-defense-healthcare-crypto-ai.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Luke Fountain"
        source_url: "https://www.cnbc.com/2026/11/02/midterm-election-stocks-defense-healthcare-crypto-ai.html"
        retrieved_at: "2026-11-03T07:48:22+00:00"
  - type: "pm_response"
    notes: "Polymarket and Kalshi contracts are directionally consistent: Democrats favored in Senate, Republicans still above even odds on retaining at least one chamber."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Luke Fountain: Defense, healthcare, crypto and AI: How the midterm election could aff"
    url: "https://www.cnbc.com/2026/11/02/midterm-election-stocks-defense-healthcare-crypto-ai.html"
    published_at: "2026-11-02T10:00:00.000Z"
    retrieved_at: "2026-11-03T07:48:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
