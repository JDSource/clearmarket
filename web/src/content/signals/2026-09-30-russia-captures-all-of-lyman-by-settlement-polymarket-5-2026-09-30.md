---
signal_id: "CMSIG2026093008"
signal_slug: "russia-captures-all-of-lyman-by-settlement-polymarket-5-2026-09-30"
headline: "Russia captures all of Lyman by settlement: Polymarket 5%"
semantic_title: "Russia capturing all of Lyman by settlement stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-P275PM3SZ2"
event_slug: "will-russia-capture-all-of-lyman-by"
event_question: "Will Russia capture all of Lyman by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb4aea2573ecac699851b042d39a99b26e43aed7a6b024a4bc827ba220f9fbb78"
  question_raw: "Will Russia capture all of Lyman by December 31, 2026?"
  current_price: 0.051
  volume_24h_usd: 2014.762265
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts just 5% odds on Russia capturing all of Lyman by the settlement date, a strongly disfavored outcome."
  - "Ukraine's Vivaldi counteroffensive reaching Russian fortifications near Lyman is consistent with the low probability of a Russian capture."
  - "Russia's 27% war-budget increase signals sustained pressure heading into 2027, but the market is not pricing a near-term Lyman breakthrough."
  - "Resolution via Polymarket's UMA oracle; the settlement date is the binding constraint on whether escalated Russian spending translates to territorial gain in time."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia raised its 2027 war budget by 27% to a record while Ukraine's Vivaldi counteroffensive reached Russian fortifications near Lyman."
    publisher: "Euromaidan Press Staff"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://euromaidanpress.com/2026/09/30/russo-ukrainian-war-day-1679/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Euromaidan Press Staff"
        source_url: "https://euromaidanpress.com/2026/09/30/russo-ukrainian-war-day-1679/"
        retrieved_at: "2026-10-01T07:47:27+00:00"
  - type: "pm_response"
    notes: "Polymarket holds Lyman capture at 5%; the budget escalation news has not shifted the contract, as the market prices the military balance near Lyman as unfavorable to Russia."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Euromaidan Press Staff: Russo-Ukrainian war, day 1679: Russia raises its war budget by 27% to"
    url: "https://euromaidanpress.com/2026/09/30/russo-ukrainian-war-day-1679/"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-10-01T07:47:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
