---
signal_id: "CMSIG2026071302"
signal_slug: "iranian-regime-falls-before-2027-polymarket-9-2026-07-13"
headline: "Iranian regime falls before 2027: Polymarket 9%"
semantic_title: "Iranian regime fall before 2027 holds as a slim tail"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-13T02:54:13.000Z"
event_id: "CM-EVT-QNQ4VPVP80"
event_slug: "will-the-iranian-regime-fall-by-the-end-of-2026"
event_question: "Will the Iranian regime fall before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb4d51e6364066d92eb6f9b8413dd7193de70966736044463b205834805a1f3b"
  question_raw: "Will the Iranian regime fall before 2027?"
  current_price: 0.09
  volume_24h_usd: 47338.994157
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices just 9% on the Iranian regime falling before 2027, treating escalating conflict as non-fatal to the government."
  - "Iran's negotiator sending messages to Washington while simultaneously widening attacks suggests durability; the market is consistent with that posture."
  - "At 18%, the US-invasion Polymarket contract (Story 21) also prices limited escalation, and a 9% regime-fall probability is coherent with that read."
  - "Resolves via Polymarket UMA oracle; requires an externally verifiable end to the current Iranian government structure before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's lead negotiator signaled continued resistance to Washington as new US strikes and Iranian counter-attacks spread across the Gulf."
    publisher: "abc.net.au"
    published_at: "2026-07-13T02:54:13.000Z"
    source_url: "https://www.abc.net.au/news/2026-07-13/iran-and-united-states-mou-interpretation-strait-of-hormuz/106908594"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "abc.net.au"
        source_url: "https://www.abc.net.au/news/2026-07-13/iran-and-united-states-mou-interpretation-strait-of-hormuz/106908594"
        retrieved_at: "2026-07-13T10:56:18+00:00"
  - type: "pm_response"
    notes: "Polymarket at 9% on regime fall and 18% on invasion form a coherent, low-probability escalation cluster despite the most intense Gulf fighting in years."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "abc.net.au: As new strikes rattle the Gulf, Iran's lead negotiator sends a clear m"
    url: "https://www.abc.net.au/news/2026-07-13/iran-and-united-states-mou-interpretation-strait-of-hormuz/106908594"
    published_at: "2026-07-13T02:54:13.000Z"
    retrieved_at: "2026-07-13T10:56:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
