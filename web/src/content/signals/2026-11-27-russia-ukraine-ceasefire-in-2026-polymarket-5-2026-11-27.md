---
signal_id: "CMSIG2026112705"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-5-2026-11-27"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 5%"
semantic_title: "Russia-Ukraine ceasefire in 2026 stays a long shot at 5 percent"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-27T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.046
  volume_24h_usd: 976.140998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 5% chance of a Russia-Ukraine ceasefire in 2026, resolving via UMA oracle."
  - "US pressure escalation, nuclear submarine repositioning and diplomatic pressure, has not moved the market meaningfully; the news and the price are at odds."
  - "A companion Polymarket contract on Ukraine signing a full peace deal before 2027 sits at 6% (Story 28), while Ukraine agreeing to cede territory is at 3%, the spread is tight, suggesting markets see no path to any deal variant."
  - "Russia's largest air attack of the war this weekend (Story 29) is consistent with the low ceasefire probability; markets see escalation, not resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Trump administration repositioned nuclear submarines and pushed back on India-Russia ties in a new pressure campaign on Moscow to end the war in Ukraine."
    publisher: "link.cfr.org"
    published_at: "2026-11-27T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/40979402"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/40979402"
        retrieved_at: "2026-11-28T07:47:57+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; at 5%, the market is effectively treating a 2026 ceasefire as a tail event despite active US mediation efforts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/40979402"
    published_at: "2026-11-27T00:00:00.000Z"
    retrieved_at: "2026-11-28T07:47:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
