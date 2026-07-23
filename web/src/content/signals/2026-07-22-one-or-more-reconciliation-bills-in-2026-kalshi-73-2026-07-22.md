---
signal_id: "CMSIG2026072207"
signal_slug: "one-or-more-reconciliation-bills-in-2026-kalshi-73-2026-07-22"
headline: "One or more reconciliation bills in 2026: Kalshi 73%"
semantic_title: "Consensus backs at least one reconciliation bill passing in 2026"
telemetry: "Kalshi 73%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-1WV8R9JXH3"
event_slug: "kxreccount-27"
event_question: "How many reconciliation bills will be passed in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECCOUNT-27-1"
  question_raw: "Will 1 reconciliation bills be passed in 2027?"
  current_price: 0.73
  volume_24h_usd: 73.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prices 73% probability that at least one reconciliation bill passes in 2026, reflecting meaningful but not certain legislative follow-through."
  - "House passage of a reconciliation blueprint is a concrete procedural step consistent with the 73% probability, the market is not skeptical of the news."
  - "The SAVE Act Kalshi contract sits at just 7%, showing the market sharply distinguishes between a reconciliation vehicle passing and any specific bill within it becoming law."
  - "Resolves via Library of Congress; Senate passage and presidential signature, not just House action, are required to resolve yes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "House Republicans passed a blueprint for reconciliation 3.0 alongside a 95 billion dollar Iran war funding package, advancing Speaker Mike Johnson's legislative agenda."
    publisher: "Kate Santaliz"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://www.axios.com/2026/07/22/house-republicans-reconciliation-iran-funding-save-act"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kate Santaliz"
        source_url: "https://www.axios.com/2026/07/22/house-republicans-reconciliation-iran-funding-save-act"
        retrieved_at: "2026-07-23T10:16:46+00:00"
  - type: "pm_response"
    notes: "Kalshi at 73% on reconciliation passing versus 7% on the SAVE Act specifically reveals the market pricing a high probability of process success but deep uncertainty on any individual measure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kate Santaliz: House GOP passes blueprint for reconciliation 3.0"
    url: "https://www.axios.com/2026/07/22/house-republicans-reconciliation-iran-funding-save-act"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-23T10:16:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
